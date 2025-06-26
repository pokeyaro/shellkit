# date - 显示当前日期和时间

## 用法（SYNOPSIS）

```shell
date [options]
```


## 描述（DESCRIPTION）

以多种格式显示当前系统时间。

* 默认显示本地时间，以易读格式输出。
* 支持 ISO 8601、UTC 和 Unix 时间戳格式。


## 选项（OPTIONS）

* `--iso`
  以 ISO 8601 格式显示时间（`YYYY-MM-DD HH:MM:SS`）。

* `--utc`
  显示 UTC 时间，而非本地时间。

* `--timestamp`
  以 Unix 时间戳输出当前时间（计算时点起始计积秒数）。

* `-h, --help`
  显示帮助信息。


## 示例（EXAMPLES）

显示本地系统时间（默认格式）：

```shell
$ date
```

以 ISO 8601 格式显示时间：

```shell
$ date --iso
```

显示 UTC 时间（默认格式）：

```shell
$ date --utc
```

显示当前 Unix 时间戳：

```shell
$ date --timestamp
```


## 说明（NOTES）

* 默认时间格式类似 GNU `date` 命令的输出。
* 当同时使用 `--utc` 和 `--iso` 时，只有首个匹配的选项生效。
