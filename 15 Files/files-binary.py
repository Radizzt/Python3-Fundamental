#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    buffersize = 50000;
    fin = open('olives.jpg', "rb") #read mode by default "R,W,A(append) mode. b = binary mode
    fout = open("new.jpg", "wb");
    buffer = fin.read(buffersize);
    while len(buffer):
        fout.write(buffer);
        print(".", end="");
        buffer = fin.read(buffersize);
    
    print("done");

if __name__ == "__main__": main()
