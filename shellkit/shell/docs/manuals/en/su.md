# su - Switch to another user (Linux/macOS compatible)

## SYNOPSIS

    su [user]


## DESCRIPTION

Launch a new **login shell** under a different user account, using the current `pysh` as the shell interpreter.

* On **Linux**, this is implemented via `su [user] -s /path/to/pysh`
* On **macOS**, it falls back to `sudo /path/to/pysh` and does not support arguments.

The command replaces the current shell process using `os.execvp()` and never returns if successful.


## EXAMPLES

Switch to root on Linux:

```shell
$ su
```

Switch to another user named `admin` on Linux:

```shell
$ su admin
```

Launch a new shell as the current user on macOS (no arguments allowed):

```shell
$ su
```


## NOTES

* This command requires that your `pysh` binary is discoverable via `$PATH` or is being executed directly.
