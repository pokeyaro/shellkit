# whoami - 現在のユーザーを表示

## 使用法（SYNOPSIS）

```shell
whoami
```


## 説明（DESCRIPTION）

現在のシェルユーザーを表示します。

* 現在の `$USER` の値を取得して表示します；
* Unix の `whoami` コマンドと同等です。


## 使用例（EXAMPLES）

現在のユーザーを表示：

```shell
$ whoami
root
```


## 備考（NOTES）

* ユーザー情報は、内部環境変数 `$USER` から取得されます。
