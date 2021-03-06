#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#for more Module: http://docs.python.org/py3k/library/index.html
#for third party module: http://pypi.python.org/pypi

import bitstring

def main():
    a = bitstring.BitString(bin = "01010101");
    print(a.hex, a.bin, a.uint);

    
if __name__ == "__main__": main()
