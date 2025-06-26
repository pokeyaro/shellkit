# machinfo - 显示详细的机器信息

## 用法（SYNOPSIS）

```shell
machinfo [--json] [--short]
```


## 描述（DESCRIPTION）

展示完整的机器 / 系统信息。

* 包含平台、CPU、内存、磁盘和 GPU 等详细信息；
* 默认输出为多段式结构化布局，带有图标和格式化效果；
* 支持简要摘要或结构化 JSON 格式。


## 选项（OPTIONS）

* `--json`
  以格式化 JSON 形式输出完整的机器信息。

* `--short`
  以一行摘要形式输出简要信息。


## 示例（EXAMPLES）

显示完整的机器信息（默认视图）：

```shell
$ machinfo
```

打印一行简要摘要：

```shell
$ machinfo --short
```

以 JSON 格式输出原始机器信息：

```shell
$ machinfo --json
```


## 说明（NOTES）

* 本命令通过 `get_sysinfo()` 收集系统元数据；
* 字段的完整性和准确性可能因运行平台不同而有所差异。
