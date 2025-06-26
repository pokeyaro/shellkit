# env - Print environment variables

## SYNOPSIS

    env [options]


## DESCRIPTION

Display the current environment variables.

- By default, prints all key-value pairs in `KEY=VALUE` format.
- Can optionally output as JSON with syntax highlighting.


## OPTIONS

- `--json`  
  Output environment variables as a JSON object with color formatting.

- `-h, --help`  
  Show this help message.


## EXAMPLES

Show all environment variables.

```shell
$ env
```

Display environment variables in JSON format.

```shell
$ env --json
```


## NOTES

- The environment is retrieved from the internal variable store via `all_env()`.
- JSON output is mainly for readability and debugging purposes.
