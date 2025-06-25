# echo - Print text with variable substitution and escape support

## SYNOPSIS

    echo [-n] [text...]


## DESCRIPTION

Print the given text to standard output with support for:

- Environment variable substitution (`$VAR`, `${VAR}`)
- Escaped variables are preserved as literals (`\$VAR`, `\${VAR}`)
- Standard escape sequences like `\n`, `\t`
- The `-n` option disables the trailing newline


## FEATURES

- `$VAR` and `${VAR}` are replaced using the current shell environment.
- To display literal variables (e.g. `$USER`), escape the dollar sign: `\$USER`.
- Common escape sequences (`\n`, `\t`, etc.) are interpreted.
- `-n` prevents automatic newline at the end of output.


## EXAMPLES

Print a line with newline:

```shell
$ echo "Hello\nWorld"
Hello
World
$ 
```

Print a line without newline:

```shell
$ echo -n "Hello, World"
Hello, World $ 
```

Substitute a variable:

```shell
$ export GREETING="World"
$ echo "Hello, $GREETING"
Hello, World
$ 
```

Escape the variable to prevent substitution:

```shell
$ echo "Hello, \$GREETING"
Hello, $GREETING
$ 
```


## NOTES

- Variable values are fetched from the current shell environment (`$USER`, `$HOME`, etc.).
- Use `export` to set environment variables before echoing.
- Backslash escapes use Python-style decoding: `\n`, `\t`, `\\`, etc.
