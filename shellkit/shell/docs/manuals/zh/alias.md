# alias - 定义或查看命令别名

## 用法（SYNOPSIS）

```
alias
alias 名称
alias 名称='命令'
```


## 描述（DESCRIPTION）

用于创建或查看 Shell 命令别名。

* 不带参数时，`alias` 会列出所有已定义的别名。
* 仅提供别名名称时，会显示该别名对应的命令。
* 使用 `名称='命令'` 格式时，会定义一个新的别名。

别名是对常用命令的快捷方式，有助于提升操作效率。


## 示例（EXAMPLES）

定义一个新的别名：

```shell
$ alias greet='echo Hello World'
$ greet
Hello World
```

查询某个别名的定义：

```shell
$ alias greet
greet='echo Hello World'
```

列出所有别名：

```shell
$ alias
ll='ls -l'
la='ls -a'
greet='echo Hello World'
```

使用别名可以简化常用命令的输入，提高便利性。


## 说明（NOTES）

* 当前别名为**只读**状态，且是**硬编码**写死的。
* 如果你想查看别名实际展开的命令，可以使用：

```shell
$ which greet
greet: alias for 'echo Hello World'
```
