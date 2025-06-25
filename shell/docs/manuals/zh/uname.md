# uname - 显示基本系统信息

## 用法（SYNOPSIS）

```shell
uname [options]
```


## 描述（DESCRIPTION）

使用内部的 `SYSINFO` 展示当前系统的信息。

* 默认仅显示操作系统名称；
* 通过选项可选择性输出硬件架构、内核版本等。


## 选项（OPTIONS）

* `-a`, `--all`
  一行内打印所有可用系统信息。

* `-m`, `--machine`
  显示硬件架构（如 `x86_64`、`arm64`）。

* `-r`, `--kernel-version`
  显示内核发布版本。

* `-s`, `--kernel-name`
  显示操作系统名称（如 `Linux`、`Darwin`）。


## 示例（EXAMPLES）

仅显示操作系统名称（默认）：

```shell
$ uname
```

显示全部可用信息：

```shell
$ uname -a
```

仅显示系统架构：

```shell
$ uname -m
```

仅显示内核版本：

```shell
$ uname -r
```

显式显示操作系统名称：

```shell
$ uname -s
```


## 说明（NOTES）

* 所有系统数据均通过内部环境变量 `$SYSINFO` 获取；
* 对于未知参数选项，将显示警告信息。
