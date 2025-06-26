# locale - Show or change current shell language

## SYNOPSIS

    locale [options]
    locale [<language_code>]


## DESCRIPTION

Display or update the shell interface language (locale).

- If no argument is provided, prints the current `LANG` setting.
- Accepts a valid language code (e.g. `en`, `zh`, `ja`) to change the language.
- Supports listing all available languages.

Changing the language updates both the internal i18n system and the environment variable `LANG`.


## OPTIONS

- `--list`, `-l`  
  List all supported language codes.

- `-h`, `--help`  
  Show this help message.


## EXAMPLES

Show current shell language:

```shell
$ locale
LANG=en
```

Switch to Chinese interface:

```shell
$ locale zh
LANG set to: zh
```

List available languages:

```shell
$ locale --list
Supported languages:
  - en
  - zh
  - ja
  - ko
```


## NOTES

- The language setting can be initialized via the environment variable `PYSH_LANG`.
- If `PYSH_LANG` or `LANG` contains an unsupported code, it will fallback to `en`.
- This command only affects the shell interface, not the system-wide locale.
