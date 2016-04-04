#!/usr/bin/env python

from setuptools import setup, Extension, find_packages

_packages = find_packages(where=".", exclude=[])

setup(
    name='lz4r',
    version='1.0',
    author="root",
    long_description=open('README.md', 'r').read(),
    packages=_packages,
    scripts=['lz4test'],
    ext_modules=[
        Extension('lz4f', [
            'src/lz4.c',
            'src/lz4hc.c',
            'src/lz4frame.c',
            'src/python-lz4f.c',
            'src/xxhash.c'
        ], extra_compile_args=[
            "-std=c99",
            "-O3",
            "-Wall",
            "-W",
            "-Wundef",
            "-DVERSION=\"1.0\"" ,
            "-DLZ4_VERSION=\"r124\"",
        ])],
    setup_requires=["nose>=1.0"],
)
