# 🐚 ShellKit (libc + pysh)

> `echo` はどのように動作しているのかを、Shell から syscall まで Python で現象解析。

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/shellkit)](https://pypi.org/project/shellkit/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/pokeyaro/shellkit)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20中文%20%7C%20日本語%20%7C%20한국어-brightgreen)](./examples/)
[![CI](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml)

[English](./README.md) | [简体中文](./README_zh.md) | **日本語** | [한국어](./README_ko.md)

---

## 📖 概要

`ShellKit`は Unix 風の教育用ターミナルツールキットで、主に次の 2 つのサブプロジェクトから構成されています：

* **Libc**: C 言語の格納を Python で再現。`syscall` や `write`、`printf`など、ユーザーモードからカーネルモードまでの流れを現示。
* **Pysh**: `Libc`上に構築された、内藏コマンドや REPL、超階層トレースなどを搭載した互動型 Shell 。システム開発者や細かい操作を好むユーザー向け。

macOS や Linux に対応。Arm64 および x86\_64 アーキテクチャに対応しています。


## ✨ 特徴

### Pysh

* 🧠 内藏コマンド (`cd`、`echo`、`pwd`、`env`など)
* 🧵 複数言語に対応（英/中/日/韓 言語マニュアル搭載）
* 🔍 超階層トレース：コマンド解析 → libc 関数 → C システムコール
* 🧹 REPL 式実行モデル
* 🔌 プラグイン式コマンド管理

### Libc

* 📨 カスタム `printf` エンジン（`%s` や `%d` 、`%f`、エスケープ文字列に対応）
* 📜 `syscall/syslib.so` を用いた Python ↔ C ブリッジ
* 🧪 `pytest` でテスト済、ベンチマークも対応


## 📦 インストール

> `Python 3.10`以上が必要

`pip`でインストール:

```bash
pip install shellkit
```

インストール完了後に、次のように実行:

```bash
pysh
```


## 🚀 使用法

```bash
pysh [オプション]
```

### コマンドラインオプション

| オプション        | 説明                                                 |
| --------------- |------------------------------------------------------|
| `--command`     | 単一の指定コマンドを実行                                 |
| `--no-banner`   | 起動時のバナー表示をスキップ                              |
| `--no-reminder` | 休憩メッセージを無効化                                   |
| `--quiet`       | 静音モード。最少の出力み                                 |
| `--safe`        | セーフモード。`rm -rf /` などを無効化                     |
| `--debug`       | Shell 解析/実行のデバッグ情報を表示                       |
| `--trace-echo`  | `echo`や `printf` が `libc` でどのように実行されるかを追跡 |

より詳細は:

```bash
pysh --help
```


## 📚 サンプルとチュートリアル

ShellKit の実際の動作を見てみませんか？包括的なサンプルをご覧ください：

→ **[サンプルとデモ](./examples/README_ja.md)** - 基本から高度な機能まで、実際のターミナルセッション

*多言語デモ、デバッグチュートリアル、高度な printf フォーマット機能が含まれています！*


## 📦 プロジェクト構成 (一部)

```
pysh/
├── native/      # C 言語で書かれた syscall 実装
├── syscall/     # ctypes で Python から syscall を呼び出し
├── libc/        # カスタム libc (printf, write, exit)
├── shell/       # 核心エンジン、内藏コマンド、REPL
├── inspector/   # デバッグ・追跡モジュール
└── i18n/        # 多言語対応システム
```


## 🥉 syslib.so の対応プラットフォーム

| プラットフォーム              | 対応  | 備考                                  |
| -------------------------- |------|---------------------------------------|
| **Linux x86\_64**          | ✅   | `rax = 1` + `syscall` を使用           |
| **Linux ARM64**            | ✅   | `x8 = 64` + `svc #0` を使用            |
| **macOS Intel (x86)**      | ✅   | `rax = 0x2000004` + `syscall` を使用   |
| **macOS ARM64 (M1/M2/M3)** | ✅   | `syscall(SYS_write, ...)`をラッパー置換 |
| **Windows**                | ❌   | 非対応：統一的 `syscall()` が存在しない   |


## 📌 変更履歴

[変更履歴 (CHANGELOG.md)](./CHANGELOG.md) を参照してください。


## 📜 ライセンス

MIT ライセンスで提供しています。詳細は [LICENSE](./LICENSE) をご覧ください。


## 🤝 感謝

伝統的な Unix Shell の思想に感化して。\
すべてのシステム開発者、ターミナルユーザーに感謝します。
