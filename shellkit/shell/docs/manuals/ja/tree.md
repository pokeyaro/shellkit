# tree - システムの `tree` コマンドを使ってディレクトリ構造を表示

## 使用法（SYNOPSIS）

```shell
tree [path] [options]
```


## 説明（DESCRIPTION）

ディレクトリ構造を再帰的にツリー形式で表示します。

* このコマンドはシステムにインストールされた `tree` ユーティリティのラッパーです；
* デフォルトでは、`.git`、`__pycache__`、`.venv` など一般的な除外対象のディレクトリは表示されません（明示的に上書き可能）；
* 追加のすべての引数はそのまま `tree` バイナリに渡されます。


## デフォルトの除外ディレクトリ（DEFAULT IGNORED DIRECTORIES）

以下のディレクトリは標準で除外されます：

* `.git`, `.hg`, `.svn`
* `.idea`, `.vscode`, `.DS_Store`
* `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.tox`
* `.coverage`, `htmlcov`, `coverage.xml`
* `.venv`, `venv`, `env`
* `node_modules`
* `.trash`, `Thumbs.db`, `desktop.ini`


## 使用例（EXAMPLES）

カレントディレクトリのツリーを表示：

```shell
$ tree
```

隠しファイルも含めた完全なツリーと概要を表示：

```shell
$ tree -v
```

2 階層までを表示し、ファイルサイズも含める：

```shell
$ tree -L 2 -s
```

デフォルトの除外対象以外にも独自の除外ルールを追加：

```shell
$ tree -I "target"
```


## 備考（NOTES）

* このコマンドは、`$PATH` 上に存在する `tree` バイナリに依存します；

* 見つからない場合はインストール手順を案内します：

  * macOS: `brew install tree`
  * Ubuntu/Debian: `sudo apt install tree`

* `tree` 実行時に発生したエラーは標準エラー出力（stderr）に出力されます。
