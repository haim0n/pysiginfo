# pysiginfo


## Goal

pysignfo is a utility to retrieve information about process signals origin.


## Sample usage: Get the information on SIGABRT sender to your process:

```shell

$ siginfo -p 1234 -s 6 

2022-05-05 11:50:44,844 INFO  monitored pid: 370291 event: {si_signo=SIGABRT, si_code=SI_USER, si_pid=371479, si_uid=1000}, NULL, 8) = 6 (SIGABRT), sig sender: {'ppid': 8964, 'cwd': '/home/haim0n/projects/pysiginfo', 'open_files': [], 'connections': [], 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'create_time': 1651740638.48}
```

## Installation

```shell

$ pip install -U 'git+https://github.com/haim0n0n/pysiginfo.git'
```