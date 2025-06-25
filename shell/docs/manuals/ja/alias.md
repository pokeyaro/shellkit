# alias - コマンドエイリアスの定義または表示

## 使用法（SYNOPSIS）

```
alias
alias 名前
alias 名前='コマンド'
```


## 説明（DESCRIPTION）

Shell コマンドのエイリアスを作成または表示します。

* 引数なしで `alias` を実行すると、定義済みのすべてのエイリアスが表示されます。
* 名前のみを指定すると、そのエイリアスの定義が表示されます。
* `名前='コマンド'` の形式で新しいエイリアスを定義できます。

エイリアスは頻繁に使用するコマンドのショートカットとして機能し、操作の効率を高めます。


## 使用例（EXAMPLES）

新しいエイリアスを定義する：

```shell
$ alias greet='echo Hello World'
$ greet
Hello World
```

特定のエイリアスを確認する：

```shell
$ alias greet
greet='echo Hello World'
```

すべてのエイリアスを一覧表示する：

```shell
$ alias
ll='ls -l'
la='ls -a'
greet='echo Hello World'
```

エイリアスを活用することで、よく使うコマンドの入力が簡略化され、利便性が向上します。


## 備考（NOTES）

* 現在のエイリアスは**読み取り専用**であり、**ハードコード**されています。
* エイリアスが展開される実際のコマンドを確認するには、次のコマンドを使います：

```shell
$ which greet
greet: alias for 'echo Hello World'
```
