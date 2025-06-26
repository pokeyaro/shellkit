# whoami - 显示当前用户

## 用法（SYNOPSIS）

```shell
whoami
```


## 描述（DESCRIPTION）

显示当前 Shell 用户。

* 从内部环境变量 `$USER` 获取用户信息；
* 等价于 Unix 系统中的 `whoami` 命令。


## 示例（EXAMPLES）

显示当前用户：

```shell
$ whoami
root
```


## 说明（NOTES）

* 用户信息通过内部环境变量 `$USER` 获取。
