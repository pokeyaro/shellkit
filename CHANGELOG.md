# 📦 Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0-beta4] - 2025-06-26

### Fixed
- **Linux**: Fixed exit command hanging and creating zombie processes
- Replaced SYS_exit with SYS_exit_group for proper multi-threaded process termination
- Exit command now works correctly across all supported platforms


## [0.1.0-beta3] - 2025-06-25

### Added
- Python 3.13 support
- Multi-platform wheel building (Linux, macOS Intel/ARM)

### Changed
- Improved CI/CD pipeline with cross-platform testing


## [0.1.0-beta2] - 2025-06-25

### Fixed
- C extension build configuration for proper wheel packaging


## [0.1.0-beta1] - 2025-06-24

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
