# clear - 清空终端屏幕

## 用法（SYNOPSIS）

    clear


## 描述（DESCRIPTION）

通过发送 ANSI 转义序列清空终端屏幕。

* 此命令会清除屏幕上所有可见内容。
* 清空后，光标将移动至屏幕左上角（第 1 行，第 1 列）。
* 在功能上等同于 Windows 系统中的 `cls` 命令。


## 示例（EXAMPLES）

清空屏幕并重置光标位置：

```shell
$ clear
```


## 说明（NOTES）

* 内部使用的 ANSI 转义序列为 `\033[2J\033[H`。
* 对于不支持 ANSI 的终端，其行为可能无法预期。
