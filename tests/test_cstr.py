import ctypes
from libc.write import write_cstr


def test_write_cstr():
    c_str = ctypes.c_char_p(b"hello\0 world")
    length = write_cstr(1, c_str)
    assert length == 5
    print("\n✅ test passed")


if __name__ == "__main__":
    test_write_cstr()
