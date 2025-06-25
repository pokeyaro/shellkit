# 📦 Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2025-06-24

### ✨ Added

- Initial release of **ShellKit**, with two main submodules:
  - `libc`: A Python-based simulation of core C standard library functions, including `printf`, `write`, and `exit`.
  - `pysh`: A REPL-based interactive shell built on top of `libc`.
- Implemented essential built-in commands: `cd`, `echo`, `pwd`, `export`, `env`, `clear`, etc.
- Multilingual manual support: Chinese, English, Japanese, Korean.
- Advanced startup flags:
  - `--debug`, `--safe`, `--trace-echo`, `--thinking`.
- Customizable prompt styles with ANSI color and path format support.
- Cross-platform native syscall bridge (`syslib.so`) for:
  - macOS/Linux
  - x86_64 and ARM64 architectures.
- Robust `Makefile` workflow:
  - `make test`, `make check`, `make build`.
- Integrated unit test framework (`pytest`) and benchmark scripts.
- Preliminary GitHub Actions CI setup for linting, formatting, typing, and testing.

---
