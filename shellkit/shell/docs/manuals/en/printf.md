# printf - Format and print text using C-style placeholders

## SYNOPSIS

    printf format [arguments...]


## DESCRIPTION

Print formatted output using C-style placeholders.

- Supports placeholders like `%s`, `%d`, `%f`, `%x`, etc.
- The format string and arguments both support escape sequences (e.g., `\n`, `\t`)
- No automatic newline is appended (unlike `echo`)


## FEATURES

- Format string is parsed and interpreted like in C's `printf`
- Each argument is matched to its corresponding placeholder
- Escape sequences are supported in both the format and values
- Supports all typical types: strings, integers, floats, hex, etc.


## EXAMPLES

Basic usage:

```shell
$ printf "Hello, %s!" World
Hello, World!$ 
```

Integer and float formatting:

```shell
$ printf "You have %d unread messages and %.2f GB used." 5 13.27
You have 5 unread messages and 13.27 GB used.$ 
```

Multiline output with escape sequences:

```shell
$ printf "Name:\t%s\nAge:\t%d\n" Alice 30
Name:	Alice
Age:	30
$ 
```


## NOTES

- Escape sequences like `\n`, `\t`, `\\` are automatically decoded.
- If argument count does not match placeholder count, extra arguments are ignored, and missing ones may result in formatting errors.
- Unlike `echo`, `printf` does **not** add a newline unless explicitly included in the format.
