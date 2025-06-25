/*
 * syscall.c
 *
 * Cross-platform syscall wrappers for low-level output and process termination.
 * - Provides direct write / exit syscalls using inline assembly or libc syscall
 * - Supports Linux and macOS on x86_64 and ARM64 architectures
 * - Exported symbols use `__attribute__((visibility("default")))` for FFI binding
 */

#include <unistd.h>
#include <stddef.h>

// ------------------------------------------------------------
// Internal: Platform-specific syscall_write implementation
// ------------------------------------------------------------

static inline ssize_t _internal_syscall_write(int fd, const char *buf, size_t count) {
#if defined(__linux__) && defined(__x86_64__)
#pragma message("Building for Linux x86_64")

    // Linux x86_64: syscall number 1 = write
    ssize_t ret;
    register int         _fd  asm("rdi") = fd;
    register const char *_buf asm("rsi") = buf;
    register size_t      _len asm("rdx") = count;

    asm volatile (
        "mov $1, %%rax\n\t"
        "syscall\n\t"
        : "=a"(ret)
        : "r"(_fd), "r"(_buf), "r"(_len)
        : "rcx", "r11", "memory"
    );

    return ret;

#elif defined(__APPLE__) && defined(__x86_64__)
#pragma message("Building for macOS x86_64 (Intel)")

    // macOS x86_64: syscall number 0x2000004 = write
    ssize_t ret;
    register int         _fd  asm("rdi") = fd;
    register const char *_buf asm("rsi") = buf;
    register size_t      _len asm("rdx") = count;

    asm volatile (
        "mov $0x2000004, %%rax\n\t"
        "syscall\n\t"
        : "=a"(ret)
        : "r"(_fd), "r"(_buf), "r"(_len)
        : "rcx", "r11", "memory"
    );

    return ret;

#elif defined(__APPLE__) && defined(__aarch64__)
#pragma message("Building for macOS on Apple Silicon (ARM64)")

    // macOS ARM64: Direct svc is technically possible but not recommended.
    // Apple prefers using the syscall() wrapper for better compatibility
    // and to avoid potential issues with system integrity protection.
    // SYS_write = 4 (defined in <sys/syscall.h>)
    #include <sys/syscall.h>
    return syscall(SYS_write, fd, buf, count);

#elif defined(__linux__) && defined(__aarch64__)
#pragma message("Building for Linux ARM64")

    // Linux ARM64: syscall number 64 = write
    register long x0 asm("x0") = (long)fd;
    register const char *x1 asm("x1") = buf;
    register size_t x2 asm("x2") = count;
    register long x8 asm("x8") = 64;

    asm volatile (
        "svc #0\n"
        : "+r"(x0)
        : "r"(x1), "r"(x2), "r"(x8)
        : "memory"
    );

    return x0;

#else
#pragma message("Building for unsupported or unknown platform")

    // Unsupported platform: emit error message to STDERR
    #define MSG_LEN(arr) (sizeof(arr) - 1)
    const char msg[] = "syscall_write: unsupported platform\n";
    write(2, msg, MSG_LEN(msg));
    return -1;

#endif
}


// ------------------------------------------------------------
// Internal: Platform-specific syscall_exit implementation
// ------------------------------------------------------------

static inline void _internal_syscall_exit(int code) {
#if defined(__linux__) && defined(__x86_64__)

    // Use exit_group (231) instead of exit (60) for proper process termination
    //
    // Why exit_group vs exit:
    // - exit (60):        Only terminates the calling thread
    // - exit_group (231): Terminates all threads in the process group
    //
    // ☠️ In Python's multi-threaded environment (GC, signal handlers, etc.),
    // using exit (60) leaves other threads running, causing the process
    // to become a zombie. exit_group ensures clean process-wide termination.
    //
    // Register constraints:
    // - rax: syscall number (231 = SYS_exit_group)
    // - rdi: exit code (first argument)
    // - clobbers: rcx, r11 (modified by syscall instruction), memory
    register long rax asm("rax") = 231;  // SYS_exit_group
    register long rdi asm("rdi") = code;

    asm volatile(
        "syscall\n\t"
        :
        : "r"(rax), "r"(rdi)
        : "rcx", "r11", "memory"
    );

    // Tell compiler this function never returns (helps with optimization)
    __builtin_unreachable();

#elif defined(__APPLE__) && defined(__x86_64__)

    __asm__ volatile (
        "movq $0x2000001, %%rax\n\t"
        "movq %0, %%rdi\n\t"
        "syscall\n\t"
        :
        : "r"((long)code)
        : "rax", "rdi", "rcx", "r11", "memory"
    );

#elif defined(__APPLE__) && defined(__aarch64__)

    #include <sys/syscall.h>
    syscall(SYS_exit, code);

#elif defined(__linux__) && defined(__aarch64__)

    register long x0 asm("x0") = code;
    register long x8 asm("x8") = 93;
    asm volatile(
        "svc #0"
        :
        : "r"(x0), "r"(x8)
        : "memory"
    );

#else

    #define MSG_LEN(arr) (sizeof(arr) - 1)
    const char msg[] = "syscall_exit: unsupported platform\n";
    write(2, msg, MSG_LEN(msg));
    return -1;

#endif
}


// ------------------------------------------------------------
// Exported API: syscall_write / syscall_exit
// ------------------------------------------------------------

__attribute__((visibility("default")))
ssize_t syscall_write(int fd, const char *buf, size_t count) {
    return _internal_syscall_write(fd, buf, count);
}

__attribute__((visibility("default")))
void syscall_exit(int code) {
    _internal_syscall_exit(code);
}


// ------------------------------------------------------------
// Buffered I/O (optional): buffered_syscall_write / flush
// ------------------------------------------------------------

#define SYSCALL_BUFSIZE 4096  // 4KB page-aligned buffer

static char syscall_buf[SYSCALL_BUFSIZE];
static size_t syscall_buf_len = 0;

__attribute__((visibility("default")))
void buffered_syscall_flush(int fd) {
    if (syscall_buf_len > 0) {
        _internal_syscall_write(fd, syscall_buf, syscall_buf_len);
        syscall_buf_len = 0;
    }
}

__attribute__((visibility("default")))
ssize_t buffered_syscall_write(int fd, const char *buf, size_t count) {
    ssize_t total_written = 0;

    while (count > 0) {
        size_t space = SYSCALL_BUFSIZE - syscall_buf_len;
        size_t to_copy = count < space ? count : space;

        // Copy data into buffer
        for (size_t i = 0; i < to_copy; ++i) {
            syscall_buf[syscall_buf_len + i] = buf[i];
        }

        syscall_buf_len += to_copy;
        buf += to_copy;
        count -= to_copy;
        total_written += to_copy;

        // Flush if buffer is full
        if (syscall_buf_len == SYSCALL_BUFSIZE) {
            buffered_syscall_flush(fd);
        }
    }

    return total_written;
}
