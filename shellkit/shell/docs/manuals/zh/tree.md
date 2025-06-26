# tree - 使用系统 `tree` 命令展示目录结构

## 用法（SYNOPSIS）

```shell
tree [path] [options]
```


## 描述（DESCRIPTION）

以树状结构递归展示目录列表。

* 此命令是系统安装的 `tree` 工具的封装；
* 默认会排除常见的忽略目录（如 `.git`、`__pycache__`、`.venv` 等），除非显式覆盖；
* 所有附加参数将直接传递给底层的 `tree` 可执行文件。


## 默认忽略目录（DEFAULT IGNORED DIRECTORIES）

以下目录在默认情况下会被排除：

* `.git`, `.hg`, `.svn`
* `.idea`, `.vscode`, `.DS_Store`
* `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.tox`
* `.coverage`, `htmlcov`, `coverage.xml`
* `.venv`, `venv`, `env`
* `node_modules`
* `.trash`, `Thumbs.db`, `desktop.ini`


## 示例（EXAMPLES）

展示当前目录的树状结构：

```shell
$ tree
```

展示包括隐藏文件的完整树结构，并显示总结信息：

```shell
$ tree -v
```

显示两级目录深度并附带文件大小：

```shell
$ tree -L 2 -s
```

如需排除除默认规则外的其他目录，可使用 `-I` 追加自定义排除规则，例如：

```shell
$ tree -I "target"
```


## 说明（NOTES）

* 本命令依赖系统中的 `tree` 可执行文件，需位于 `$PATH` 中；

* 若未安装，将提示安装建议：

  * macOS: `brew install tree`
  * Ubuntu/Debian: `sudo apt install tree`

* 执行 `tree` 命令时如遇错误，将输出到标准错误流（stderr）。
