# locale - 現在のシェル言語を表示または変更

## 使用法（SYNOPSIS）

```shell
locale [options]
locale [<language_code>]
```


## 説明（DESCRIPTION）

シェルインターフェースの言語（ロケール）を表示または更新します。

* 引数がない場合、現在の `LANG` 設定を表示します；
* 有効な言語コード（例：`en`、`zh`、`ja`）を指定することで言語を変更できます；
* 利用可能な言語一覧の表示にも対応しています。

言語を変更すると、内部の i18n システムと環境変数 `LANG` の両方が更新されます。


## オプション（OPTIONS）

* `--list`, `-l`
  サポートされているすべての言語コードを一覧表示します。

* `-h`, `--help`
  このヘルプメッセージを表示します。


## 使用例（EXAMPLES）

現在のシェル言語を表示：

```shell
$ locale
LANG=en
```

シェルを中国語に切り替え：

```shell
$ locale zh
LANG set to: zh
```

利用可能な言語一覧を表示：

```shell
$ locale --list
Supported languages:
  - en
  - zh
  - ja
  - ko
```


## 備考（NOTES）

* 環境変数 `PYSH_LANG` により初期化時の言語を指定できます；
* `PYSH_LANG` または `LANG` に未サポートのコードが含まれる場合は `en` にフォールバックします；
* このコマンドはシェルインターフェースのみに影響し、システム全体のロケールには影響しません。
