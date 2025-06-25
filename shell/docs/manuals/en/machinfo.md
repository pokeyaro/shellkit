# machinfo - Show detailed machine information

## SYNOPSIS

    machinfo [--json] [--short]


## DESCRIPTION

Display comprehensive machine/system information.

- Shows platform, CPU, memory, disk, and GPU details.
- Default output is a multi-section rich layout with icons and formatting.
- Supports compact summary or structured JSON formats.


## OPTIONS

- `--json`  
  Output full machine information as formatted JSON.

- `--short`  
  Print a brief summary in one line.


## EXAMPLES

Display full machine information (default view).

```shell
$ machinfo
```

Print a brief summary line.

```shell
$ machinfo --short
```

Output raw machine info as JSON.

```shell
$ machinfo --json
```


## NOTES

- This command gathers internal system metadata via `get_sysinfo()`.
- The presence and accuracy of fields may vary depending on the runtime platform.
