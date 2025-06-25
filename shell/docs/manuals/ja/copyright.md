# copyright - ライセンス著作権行の表示

## 使用法（SYNOPSIS）

```shell
copyright
```


## 説明（DESCRIPTION）

`LICENSE` ファイルから著作権の行を表示します。

* プロジェクトのルートディレクトリにある `LICENSE` ファイルを読み取ります；
* 読み取った行の末尾に `All Rights Reserved.` を追加します；
* `LICENSE` ファイルが存在しない場合や形式が不正な場合は、フォールバックメッセージを表示します。


## 使用例（EXAMPLES）

著作権情報を表示：

```shell
$ copyright
```

または：

```shell
$ copyright()
```


## 備考（NOTES）

* 出力は情報表示のみであり、ライセンス形式の検証は行いません。
