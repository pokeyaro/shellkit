# help - Show help for built-in commands

## SYNOPSIS

    help [COMMAND]
    ? [COMMAND]


## DESCRIPTION

Display help information for shell built-ins.

- With no arguments, shows a list of all available built-in commands.
- With a specific command name, displays the corresponding manual page (from `docs/`).


## EXAMPLES

Show a list of all built-in commands.

```shell
$ help
```

Show help for the `cd` command.

```shell
$ help cd
```

Alternate shorthand syntax.

```shell
$ ? cd
```


## NOTES

- Help files are stored as `.md` documents under the internal `docs/` directory. 
- The command `?` is a full alias of `help`. 
- If no matching command is found, a fallback message is displayed.
