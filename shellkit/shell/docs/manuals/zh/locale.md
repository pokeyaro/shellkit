# locale - 显示或切换当前 Shell 语言

## 用法（SYNOPSIS）

```shell
locale [options]
locale [<language_code>]
```


## 描述（DESCRIPTION）

显示或更新 Shell 界面语言（locale）。

* 不带参数时，打印当前 `LANG` 设置；
* 传入合法语言代码（如 `en`、`zh`、`ja`）可切换界面语言；
* 支持列出所有可用语言。

切换语言会同时更新内部的 i18n 系统和环境变量 `LANG`。


## 选项（OPTIONS）

* `--list`, `-l`
  列出所有支持的语言代码。

* `-h`, `--help`
  显示帮助信息。


## 示例（EXAMPLES）

查看当前语言设置：

```shell
$ locale
LANG=en
```

切换为中文界面：

```shell
$ locale zh
LANG set to: zh
```

列出支持的语言：

```shell
$ locale --list
Supported languages:
  - en
  - zh
  - ja
  - ko
```


## 说明（NOTES）

* 可通过环境变量 `PYSH_LANG` 初始化语言设置；
* 若 `PYSH_LANG` 或 `LANG` 包含不支持的语言代码，则回退为 `en`；
* 此命令仅影响 Shell 界面语言，不影响系统全局语言配置。
