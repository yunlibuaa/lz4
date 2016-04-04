#!/usr/bin/env python

import argparse
import os
import sys

try:
    import lz4r
except ImportError:
    import __init__ as lz4r


def compDir(input, output):
    return lz4r.compressDir(input,output)

def decompDir(input):
    return lz4r.decompressDir(input)

def outErr(msg):
    sys.stdout.write(''.join([msg]))
    sys.exit()
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', dest='comp', default=False,
                        help=''.join(['Compress directory to .lz4r.']))
    parser.add_argument('-x', action='store_true', dest='decomp', default=False,
                        help=''.join(['Decompress file ends in .lz4r.']))
    parser.add_argument('output', action='store', nargs='?', default=None, help='Optional output target.')
    parser.add_argument('input', action='store', help='The targeted input.')
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
        
    res = parser.parse_args()
    
    if res.comp:
        if res.decomp:
            outErr('Please specify only one of the comp/decomp options!\n')
        elif not (os.path.isdir(res.input) and os.path.exists(res.input)):
            outErr(res.input + ' is not exists or not a directory!\n')
        elif res.output and os.path.isfile(res.output):
            answer = raw_input(res.output + ' already exists\nOverwrite? Y/N : ')
            if answer and answer.upper() not in ('Y', 'YES'):
                sys.exit()
        compDir(res.input, res.output)
    
    elif res.decomp:
        if not res.input.endswith('lz4r'):
            print(res.input + ' is not a valid file!')
            sys.exit()
        decompDir(res.input)
        
    else:
        parser.print_help()
        
