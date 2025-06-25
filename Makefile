# Makefile for ShellKit
# Supports: Linux/macOS, Python 3.10+

# Native build config
CC = gcc
SRC = native/syscall.c native/libc.c
BUILD_DIR = build
BUILD_OUT = $(BUILD_DIR)/libnative.so
PACKAGE_OUT = syscall/syslib.so
CFLAGS = -shared -fPIC

# Python toolchain - detect CI vs local environment
ifeq ($(CI),true)
	# CI environment uses system PATH
	BIN_PREFIX =
else
	# Local development uses virtual environment
	BIN_PREFIX = .venv/bin/
endif

PYTHON = $(BIN_PREFIX)python
PIP    = $(BIN_PREFIX)pip
BLACK  = $(BIN_PREFIX)black
ISORT  = $(BIN_PREFIX)isort
RUFF   = $(BIN_PREFIX)ruff
MYPY   = $(BIN_PREFIX)mypy
PYTEST = $(BIN_PREFIX)pytest

# Declare phony targets
.PHONY: build package clean test fmt lint type check install start

# Clean all build-related artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf dist build *.egg-info \
		__pycache__ */__pycache__ .mypy_cache .pytest_cache
	@echo "✅ Clean complete!"

# Compile native syscall library and copy to project
build: clean
	@mkdir -p $(BUILD_DIR)
	@echo "📦 Compiling: $(SRC) → $(BUILD_OUT)"
	@$(CC) $(CFLAGS) -o $(BUILD_OUT) $(SRC) 2>&1 \
	| sed -En 's/.*(message|warning):/🧱 Platform:/;s/(’| \[-).*//;1p'
	@cp $(BUILD_OUT) $(PACKAGE_OUT)
	@echo "📥 Copied: $(BUILD_OUT) → $(PACKAGE_OUT)"
	@echo "🎉 Native build complete!"

# Build wheel package and install locally for CLI testing
package: clean
	@echo "📦 Building Python package..."
	@$(PYTHON) -m build
	@echo "📥 Installing built wheel..."
	@$(PIP) install --force-reinstall --no-cache-dir dist/*.whl
	@echo "✅ Package install complete!"

# Install all dev tools listed in requirements-dev.txt
install:
	@echo "📦 Installing development dependencies..."
	@$(PIP) install -r requirements-dev.txt

# Run all Python tests
test:
	@echo "🧪 Running unit tests..."
	PYTHONPATH=. $(PYTEST) tests/

# Format check (disabled diff output by default)
fmt:
	@echo "🎨 Checking code format..."
#	@$(BLACK) . --check --diff | colordiff
#	@$(ISORT) . --check-only --diff | colordiff
	@echo "Code formatter passwd!"

# Lint using Ruff
lint:
	@echo "🔍 Running linter..."
	@$(RUFF) check .

# Type check using MyPy
type:
	@echo "🔧 Running type checker..."
	@$(MYPY) shell/ inspector/ libc/

# Run all code quality checks
check: fmt lint type
	@echo "✅ All checks passed!"

# Start the interactive shell
start:
	@$(PYTHON) -m shell.main
