# printf - 使用 C 风格占位符格式化并打印文本

## 用法（SYNOPSIS）

```shell
printf format [arguments...]
```


## 描述（DESCRIPTION）

使用 C 风格的占位符格式化输出文本。

* 支持 `%s`、`%d`、`%f`、`%x` 等占位符；
* 格式字符串与参数均支持转义序列（如 `\n`、`\t`）；
* 不会自动添加换行符（不同于 `echo`）。


## 特性（FEATURES）

* 格式字符串将按 C 语言中的 `printf` 规则解析；
* 每个参数对应格式字符串中的一个占位符；
* 格式与参数中都可使用转义序列；
* 支持常见类型：字符串、整数、浮点数、十六进制等。


## 示例（EXAMPLES）

基本用法：

```shell
$ printf "Hello, %s!" World
Hello, World!$ 
```

整数和浮点数格式化：

```shell
$ printf "You have %d unread messages and %.2f GB used." 5 13.27
You have 5 unread messages and 13.27 GB used.$ 
```

多行输出及转义序列：

```shell
$ printf "Name:\t%s\nAge:\t%d\n" Alice 30
Name:	Alice
Age:	30
$ 
```


## 说明（NOTES）

* `\n`、`\t`、`\\` 等转义序列将自动解码；
* 如果参数数量与占位符不匹配：多余的参数会被忽略，缺失的参数可能导致格式错误；
* 与 `echo` 不同，`printf` **不会** 自动添加换行，需在格式中显式指定。
