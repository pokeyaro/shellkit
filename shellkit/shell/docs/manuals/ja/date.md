# date - 現在の日付と時刻を表示

## 使用法（SYNOPSIS）

```shell
date [options]
```


## 説明（DESCRIPTION）

現在のシステム時刻をさまざまな形式で表示します。

* デフォルトでは、人間に読みやすい形式でローカル時刻を表示します；
* ISO 8601、UTC、Unixタイムスタンプ形式をサポートします。


## オプション（OPTIONS）

* `--iso`
  ISO 8601 形式（`YYYY-MM-DD HH:MM:SS`）で時刻を表示します。

* `--utc`
  ローカル時刻の代わりに UTC 時刻を表示します。

* `--timestamp`
  現在の時刻を Unix タイムスタンプ（エポックからの秒数）として出力します。

* `-h, --help`
  このヘルプメッセージを表示します。


## 使用例（EXAMPLES）

ローカル時刻を表示（デフォルト形式）：

```shell
$ date
```

ISO 8601 形式で表示：

```shell
$ date --iso
```

UTC 時刻を表示：

```shell
$ date --utc
```

Unix タイムスタンプを表示：

```shell
$ date --timestamp
```


## 備考（NOTES）

* デフォルトの時刻形式は GNU `date` の出力に似ています；
* `--utc` と `--iso` の両方を指定した場合、最初に一致したオプションのみが有効になります。
