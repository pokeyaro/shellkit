# copyright - Show license copyright line

## SYNOPSIS

    copyright


## DESCRIPTION

Display the copyright line from the LICENSE file.

- Reads the project's top-level `LICENSE` file.
- Appends `All Rights Reserved.` after the line.
- If the LICENSE file is missing or malformed, a fallback message is shown.


## EXAMPLES

Show copyright text.

```shell
$ copyright
```

or

```shell
$ copyright()
```


## NOTES

- The output is purely informational and does not validate license format.
