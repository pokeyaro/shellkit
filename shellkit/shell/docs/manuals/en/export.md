# export - Set or update environment variables

## SYNOPSIS

    export VAR=value [VAR2=value2 ...]

## DESCRIPTION

Set or update shell environment variables.

- Supports setting multiple key-value pairs in a single command.
- Keys must begin with a letter, underscore, or Chinese character.
- Values must be non-empty.


## EXAMPLES

Set a basic environment variable.

```shell
$ export USERNAME=alice
```

Set multiple variables at once.

```shell
$ export LANG="en_US.UTF-8" PS1="[admin@localhost ~]$ "
```


## NOTES

- Keys starting with `_ENV__` are **protected**: once set, they cannot be modified. 
- Certain system-defined keys (e.g., in the shell bootstrap) are immutable. 
- Setting `PS1` updates the shell prompt and supports ANSI escape sequences. 
- Invalid formats (e.g., missing `=` or empty values) will be ignored with warnings.
