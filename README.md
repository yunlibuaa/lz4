Overview
--------

  1. lz4f - C-Module containing python bindings for all lz4frame functions.
  2. lz4lib - a file wrapper for lz4r compressed files. 

##Usage

usage: lz4test [-h] [-c] [-x] [output] input

positional arguments:
  output      Optional output target.
  input       The targeted input.

optional arguments:
  -h, --help  show this help message and exit
  -c          Compress directory to .lz4r.
  -x          Decompress file ends in .lz4r.


Compress:

	lz4test -c dir_name.lz4r dir_name

Decompress:

	lz4test -x dir_name.lz4r
