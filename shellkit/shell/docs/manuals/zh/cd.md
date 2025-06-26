# cd - 切换当前工作目录

## 用法（SYNOPSIS）

```
cd [路径]
```

## 描述（DESCRIPTION）

切换当前的工作目录。

* `cd`
  切换到用户的主目录。

* `cd ~`
  主目录的快捷方式。

* `cd -`
  切换到上一个工作目录。

* `cd /路径`
  切换到指定的绝对路径或相对路径。


## 示例（EXAMPLES）

切换到主目录：

```shell
$ cd
```

切换到主目录下的 `Projects` 文件夹：

```shell
$ cd ~/Projects
```

切换到上一次访问的目录：

```shell
$ cd -
```

切换到系统临时目录：

```shell
$ cd /tmp
```


## 说明（NOTES）

* `cd` 命令会同时更新 `$PWD` 和 `$OLDPWD`。
* 波浪号 `~` 会被解析为当前用户的主目录路径。
