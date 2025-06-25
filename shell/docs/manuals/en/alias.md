# alias - Define or display command aliases

## SYNOPSIS

    alias
    alias NAME
    alias NAME='COMMAND'


## DESCRIPTION

Create or display shell command aliases.

- With no arguments, `alias` lists all defined aliases.
- With a single `NAME`, it shows the alias definition.
- With a `NAME='COMMAND'` pair, it defines a new alias.

Aliases act as shortcuts for frequently used commands.


## EXAMPLES

Define a new alias:

```shell
$ alias greet='echo Hello World'
$ greet
Hello World
```

Query a specific alias:

```shell
$ alias greet
greet='echo Hello World'
```

List all aliases:

```shell
$ alias
ll='ls -l'
la='ls -a'
greet='echo Hello World'
```

These aliases enhance convenience for commonly used commands.


## NOTES

- Aliases are **read-only** and currently **hardcoded**.
- If you want to see what an alias expands to, use:

```shell
$ which greet
greet: alias for 'echo Hello World'
```
