# echo - 変数展開とエスケープ対応のテキスト出力

## 使用法（SYNOPSIS）

```shell
echo [-n] [text...]
```


## 説明（DESCRIPTION）

指定されたテキストを標準出力に表示します（以下の機能をサポート）。

* 環境変数の展開（`$VAR`, `${VAR}`）
* エスケープされた変数（`\$VAR`, `\${VAR}`）はリテラルとして扱われます
* 標準的なエスケープシーケンス（例：`\n`, `\t`）を解釈します
* `-n` オプションで末尾の改行を抑制します


## 機能（FEATURES）

* `$VAR` や `${VAR}` は現在のシェル環境から値が取得されて置き換えられます；
* リテラル変数を表示したい場合は、ドル記号をエスケープ（例：`\$USER`）してください；
* `\n`, `\t` などのエスケープシーケンスをサポート；
* `-n` を使用すると出力の末尾に自動改行が入りません。


## 使用例（EXAMPLES）

改行付きで出力：

```shell
$ echo "Hello\nWorld"
Hello
World
$ 
```

改行なしで出力：

```shell
$ echo -n "Hello, World"
Hello, World $ 
```

変数を展開：

```shell
$ export GREETING="World"
$ echo "Hello, $GREETING"
Hello, World
$ 
```

変数展開を抑制（リテラル表示）：

```shell
$ echo "Hello, \$GREETING"
Hello, $GREETING
$ 
```


## 備考（NOTES）

* 変数の値はシェルの環境変数（例：`$USER`, `$HOME`）から取得されます；
* 事前に `export` を使って環境変数を設定してください；
* バックスラッシュによるエスケープは Python 風のデコード規則（`\n`, `\t`, `\\` など）に従います。
