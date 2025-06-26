# license - Display full LICENSE content

## SYNOPSIS

    license


## DESCRIPTION

Print the full contents of the project's LICENSE file.

- Looks for a file named `LICENSE` at the project root.
- If the file is found, it is printed as-is to standard output.
- If not found, a fallback message is displayed.


## EXAMPLES

Show full license text.

```shell
$ license
```

or

```shell
$ license()
```


## NOTES

- The output is unprocessed and includes all license terms as plain text.
- If the file is missing, the output will be:

    ```text
    (No LICENSE file found)
    ```
