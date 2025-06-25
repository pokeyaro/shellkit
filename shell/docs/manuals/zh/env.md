# env - 打印环境变量

## 用法（SYNOPSIS）

```shell
env [options]
```


## 描述（DESCRIPTION）

显示当前的环境变量。

* 默认以 `KEY=VALUE` 形式列出所有键值对；
* 可选地以带语法高亮的 JSON 格式输出。


## 选项（OPTIONS）

* `--json`
  以 JSON 对象格式输出环境变量，支持彩色格式化。

* `-h, --help`
  显示帮助信息。


## 示例（EXAMPLES）

显示所有环境变量：

```shell
$ env
```

以 JSON 格式显示环境变量：

```shell
$ env --json
```


## 说明（NOTES）

* 环境变量通过内部变量存储器中的 `all_env()` 获取。
* JSON 输出主要用于调试和可读性增强。
