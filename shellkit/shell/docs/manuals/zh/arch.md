# arch - 显示机器架构信息

## 用法（SYNOPSIS）

```
arch [选项]
```


## 描述（DESCRIPTION）

显示当前机器的架构信息。

* 默认情况下，架构信息来自 PySH 内部的 `SYSINFO`，该信息在跨平台之间进行了统一处理。
* 使用 `--raw` 选项时，将调用系统的 `arch` 命令，返回原始的架构字符串。


## 选项（OPTIONS）

* `--raw`  从系统 `arch` 命令获取原始架构字符串。
* `-h, --help` 显示此帮助信息。


## 示例（EXAMPLES）

显示来自 PySH 内部 SYSINFO 的标准化架构信息：

```shell
$ arch
Architecture: x86_64
```

获取来自系统 `arch` 命令的原始架构字符串：

```shell
$ arch --raw
Architecture (raw): i386
```


## 说明（NOTES）

* 内部架构信息为标准化格式，可能与系统的原始结果略有不同。
* 此命令有助于区分跨平台环境，例如区分 Apple Silicon 和 Intel 架构的 Mac。
