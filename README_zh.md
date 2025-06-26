# 🐚 ShellKit (libc + pysh)

> 亲手用 `Python` 拆解 `echo` 的工作原理：从命令行一路追到系统调用。

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/shellkit)](https://pypi.org/project/shellkit/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/pokeyaro/shellkit)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20中文%20%7C%20日本語%20%7C%20한국어-brightgreen)](./examples/)
[![CI](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml)

[English](./README.md) | **简体中文** | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 📖 项目简介

`ShellKit` 是一个类 `Unix` 教学型终端工具集，由两个子项目组成：

* **Libc**：用 `Python` 模拟 `C` 语言中的系统调用链，涵盖 `syscall`、`write`、`printf` 等底层机制，帮助理解用户态到内核态的完整流程。
* **Pysh**：一个具备内建命令、`REPL`、跨层追踪和多语言支持的交互式 `Shell`，构建于 `Libc` 之上，面向系统开发者与终端爱好者。

说明：可运行在 `macOS` / `Linux` 系统上，适配 `Arm64` 与 `Intel x86_64` 架构。


## ✨ 项目特性

### Pysh

* 🧠 内建命令引擎（如 `cd`、`echo`、`pwd`、`env` 等）
* 🧵 多语言支持（含英/中/日/韩完整命令手册）
* 🔍 跨层追踪系统：从命令解析 → `libc` 函数 → `C` 级 `syscall`
* 🧩 可组合的 `REPL` 执行模型
* 🔌 插件化命令注册系统

### Libc

* 🖨️ 自定义 `printf` 引擎，支持 `%s`、`%d`、`%f` 等格式符与转义序列
* 📜 `Python` ↔ `C` 的原生 `syscall` 桥接（通过 `syscall/syslib.so`）
* 🧪 覆盖 `libc` 核心行为的 `pytest` 测试用例，与关键 `benchmark` 性能测试


## 📦 安装方法

> ⚙️ 需要 `Python 3.10` 及以上版本

使用 `pip` 直接安装 `ShellKit`：

```bash
pip install shellkit
```

安装完成后，即可使用 `pysh` 命令启动交互式 `Shell`。


## 🚀 使用方法

```bash
pysh [选项]
```

### 命令行参数

| 参数             | 说明                                          |
|-----------------|----------------------------------------------|
| `--command`     | 执行单条命令                                   |
| `--no-banner`   | 跳过启动横幅                                   |
| `--no-reminder` | 禁用休息提醒功能                                |
| `--quiet`       | 安静模式启动，仅输出最少信息                      |
| `--safe`        | 启用安全模式，阻止如 `rm -rf /` 等高危险命令       |
| `--debug`       | 启用 `Shell` 层调试，显示命令解析与分发执行流程     |
| `--trace-echo`  | 追踪 `echo`/`printf` 在 `libc` 层的内部调用路径  |

可使用 `pysh --help` 查看更完整的帮助信息。


## 📚 示例与教程

想看看 ShellKit 的实际效果吗？查看我们的综合示例：

→ **[示例与演示](./examples/README_zh.md)** - 从基础到高级功能的真实终端会话

*包含多语言演示、调试教程和高级 printf 格式化！*


## 📦 项目结构（部分）

```text
shellkit/
├── native/         # C 编写的原生 syscall 实现源码（生成 syslib.so）
├── shellkit/       # 主包
│   ├── syscall/    # 原生 syscall 封装（通过 ctypes）
│   ├── libc/       # 自定义 libc 层（printf、write、exit）
│   ├── shell/      # 核心引擎、内建命令、运行时、REPL
│   ├── inspector/  # 调试与追踪系统
│   └── i18n/       # 多语言支持与翻译字典
├── benchmarks/     # 性能基准测试
├── examples/       # 使用示例与演示日志
└── tests/          # 测试套件
```


## 🧩 syslib.so 支持的平台

| 平台                        | 是否支持   | 备注                                    |
| -------------------------- |-----------|----------------------------------------|
| **Linux x86\_64**          | ✅ 支持   | 使用 `rax = 1` + `syscall` 指令          |
| **Linux ARM64**            | ✅ 支持   | 使用 `x8 = 64` + `svc #0`               |
| **macOS Intel (x86)**      | ✅ 支持   | 使用 `rax = 0x2000004` + `syscall`      |
| **macOS ARM64 (M1/M2/M3)** | ✅ 支持   | 使用 `syscall(SYS_write, ...)` 软封装    |
| **Windows**                | ❌ 不支持 | 未实现；Windows 没有统一的 `syscall()` 接口|


## 📌 更新日志

版本历史详见 [CHANGELOG.md](./CHANGELOG.md) 文件。


## 📜 许可证

本项目使用 `MIT License`，详情见 [LICENSE](./LICENSE) 文件。


## 🤝 鸣谢

灵感来源于经典 Unix Shell。 \
致谢所有系统级开发者与终端控用户。
