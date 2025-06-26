# which - Locate a command and show its source

## SYNOPSIS

    which COMMAND [COMMAND2 ...]


## DESCRIPTION

Determine the source of a given command.

- If the command is a **shell builtin**, it is marked as such.
- If it's an **alias**, the expansion target is shown.
- Otherwise, the system PATH is searched to locate the external executable.


## EXAMPLES

Locate a builtin command.

```shell
$ which cd
```

Locate an alias.

```shell
$ which ll
```

Locate an external program.

```shell
$ which python
```

Check multiple commands at once.

```shell
$ which clear cd echo
```


## NOTES

- Builtins and aliases are resolved through internal shell logic. 
- All other names are resolved using the system `PATH`. 
- If a command cannot be found, a warning is displayed.
