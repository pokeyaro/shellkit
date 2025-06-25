# whoami - Show the current user

## SYNOPSIS

    whoami


## DESCRIPTION

Display the current shell user.

- Retrieves the value of the current `$USER`.
- Equivalent to the Unix `whoami` command.


## EXAMPLES

Show the current user.

```shell
$ whoami
root
```


## NOTES

- The user value is retrieved from the internal environment variable `$USER`.
