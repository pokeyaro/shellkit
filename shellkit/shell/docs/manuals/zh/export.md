# export - 设置或更新环境变量

## 用法（SYNOPSIS）

```shell
export VAR=value [VAR2=value2 ...]
```


## 描述（DESCRIPTION）

设置或更新 shell 环境变量。

* 支持一次设置多个键值对；
* 键必须以字母、下划线或中文字符开头；
* 值不能为空字符串。


## 示例（EXAMPLES）

设置一个基本环境变量：

```shell
$ export USERNAME=alice
```

同时设置多个变量：

```shell
$ export LANG="en_US.UTF-8" PS1="[admin@localhost ~]$ "
```


## 说明（NOTES）

* 以 `_ENV__` 开头的键为**受保护变量**，设置后不可修改；
* 某些系统预定义变量（如 shell 启动时设定的）为只读；
* 设置 `PS1` 会更新 shell 提示符，支持 ANSI 转义序列；
* 格式非法（如缺失 `=` 或值为空）将被忽略并发出警告。
