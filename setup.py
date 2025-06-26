from setuptools import setup, Extension

setup(
    ext_modules=[
        Extension(
            name="shellkit.syscall.syslib",
            sources=["native/syscall.c", "native/libc.c"],
        )
    ]
)
