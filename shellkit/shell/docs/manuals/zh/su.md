# su - 切换用户（兼容 Linux/macOS）

## 用法（SYNOPSIS）

    su [用户]


## 描述（DESCRIPTION）

使用当前 `pysh` 作为 shell 解释器，启动一个新的 **登录 shell**，以另一个用户身份运行。

* 在 **Linux** 上，实际执行为：`su [用户] -s /path/to/pysh`
* 在 **macOS** 上，会回退为：`sudo /path/to/pysh`，且不支持任何参数。

该命令会使用 `os.execvp()` 替换当前进程，成功后不会返回。


## 示例（EXAMPLES）

以 root 身份切换 shell（Linux）：

```shell
$ su
```

切换为名为 `admin` 的用户（Linux）：

```shell
$ su admin
```

以当前用户身份重新启动 shell（macOS，仅限无参数）：

```shell
$ su
```


## 说明（NOTES）

* 该命令要求 `pysh` 可通过 `$PATH` 找到，或当前正在直接执行 pysh 二进制文件。
