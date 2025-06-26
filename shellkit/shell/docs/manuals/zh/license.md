# license - 显示完整 LICENSE 内容

## 用法（SYNOPSIS）

```shell
license
```


## 描述（DESCRIPTION）

打印项目根目录下 LICENSE 文件的全部内容。

* 查找项目根目录中的 `LICENSE` 文件；
* 若找到，则原样输出其内容至标准输出；
* 若未找到，则显示回退提示信息。


## 示例（EXAMPLES）

显示完整的许可协议文本：

```shell
$ license
```

或：

```shell
$ license()
```


## 说明（NOTES）

* 输出内容不经处理，完整呈现所有许可条款的纯文本；
* 若文件不存在，输出内容如下：

  ```text
  （未找到 LICENSE 文件）
  ```
