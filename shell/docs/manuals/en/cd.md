# cd - Change the current working directory

## SYNOPSIS

    cd [path]


## DESCRIPTION

Change the current working directory.

- `cd`  
  Change to the user's home directory.

- `cd ~`  
  Shortcut for the home directory.

- `cd -`  
  Switch to the previous working directory.

- `cd /path`  
  Navigate to the specified absolute or relative path.


## EXAMPLES

Go to the home directory.

```shell
$ cd
```

Go to the `Projects` folder under the home directory.

```shell
$ cd ~/Projects
```

Switch to the last visited directory.

```shell
$ cd -
```

Go to the system temporary directory.

```shell
$ cd /tmp
```


## NOTES

- The `cd` command updates both `$PWD` and `$OLDPWD`.
- Tilde `~` expansion resolves using the current user's home path.
