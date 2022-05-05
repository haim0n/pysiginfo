#!/usr/bin/env python
import argparse
import logging
import os
import re
import signal
import subprocess
import sys
from distutils.spawn import find_executable
from typing import Iterable, Optional, Set

import psutil
from psutil import Process

pid_regex = re.compile(r'.+si_pid=([0-9]+),')


def get_sender_pid(strace_line: str) -> Optional[str]:
    match = pid_regex.match(strace_line)
    if match:
        return match.groups(1)[0]


def strace_err(line: str):
    exit_error(f'Strace returned an error: {line}')


def gen_strace_lines(pids: Iterable, sigs: Set):
    pid_args = ' '.join(f'-p {pid}' for pid in pids)
    sig_args = ' '.join(f'-e signal={sig}' for sig in sigs)
    strace_args = f'-d {sig_args} {pid_args}'
    strace_proc = subprocess.Popen(
        f'strace {strace_args}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0,
    )
    monitored_pid = None
    for l in strace_proc.stdout:
        enc_l = l.decode()
        if 'strace: next_event: dequeued pid' in enc_l:
            monitored_pid = enc_l.rsplit(maxsplit=1)[1]
        if 'si_pid=' in enc_l:
            yield f'monitored pid: {monitored_pid} event: {enc_l}'
        elif 'strace: Could not attach to process' in enc_l:
            strace_err(enc_l)


def get_pid_info(sender_pid) -> dict:
    try:
        p = Process(int(sender_pid))
        return p.as_dict(
            (
                'cmdline',
                'open_files',
                'connections',
                'create_time',
                'username',
                'ppid',
                'cwd',
            )
        )
    except Exception:
        return {'info': 'N/A'}


def exit_error(msg):
    print(msg)
    sys.exit(-1)


def _validate_pid(pid: int):
    try:
        psutil.Process(pid)
    except psutil.NoSuchProcess:
        exit_error(f'Error: invalid pid: {pid}')


def _validate_sig(sig: int):
    if not 0 <= sig < signal.NSIG:
        exit_error(
            f'Error: invalid sig: {sig} (legal values are [0..{signal.NSIG - 1}])'
        )


def validate_args(args):
    for pid in args.pids:
        _validate_pid(pid)
    for sig in args.sigs:
        _validate_sig(sig)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--pids',
        nargs='+',
        help='List of pids to monitor',
        type=int,
        required=True,
    )
    parser.add_argument(
        '-s',
        '--sigs',
        nargs='+',
        help='List of signals to monitor',
        default=[6],
        type=int,
    )
    return parser.parse_args()


def config_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        stream=sys.stdout,
    )


def validate_permissions():
    if os.geteuid():
        exit_error('error: insufficient priviligies, run as sudo')


def validate_strace():
    if not find_executable('strace'):
        exit_error('error: strace doesn\'t exist')


def main():
    args = get_args()
    validate_args(args)
    validate_permissions()
    validate_strace()
    config_logging()

    for line in gen_strace_lines(args.pids, sigs=set(args.sigs)):
        sender_pid = get_sender_pid(line)
        sender_pid_info = get_pid_info(sender_pid)
        out_line = f'{line.strip()}, sig sender: {sender_pid_info}'
        logging.info(out_line)


if __name__ == '__main__':
    main()
