# exit - Exit the current shell session

## SYNOPSIS

    exit [code]


## DESCRIPTION

Terminate the current shell session.

- If no exit code is provided, the shell exits with code `0`.
- If a numeric code is given, it will be used as the process's exit status.


## EXAMPLES

Exit the shell with default status `0`.

```shell
$ exit
```

Exit the shell with status code `42`.

```shell
$ exit 42
```


## NOTES

- Non-zero exit codes are typically used to indicate failure or abnormal termination.
- The exit code can be checked by the parent process or script that launched the shell.
- The following inputs are also accepted (for user convenience):

    ```shell
    $ quit
    $ quit()
    $ exit()
    $ Ctrl+D   (End-of-file / EOF)
    ```
    These are interpreted as `exit 0` unless otherwise specified.
