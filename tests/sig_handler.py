#! /usr/bin/python3

import os
import signal


def dummy_sig_handler(sig_num, frame):
    pass


def main():
    signal.signal(signal.SIGABRT, dummy_sig_handler)
    pid = os.getpid()
    print(f"Hi, I'm {pid}, talk to me with 'kill -SIGABRT {pid}'")

    # wait for signal info
    while True:
        siginfo = signal.sigwaitinfo({signal.SIGABRT})
        print(
            f"got {siginfo.si_signo} from {siginfo.si_pid} by user {siginfo.si_uid}\n"
        )


if __name__ == '__main__':
    main()
