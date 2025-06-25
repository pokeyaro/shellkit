import time


COUNT = 10_000
FRAGMENT = "hello"


def concat_plus_equal():
    s = ""
    for _ in range(COUNT):
        s += FRAGMENT
    return s


def concat_join():
    parts = []
    for _ in range(COUNT):
        parts.append(FRAGMENT)
    return "".join(parts)


def bench(name, func):
    print(f"🧪 Benchmark: {name}")
    start = time.perf_counter()
    result = func()
    duration = time.perf_counter() - start
    print(f"⏱ Duration: {duration:.6f} sec")
    print(f"📏 Length: {len(result)} chars\n")


if __name__ == "__main__":
    bench("String += Concatenation", concat_plus_equal)
    bench("List append + ''.join()", concat_join)
