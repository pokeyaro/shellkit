# 📦 Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.2.0-beta3] - 2025-06-27

### Changed
- `help.py` updated: added `su` entry to built-in commands list in all supported languages (EN, JA, KO, ZH)

### Notes
- This is a documentation-only update. No functional changes were made to the shell runtime.


## [0.2.0-beta2] - 2025-06-27

### Features
- Added the `su` command with dynamic user switching support (Linux/macOS compatible).
- Automatically detects platform and uses `su -s <pysh>` on Linux or `sudo <pysh>` on macOS.
- Added localized `su.md` manuals in English, Chinese, Japanese, and Korean.
- Introduced new i18n keys for all related prompts and error messages.

### Documentation
- Unified and improved the usage description in both Chinese and Japanese versions of the `su.md` manual for clarity and consistency.


## [0.2.0-beta1] - 2025-06-27

### Features
- Introduced detailed roadmap and contribution call in `README.md`

### Project Structure
- Added `.github/ISSUE_TEMPLATE`:
  - `bug_report.yml` – Standardized bug report form
  - `feature_request.yml` – Structured feature suggestion template
  - `config.yml` – Issue template configuration

- Added `.github/PULL_REQUEST_TEMPLATE.md` – With checklist and contribution guide link

### Community
- Added `CONTRIBUTING.md` with clear guidelines for new contributors
- Improved phrasing and contributor-facing copy across templates
- Enabled GitHub Discussions and created default categories (Announcements, Bug Reports, Ideas, Help, Show & Tell)


## [0.1.0] - 2025-06-26

### Features
- Initial release to PyPI!
- Custom `printf` / `println` / `sprintf` utilities (via libc module)
- i18n support: English, Chinese, Japanese, Korean (`.json` dictionaries)
- Structured `libc`, `shell`, `syscall`, `inspector` modules
- Tracing and debugging decorators for development
- Custom shell runtime with command dispatch support


## [0.1.0-beta10] - 2025-06-26

### Added
- Format argument check in printf: Basic sanity check added to ensure that the number of arguments matches the number of format specifiers. Prevents silent failures.
- Internationalized error message: New i18n key shell.engine.builtin.printf.too_few_arguments for handling format argument mismatch.
- Internal _formatted_str() helper: Safely formats strings without writing to file descriptor. Supports strict mode for argument count validation.

### Changed
- Safe argument unpacking: _formatted_str() and _formatted_write() now safely handle missing or None arguments via args or ().
- Debug fallback mechanism: In case eprintln() itself fails (e.g. during format failure), it gracefully falls back to using native print() to prevent infinite loops in tracing.

### Stability
- This release strengthens robustness in the printf family, especially around argument mismatches.
- Also improves internal tooling reliability under error conditions.


## [0.1.0-beta9] - 2025-06-26

### Fixed
- metadata: Fixed a bug where syslib.so build time was not correctly resolved from installed path


## [0.1.0-beta8] - 2025-06-26

### Changed
- Refactored runtime/metadata.py: split get_metadata() into get_project_info() and get_syslib_build_time() for clarity

### Fixed
- Fixed incorrect detection of syslib*.so build time when installed via pip


## [0.1.0-beta7] - 2025-06-26

### Fixed
- sleep command: Fixed countdown display leaving residual characters on completion
- help system: Updated glow installation hints to avoid package manager compatibility issues
- Improved terminal output clearing in countdown functionality

### Changed
- Installation guidance: Now recommends GitHub releases over package managers for glow
- Updated installation hints across all supported languages (EN, JA, KO, ZH)
- Simplified installation instructions to use most reliable method

### Build System
- Breaking: Upgraded cibuildwheel from v2.19.2 to v3.0 for modern Python support
- Added Python 3.13 support across all platforms (macOS, Linux)
- Added Linux ARM64 (aarch64) architecture support for better Raspberry Pi and AWS Graviton compatibility
- Simplified build matrix to reduce CI overhead while maintaining platform coverage
- Enhanced cross-platform wheel building with latest toolchain


## [0.1.0-beta6] - 2025-06-26

### Changed
- **Breaking**: Restructured package layout to follow Python standards
- Moved all modules under unified `shellkit` package namespace
- Updated import paths: `from shell import *` → `from shellkit.shell import *`
- Fixed scattered package installation in site-packages

### Fixed
- Resolved package structure causing modules to install as separate top-level packages
- Updated all internal import statements to use new package structure
- Fixed Makefile paths for new directory layout
- Corrected file path resolution in metadata and copyright modules
- Standardized import statement ordering throughout codebase

### Technical
- Package now installs as single `shellkit/` directory instead of scattered modules
- Maintains backward compatibility through proper package structure
- All entry points and CLI commands remain unchanged
- Implemented consistent import ordering: standard library → project modules → relative imports
- Updated build system to target macOS 14.0+ for better compatibility

### Development
- Established import style guide for consistent code organization
- Fixed cross-platform compilation warnings
- Improved package discovery and shared library detection


## [0.1.0-beta5] - 2025-06-26

### Fixed
- **Linux**: Fixed automatic detection of compiled shared library files
- Resolved `syslib.so` vs `syslib.cpython-311-x86_64-linux-gnu.so` filename mismatch


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
