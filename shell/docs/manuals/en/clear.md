# clear - Clear the terminal screen

## SYNOPSIS

    clear


## DESCRIPTION

Clear the terminal screen by sending an ANSI escape sequence.

- This command erases all visible content from the screen.
- After clearing, it moves the cursor to the top-left corner (row 1, column 1).
- Functionally equivalent to `cls` in Windows.


## EXAMPLES

Clears the screen and resets the cursor position.

```shell
$ clear
```


## NOTES

- Internally uses the ANSI escape sequence `\033[2J\033[H`.
- On terminals that do not support ANSI, the behavior may be undefined.
