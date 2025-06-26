"""
libc module: user-space syscall wrappers for output and process termination.

Includes the following submodules:
- write: low-level write and flush
- printf: formatted output
- exit: graceful and immediate termination
"""

# write
from .write import (
    STDIN, STDOUT, STDERR,
    write, flush,
    write_bytes, write_cstr,
)

# printf
from .printf import (
    sprintf, format,
    printf, println,
    bprintf, bprintln,
    eprintf, eprintln,
    print, fmt_println, Println,
)

# exit
from .exit import (
    _exit,
    exit, atexit,
    graceful_exit,
)


__all__ = [
    # write
    "STDIN", "STDOUT", "STDERR",
    "write", "flush",
    "write_bytes", "write_cstr",

    # printf
    "sprintf", "format",
    "printf", "println",
    "bprintf", "bprintln",
    "eprintf", "eprintln",
    "print", "fmt_println", "Println",

    # exit
    "_exit",
    "exit", "atexit",
    "graceful_exit",
]
