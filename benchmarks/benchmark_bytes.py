import timeit
from shellkit.libc import flush, write, write_bytes


s = "hello" * 100


def v1():
    a = write(1, s, buffered=True)
    b = write_bytes(1, b"\x0a", buffered=True)
    flush(1)
    return a + b


def v2():
    return write(1, s + "\n")


if __name__ == "__main__":
    print(timeit.timeit(v1, number=10000))
    print(timeit.timeit(v2, number=10000))
