# date - Show current date and time

## SYNOPSIS

    date [options]


## DESCRIPTION

Display the current system time in various formats.

- By default, shows the local time in a human-readable format.
- Supports ISO 8601, UTC, and Unix timestamp formats.


## OPTIONS

- `--iso`  
  Display time in ISO 8601 format (`YYYY-MM-DD HH:MM:SS`).

- `--utc`  
  Show UTC time instead of local time.

- `--timestamp`  
  Output current time as a Unix timestamp (seconds since epoch).

- `-h, --help`  
  Show this help message.


## EXAMPLES

Show local system time (default format).

```shell
$ date
```

Display time in ISO 8601 format.

```shell
$ date --iso
```

Display UTC time in default format.

```shell
$ date --utc
```

Display current Unix timestamp.

```shell
$ date --timestamp
```


## NOTES

- The default time format is similar to the output of GNU `date`.
- When both `--utc` and `--iso` are used, only the first matched option takes effect.
