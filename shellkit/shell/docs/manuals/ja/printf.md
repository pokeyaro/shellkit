# printf - Cスタイルのプレースホルダを使って整形出力

## 使用法（SYNOPSIS）

```shell
printf format [arguments...]
```


## 説明（DESCRIPTION）

C 言語スタイルのプレースホルダを用いて整形された出力を行います。

* `%s`, `%d`, `%f`, `%x` などのプレースホルダをサポート；
* フォーマット文字列および引数の両方でエスケープシーケンス（例：`\n`, `\t`）が使用可能；
* `echo` と異なり、自動で改行は追加されません。


## 機能（FEATURES）

* フォーマット文字列は C の `printf` のように解釈・処理されます；
* 各引数は対応するプレースホルダに一致して処理されます；
* フォーマットおよび値の中でエスケープシーケンスがサポートされます；
* 文字列、整数、浮動小数、16進数などの一般的な型をサポートします。


## 使用例（EXAMPLES）

基本的な使い方：

```shell
$ printf "Hello, %s!" World
Hello, World!$ 
```

整数と浮動小数の整形出力：

```shell
$ printf "You have %d unread messages and %.2f GB used." 5 13.27
You have 5 unread messages and 13.27 GB used.$ 
```

エスケープ付きの複数行出力：

```shell
$ printf "Name:\t%s\nAge:\t%d\n" Alice 30
Name:	Alice
Age:	30
$ 
```


## 備考（NOTES）

* `\n`, `\t`, `\\` などのエスケープシーケンスは自動的にデコードされます；
* 引数の数がプレースホルダ数と一致しない場合、余分な引数は無視され、不足していると整形エラーになることがあります；
* `echo` と異なり、改行は明示的にフォーマット文字列に含める必要があります。
