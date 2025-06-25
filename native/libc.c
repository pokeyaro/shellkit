/*
 * libc.c
 *
 * Minimal libc-style utility functions for platform-native environments.
 * - Provides FFI-exposed strlen implementation.
 * - Marked with `__attribute__((visibility("default")))` for cross-boundary calls.
 */

#include <stddef.h>

// ------------------------------------------------------------
// Exported API: strlen (null-terminated C string length)
// ------------------------------------------------------------

__attribute__((visibility("default")))
size_t strlen(const char *s) {
    size_t len = 0;
    while (s[len] != '\0') {
        len++;
    }
    return len;
}
