#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    b(8);
    x, y = 0x55, 0xaa;
    b(x);
    b(y);
    #c++ way of flipping binaries from compary 
    b(x | y);#x or y
    b(x & y);#x and y
    b(x ^ y);
    b(x ^ 0);
    b(x ^ 0xff);
    b(x << 4);#shift left 4 bits
    b(x >> 4);#shift left 4 bits
    b(~x);#one's compliment operator.
    
    
#print number by binaries
def b(n):
        print("{:08b}".format(n));#'{:08n}' print out a binary value to 8 places

if __name__ == "__main__": main();