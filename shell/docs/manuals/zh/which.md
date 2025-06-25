# which - 定位命令并显示其来源

## 用法（SYNOPSIS）

```shell
which COMMAND [COMMAND2 ...]
```


## 描述（DESCRIPTION）

确定指定命令的来源。

* 如果命令是 **Shell 内建命令**，将标注为内建；
* 如果是 **别名**，将显示其展开目标；
* 否则将在系统 `PATH` 中搜索外部可执行文件的位置。


## 示例（EXAMPLES）

定位一个内建命令：

```shell
$ which cd
```

定位一个别名：

```shell
$ which ll
```

定位一个外部程序：

```shell
$ which python
```

同时检查多个命令：

```shell
$ which clear cd echo
```


## 说明（NOTES）

* 内建命令和别名通过内部 Shell 逻辑解析；
* 其他命令名通过系统环境变量 `PATH` 进行查找；
* 若无法找到某命令，将显示警告信息。
