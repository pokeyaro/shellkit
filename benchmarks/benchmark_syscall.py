import time
from shellkit.libc import flush, write


COUNT = 10_000
TEST_STRING = "hello"


def test_print():
    for _ in range(COUNT):
        print(TEST_STRING, end="")


def test_print_flush():
    for _ in range(COUNT):
        print(TEST_STRING, end="", flush=True)


def test_write():
    for _ in range(COUNT):
        write(1, TEST_STRING, buffered=False)


def test_bwrite():
    for _ in range(COUNT):
        write(1, TEST_STRING, buffered=True)
    flush(1)


def bench(name, func):
    print(f"🧪 {name}...")
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f"\n⏱ {name}: {end - start:.6f} sec\n")


if __name__ == "__main__":
    bench("Python print", test_print)
    bench("Python print (flush=True)", test_print_flush)
    bench("Native syscall(write)", test_write)
    bench("Buffered syscall (buf_write + flush)", test_bwrite)
