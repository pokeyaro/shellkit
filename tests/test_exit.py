import pytest
from shellkit.libc import print, atexit, exit, _exit


def cleanup1():
    print("hook: cleanup1", buffered=True)


def cleanup2():
    print("hook: cleanup2", buffered=True)


@pytest.mark.skip(reason="incompatible with pytest runner (calls exit)")
def test_normal_exit():
    print("=== test_normal_exit ===")
    atexit(cleanup1)
    atexit(cleanup2)
    print("before exit()", buffered=True)
    exit(42)  # run hooks + exit normally


@pytest.mark.skip(reason="incompatible with pytest runner (calls _exit)")
def test_force_exit():
    print("=== test_force_exit ===")
    atexit(cleanup1)
    atexit(cleanup2)
    print("before _exit()", buffered=True)
    _exit(99)  # skip hooks, exit directly via syscall


@pytest.mark.skip(reason="incompatible with pytest runner (calls exit)")
def test_exit_with_message():
    def goodbye():
        print("bye from hook", buffered=True)

    atexit(goodbye)
    print("about to exit", buffered=True)
    exit(0)


if __name__ == "__main__":
    # test_normal_exit()
    # test_force_exit()
    test_exit_with_message()
