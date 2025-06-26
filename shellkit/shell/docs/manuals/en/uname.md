# uname - Show basic system information

## SYNOPSIS

    uname [options]


## DESCRIPTION

Display information about the current system using internal `SYSINFO`.

- By default, shows only the operating system name.
- With flags, you can selectively output machine architecture, kernel version, etc.


## OPTIONS

- `-a`, `--all`  
  Print all available system information in one line.

- `-m`, `--machine`  
  Show the hardware architecture (e.g., `x86_64`, `arm64`).

- `-r`, `--kernel-version`  
  Show the kernel release version.

- `-s`, `--kernel-name`  
  Show the operating system name (e.g., `Linux`, `Darwin`).


## EXAMPLES

Show only the OS name (default).

```shell
$ uname
```

Show all available information.

```shell
$ uname -a
```

Show architecture only.

```shell
$ uname -m
```

Show kernel version only.

```shell
$ uname -r
```

Show OS name explicitly.

```shell
$ uname -s
```


## NOTES

- All system data is retrieved from the internal environment variable `$SYSINFO`.
- Unknown flags will produce a warning message.
