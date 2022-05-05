# pysiginfo


## Goal

pysignfo is a utility to retrieve information about process signals origin.


## Sample usage: Get the information on SIGABRT sender to your process:

```shell

$ siginfo -p 1234 -s 6 

2022-05-05 08:35:34,828 INFO     {si_signo=SIGABRT, si_code=SI_USER, si_pid=313939, si_uid=1000}, NULL, 8) = 6 (SIGABRT), {'open_files': [], 'cwd': '/home/haim0n/projects/pysiginfo', 'ppid': 8964, 'create_time': 1651644275.28, 'cmdline': ['/bin/bash'], 'username': 'haim0n', 'connections': []}

```

## Installation

```shell

$ pip install -U 'git+https://github.com/haim0n/pysiginfo.git'
```