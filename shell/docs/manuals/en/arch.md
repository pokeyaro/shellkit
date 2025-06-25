# arch - Show machine architecture

## SYNOPSIS

    arch [options]


## DESCRIPTION

Display the current machine's architecture.

- By default, the value is retrieved from PySH's internal `SYSINFO`, which is unified across platforms.
- With `--raw`, the command calls the system's `arch` utility for the original architecture string.


## OPTIONS

- `--raw` Get the raw architecture string from the system `arch` command.
- `-h, --help` Show this help message.


## EXAMPLES

Display the normalized architecture from PySH's internal SYSINFO.

```shell
$ arch
Architecture: x86_64
```

Fetch the raw architecture string from the system `arch` command.

```shell
$ arch --raw
Architecture (raw): i386
```


## NOTES

- The internal architecture is normalized and may differ slightly from the raw system result.
- This command helps distinguish cross-platform environments, such as distinguishing between Apple Silicon and Intel Macs.
