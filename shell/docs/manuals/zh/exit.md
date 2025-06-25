# exit - 退出当前 Shell 会话

## 用法（SYNOPSIS）

```shell
exit [code]
```


## 描述（DESCRIPTION）

终止当前的 Shell 会话。

* 若未提供退出码，则默认以 `0` 退出；
* 若提供数字参数，将作为进程的退出状态码返回。


## 示例（EXAMPLES）

以默认状态码 `0` 退出 Shell：

```shell
$ exit
```

以状态码 `42` 退出 Shell：

```shell
$ exit 42
```


## 说明（NOTES）

* 非零退出码通常用于指示失败或异常终止；
* 父进程或调用该 Shell 的脚本可读取退出码；
* 以下输入也被识别为退出命令（等价于 `exit 0`）：

  ```shell
  $ quit
  $ quit()
  $ exit()
  $ Ctrl+D   （文件结束 / EOF）
  ```
