# copyright - 显示版权信息

## 用法（SYNOPSIS）

```shell
copyright
```


## 描述（DESCRIPTION）

显示项目 LICENSE 文件中的版权行。

* 读取项目根目录下的 `LICENSE` 文件；
* 在该行末尾追加 `All Rights Reserved.`；
* 如果 LICENSE 文件缺失或格式异常，则显示默认回退信息。


## 示例（EXAMPLES）

显示版权信息：

```shell
$ copyright
```

或：

```shell
$ copyright()
```


## 说明（NOTES）

* 该命令仅用于信息展示，不会验证 LICENSE 格式是否合法。
