# echo - 打印文本，支持变量替换与转义序列

## 用法（SYNOPSIS）

```shell
echo [-n] [text...]
```


## 描述（DESCRIPTION）

将指定文本打印到标准输出，支持以下功能：

* 环境变量替换（`$VAR`、`${VAR}`）
* 转义的变量保留为字面量（`\$VAR`、`\${VAR}`）
* 常见转义序列（如 `\n`、`\t`）
* 使用 `-n` 选项可取消末尾自动换行


## 特性（FEATURES）

* `$VAR` 与 `${VAR}` 会从当前 shell 环境中取值替换。
* 若需输出变量名本身（如 `$USER`），请转义美元符号：`\$USER`。
* 常见的转义序列（`\n`、`\t` 等）将被解析。
* `-n` 用于禁止末尾自动换行。


## 示例（EXAMPLES）

打印一行文本并换行：

```shell
$ echo "Hello\nWorld"
Hello
World
$ 
```

打印一行文本不换行：

```shell
$ echo -n "Hello, World"
Hello, World $ 
```

替换变量：

```shell
$ export GREETING="World"
$ echo "Hello, $GREETING"
Hello, World
$ 
```

转义变量避免替换：

```shell
$ echo "Hello, \$GREETING"
Hello, $GREETING
$ 
```


## 说明（NOTES）

* 变量值来源于当前 shell 环境（如 `$USER`、`$HOME` 等）。
* 可使用 `export` 预设变量供 echo 使用。
* 反斜杠转义遵循 Python 风格的解码规则：`\n`、`\t`、`\\` 等。
