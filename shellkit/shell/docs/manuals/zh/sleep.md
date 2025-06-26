# sleep - 暂停执行指定秒数

## 用法（SYNOPSIS）

```shell
sleep SECONDS [--quiet] [--countdown=TEXT] [--done=TEXT]
```


## 描述（DESCRIPTION）

暂停 Shell 执行指定的秒数。

* 参数为正整数形式的秒数；
* 默认会显示倒计时进度；
* 使用 `--quiet` 可关闭倒计时输出；
* 使用 `--countdown=TEXT` 可自定义倒计时提示语；
* 使用 `--done=TEXT` 可自定义结束后显示的信息。


## 选项（OPTIONS）

* `--quiet`
  安静模式，不显示倒计时。

* `--countdown=TEXT`
  设置自定义倒计时提示语，可使用 `{i}` 占位符表示剩余秒数。

* `--done=TEXT`
  设置等待结束后显示的自定义消息。


## 示例（EXAMPLES）

倒计时 3 秒：

```shell
$ sleep 3
```

静默等待 5 秒：

```shell
$ sleep 5 --quiet
```

使用自定义倒计时与完成提示：

```shell
$ sleep 3 --countdown="⌛ {i}..." --done="✅ 完成！"
```


## 说明（NOTES）

* 若参数缺失或不是有效的正整数，将提示错误；
* 倒计时使用 `\r` 实时更新行内容，在非 TTY 环境中可能显示异常；
* `--countdown` 中的 `{i}` 占位符会被剩余秒数替换。
