from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            "shellkit.syscall.syslib",
            sources=["native/syscall.c", "native/libc.c"],
        )
    ]
)
