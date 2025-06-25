# help - 显示内建命令的帮助信息

## 用法（SYNOPSIS）

```shell
help [COMMAND]
? [COMMAND]
```


## 描述（DESCRIPTION）

显示 shell 内建命令的帮助文档。

* 不带参数时，列出所有可用的内建命令；
* 指定命令名称时，显示对应的手册页（读取自 `docs/` 目录）。


## 示例（EXAMPLES）

列出所有内建命令：

```shell
$ help
```

查看 `cd` 命令的帮助信息：

```shell
$ help cd
```

使用简写语法：

```shell
$ ? cd
```


## 说明（NOTES）

* 帮助文档以 `.md` 文件形式存储在内部 `docs/` 目录下；
* 命令 `?` 是 `help` 的完整别名；
* 若未匹配到对应命令，将显示回退提示信息。
