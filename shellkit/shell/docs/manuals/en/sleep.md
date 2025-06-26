# sleep - Pause execution for a number of seconds

## SYNOPSIS

    sleep SECONDS [--quiet] [--countdown=TEXT] [--done=TEXT]


## DESCRIPTION

Pause shell execution for the specified number of seconds.

- Accepts a positive integer number of seconds.
- By default, displays a countdown timer.
- Use `--quiet` to suppress countdown output.
- Use `--countdown=TEXT` to customize the countdown message.
- Use `--done=TEXT` to customize the message shown after the wait completes.


## OPTIONS

- `--quiet`  
  Suppress the countdown timer and wait silently.

- `--countdown=TEXT`  
  Set a custom countdown message. You can include `{i}` as a placeholder for remaining seconds.

- `--done=TEXT`  
  Set a custom message to display when the countdown finishes.


## EXAMPLES

Sleep for 3 seconds with countdown.

```shell
$ sleep 3
```

Sleep for 5 seconds without output.

```shell
$ sleep 5 --quiet
```

Use custom countdown and done message.

```shell
$ sleep 3 --countdown="⌛ {i}..." --done="✅ Ready!"
```


## NOTES

- If the argument is missing or not a valid positive integer, an error will be shown.
- Countdown uses `\r` to update the line in place; on non-TTY environments, output may appear differently.
- Placeholders like `{i}` in `--countdown` will be replaced with remaining seconds.
