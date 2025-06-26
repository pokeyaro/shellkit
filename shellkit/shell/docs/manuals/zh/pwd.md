# pwd - 显示当前工作目录

## 用法（SYNOPSIS）

```shell
pwd
```


## 描述（DESCRIPTION）

显示当前所在的工作目录路径。

* 返回当前文件系统位置的绝对路径；
* 等价于标准 Unix 系统中的 `pwd` 命令。


## 示例（EXAMPLES）

显示当前目录：

```shell
$ pwd
/tmp
```


## 说明（NOTES）

* 路径通过内部环境变量 `$PWD` 获取并解析。
