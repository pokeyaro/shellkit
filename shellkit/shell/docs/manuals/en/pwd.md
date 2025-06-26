# pwd - Print working directory

## SYNOPSIS

    pwd


## DESCRIPTION

Display the current working directory path.

- Returns the absolute path to the current location in the filesystem.
- Equivalent to the standard Unix `pwd` command.


## EXAMPLES

Show the current directory.

```shell
$ pwd
/tmp
```


## NOTES

- The path is resolved using the internal environment's `$PWD`.
