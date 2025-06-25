"""
inspector module: runtime tracing and diagnostic tooling for shell and libc layers.

Includes the following submodules:
- debug: traces shell-level execution flow (parsing, dispatch, builtin execution) for CLI debugging
- trace: visualizes libc-level function calls (e.g. echo/printf → print → write) as call trees
- probe: reserved for future cross-layer tracing (libc ↔ native ↔ syscall), not yet implemented

Design Notes:
- This module is not meant for direct use; it supports internal CLI options like --debug and --trace-echo.
- The `trace` submodule performs invasive instrumentation via decorators placed on selected libc functions.
  While inelegant, this approach is simple and effective for now.
- A cleaner, non-invasive alternative (e.g. monkey patching 🐒) would allow fully decoupling `inspector` from libc.
  However, such refactoring is more complex and currently deferred.
"""
