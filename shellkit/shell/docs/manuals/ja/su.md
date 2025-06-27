# su - ユーザーを切り替える（Linux/macOS 対応）

## 使用法（SYNOPSIS）

    su [ユーザー]


## 説明（DESCRIPTION）

現在の `pysh` をシェルインタプリタとして使用し、別のユーザーとして新しい **ログインシェル** を起動します。

* **Linux** では、実際に実行されるコマンドは：`su [ユーザー] -s /path/to/pysh`
* **macOS** では、`sudo /path/to/pysh` にフォールバックされ、引数はサポートされません。

このコマンドは `os.execvp()` を使って現在のプロセスを置き換え、成功すると戻りません。


## 使用例（EXAMPLES）

root としてシェルに切り替える（Linux）：

```shell
$ su
```

`admin` という名前のユーザーに切り替える（Linux）：

```shell
$ su admin
```

現在のユーザーとしてシェルを再起動する（macOS、引数なしのみ）：

```shell
$ su
```


## 備考（NOTES）

* このコマンドを使用するには、`pysh` バイナリが `$PATH` にあるか、直接実行されている必要があります。
