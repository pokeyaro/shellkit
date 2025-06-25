# tree - Display directory structure using the system `tree` command

## SYNOPSIS

    tree [path] [options]


## DESCRIPTION

Display a recursive directory listing in a tree-like format.

- This command is a wrapper around the system-installed `tree` utility.
- By default, commonly ignored directories (e.g., `.git`, `__pycache__`, `.venv`) are excluded unless overridden.
- All additional arguments are passed directly to the underlying `tree` binary.


## DEFAULT IGNORED DIRECTORIES

The following directories are excluded by default:

- `.git`, `.hg`, `.svn`
- `.idea`, `.vscode`, `.DS_Store`
- `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.tox`
- `.coverage`, `htmlcov`, `coverage.xml`
- `.venv`, `venv`, `env`
- `node_modules`
- `.trash`, `Thumbs.db`, `desktop.ini`


## EXAMPLES

Display a tree for the current directory.

```shell
$ tree
```

Show full tree including hidden files and report summary.

```shell
$ tree -v
```

Show 2 levels deep with file sizes.

```shell
$ tree -L 2 -s
```

To exclude additional directories beyond the default ones, use `-I` with your own values. For example:

```shell
$ tree -I "target"
```


## NOTES

- This command requires the system `tree` binary to be available in `$PATH`.
- If missing, the shell will suggest how to install it:

  - macOS: `brew install tree`
  - Ubuntu/Debian: `sudo apt install tree`

- Any errors encountered while invoking `tree` are reported to stderr.
