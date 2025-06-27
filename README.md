# 🐚 ShellKit (libc + pysh)

> Learn how `echo` works from shell to syscall — all in one Python playground.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/shellkit)](https://pypi.org/project/shellkit/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/pokeyaro/shellkit)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20中文%20%7C%20日本語%20%7C%20한국어-brightgreen)](./examples/)
[![CI](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml)

**English** | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md)

---

## 📖 Overview

`ShellKit` is a Unix-like educational terminal toolkit consisting of two main components:

* **Libc**: A Python-based simulation of core C library calls such as `syscall`, `write`, and `printf`. It walks through the transition from user space to kernel space.
* **Pysh**: An interactive shell built on top of `Libc`, featuring internal commands, REPL execution, cross-layer tracing, and multilingual support. Designed for system developers and terminal enthusiasts.

Runs on both `macOS` and `Linux`, supporting `Arm64` and `Intel x86_64` architectures.


## ✨ Features

### Pysh

* 🧠 Built-in commands (`cd`, `echo`, `pwd`, `env`, etc.)
* 🧵 Multilingual support with full manuals (EN/CH/JP/KR)
* 🔍 Cross-layer tracing: from command parsing → libc functions → C-level syscalls
* 🧹 Composable REPL execution model
* 🔌 Pluggable command registration system

### Libc

* 📨 Custom `printf` engine with `%s`, `%d`, `%f` format specifiers and escape sequences
* 📜 Native syscall bridge (Python ↔ C) via `syscall/syslib.so`
* 🧪 Unit-tested via `pytest`, with benchmarks for key libc behaviors


## 📦 Installation

> Requires `Python 3.10` or newer

Install via `pip`:

```bash
pip install shellkit
```

After installation, launch the interactive shell with:

```bash
pysh
```


## 🚀 Usage

```bash
pysh [options]
```

### CLI Options

| Option          | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| `--command`     | Run a single command                                           |
| `--no-banner`   | Skip the startup banner                                        |
| `--no-reminder` | Disable rest reminder messages                                 |
| `--quiet`       | Quiet mode with minimal output                                 |
| `--safe`        | Enable safety mode (blocks dangerous commands like `rm -rf /`) |
| `--debug`       | Enable shell-level debug output                                |
| `--trace-echo`  | Trace `echo`/`printf` calls down to `libc` syscall layer       |

For more, run:

```bash
pysh --help
```


## 📚 Examples & Tutorials

Want to see ShellKit in action? Check out our comprehensive examples:

→ **[Examples & Demos](./examples/README.md)** - Real terminal sessions from basic to advanced features

*Complete with multilingual demos, debugging tutorials, and advanced printf formatting!*


## 📦 Project Structure (partial)

```text
shellkit/
├── native/         # C code for native syscall implementation (builds syslib.so)
├── shellkit/       # Main package
│   ├── syscall/    # Python-side syscall wrappers via ctypes
│   ├── libc/       # Custom libc (printf, write, exit)
│   ├── shell/      # Core engine, built-in commands, runtime, REPL
│   ├── inspector/  # Debugging and tracing tools
│   └── i18n/       # Multilingual dictionaries and support
├── benchmarks/     # Performance benchmarks
├── examples/       # Usage examples and demo logs
└── tests/          # Test suite
```


## 🥉 Platform Support for syslib.so

| Platform                   | Supported  | Notes                                          |
| -------------------------- |------------| ---------------------------------------------- |
| **Linux x86\_64**          | ✅ Yes     | Uses `rax = 1` + `syscall`                     |
| **Linux ARM64**            | ✅ Yes     | Uses `x8 = 64` + `svc #0`                      |
| **macOS Intel (x86)**      | ✅ Yes     | Uses `rax = 0x2000004` + `syscall`             |
| **macOS ARM64 (M1/M2/M3)** | ✅ Yes     | Uses `syscall(SYS_write, ...)` (soft wrapper)  |
| **Windows**                | ❌ No      | Not supported; lacks a unified `syscall()` ABI |


## 🧭 Roadmap

ShellKit is stable and usable, but we plan to explore some exciting features in future releases:

- 🔌 **Plugin System**: Allow users to register custom builtin commands, aliases, and functions
- 🧠 **Deep Thinking Mode**: Experimental tracing into native syscalls (e.g. eBPF or low-level syscall capture)
- 🧳 **Persistent Profiles**: Save environment variables, shell history, and custom setups
- 🧪 **More Built-ins**: Extend shell with commands like `ls`, `cat`, `grep`
- 💡 **Multiline Script Execution**: Support running multi-line commands or script blocks in one go

If you're interested in any of these — or have other ideas in mind — feel free to [open a discussion](https://github.com/pokeyaro/shellkit/discussions) or [submit a pull request](https://github.com/pokeyaro/shellkit/pulls). \
We welcome all contributors — from feature suggestions to actual code!

> 💬 Turn your interest into contribution — ShellKit grows better with community voices.


## 📌 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.


## 📜 License

MIT License. See [LICENSE](./LICENSE) for details.


## 🤝 Acknowledgments

Inspired by the spirit of classic Unix shells. \
Thanks to all system programmers and terminal geeks who paved the way.
