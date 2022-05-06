# pysiginfo


## Goal

pysignfo is a utility to retrieve information about process signals origin.


## Examples

### Get the information on SIGABRT sender to your process:

Run as root user:
```shell
$ siginfo -p 370291 -s 6 

2022-05-05 11:50:44,844 INFO  monitored pid: 370291 event: {si_signo=SIGABRT, si_code=SI_USER, si_pid=371479, si_uid=1000}, NULL, 8) = 6 (SIGABRT), sig sender: {'ppid': 8964, 'cwd': '/home/haim0n/projects/pysiginfo', 'open_files': [], 'connections': [], 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'create_time': 1651740638.48}
```

Run with sudo:
```shell
$ sudo $(which siginfo) -p 370291 -s 6 

2022-05-05 11:50:44,844 INFO  monitored pid: 370291 event: {si_signo=SIGABRT, si_code=SI_USER, si_pid=371479, si_uid=1000}, NULL, 8) = 6 (SIGABRT), sig sender: {'ppid': 8964, 'cwd': '/home/haim0n/projects/pysiginfo', 'open_files': [], 'connections': [], 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'create_time': 1651740638.48}
```

### Get the information on SIGABRT and SIGTERM senders to multiple processes:

Run as root user:
```shell
$ siginfo -p 370291 -p 381191 -s 6 -s 15 

2022-05-05 11:50:44,844 INFO  monitored pid: 370291 event: {si_signo=SIGABRT, si_code=SI_USER, si_pid=371479, si_uid=1000}, NULL, 8) = 6 (SIGABRT), sig sender: {'ppid': 8964, 'cwd': '/home/haim0n/projects/pysiginfo', 'open_files': [], 'connections': [], 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'create_time': 1651740638.48}
2022-05-05 15:05:25,009 INFO  monitored pid: 370291 event: {si_signo=SIGTERM, si_code=SI_USER, si_pid=23965, si_uid=1005} ---, sig sender: {'ppid': 8964, 'cwd': '/home/haim0n/projects/pysiginfo', 'open_files': [], 'connections': [], 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'create_time': 1651740638.48}
```


## Installation

```shell

$ pip install -U 'git+https://github.com/haim0n0n/pysiginfo.git'
```