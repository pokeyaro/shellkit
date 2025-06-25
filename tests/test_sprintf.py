from libc.printf import sprintf


def test_sprintf_basic():
    """
    Basic usage test, including:
    - %s, %d substitution
    - %% escaping
    - Argument count alignment
    """
    cases = [
        ("hello %s", ("world",), "hello world"),
        ("age: %d", (18,), "age: 18"),
        ("percent %% done", (), "percent % done"),
        ("name: %s, age: %d%%", ("Alice", 30), "name: Alice, age: 30%"),
        ("empty", (), "empty"),
        ("%v not supported", (255,), "%v not supported"),  # fallback: no spec
    ]

    for i, (fmt, args, expected) in enumerate(cases, 1):
        result = sprintf(fmt, *args)
        assert result == expected, f"[Case {i}] Expected '{expected}', got '{result}'"
        print(f"[✓] Basic Case {i} passed: {result!r}")


def test_sprintf_precision():
    """
    Precision test: %.Nf floating-point formatting
    """
    cases = [
        ("pi: %.2f", (3.14159,), "pi: 3.14"),
        ("rounded: %.0f", (3.99,), "rounded: 4"),
        ("exact: %.6f", (3.1,), "exact: 3.100000"),
        ("default: %f", (3.1,), "default: 3.100000"),
    ]

    for i, (fmt, args, expected) in enumerate(cases, 1):
        result = sprintf(fmt, *args)
        assert result == expected, f"[Precision {i}] Expected '{expected}', got '{result}'"
        print(f"[✓] Precision Case {i} passed: {result!r}")


def test_sprintf_prefix():
    """
    Prefix test: %#x, %#o, %#b
    """
    cases = [
        ("hex: %#x", (255,), "hex: 0xff"),
        ("HEX: %#X", (255,), "HEX: 0XFF"),
        ("oct: %#o", (8,), "oct: 0o10"),
        ("bin: %#b", (5,), "bin: 0b101"),
        ("raw: %x", (255,), "raw: ff"),
    ]

    for i, (fmt, args, expected) in enumerate(cases, 1):
        result = sprintf(fmt, *args)
        assert result == expected, f"[Prefix {i}] Expected '{expected}', got '{result}'"
        print(f"[✓] Prefix Case {i} passed: {result!r}")


def test_sprintf_fallback():
    """
    Fallback test: invalid format specifiers are preserved
    """
    cases = [
        ("%q", (123,), "%q"),            # Unsupported format specifier
        ("%#s", ("abc",), "%#s"),        # # flag not supported for %s
        ("%05d", (42,), "%05d"),         # Width/zero padding not supported
        ("%#.2f", (3.14,), "%#.2f"),     # # flag + float not supported
    ]

    for i, (fmt, args, expected) in enumerate(cases, 1):
        result = sprintf(fmt, *args)
        assert result == expected, f"[Fallback {i}] Expected '{expected}', got '{result}'"
        print(f"[✓] Fallback Case {i} passed: {result!r}")


if __name__ == "__main__":
    test_sprintf_basic()
    test_sprintf_precision()
    test_sprintf_prefix()
    test_sprintf_fallback()
    print("\n🎉 All sprintf test cases passed.")
