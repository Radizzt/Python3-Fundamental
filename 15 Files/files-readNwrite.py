#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
#     fin = open('line.txt', "r"); #read mode by default "R,W,A(append) mode"
#     fout = open("new.txt", "w");
#     for line in fin:
#         print(line, file = fout, end = '')
#     
#     print("done");
    
    buffersize = 50000; #smaller it is the more it will go in the while loop
    fin = open('bigfile.txt', "r"); #read mode by default "R,W,A(append) mode"
    fout = open("new.txt", "w");
    buffer = fin.read(buffersize)#read up to a certain kb
    while len(buffer):
        fout.write(buffer)#write whatever is in the buffer
        print('.', end="");
        buffer = fin.read(buffersize);#read the next buffersize
    
    print("done2");

if __name__ == "__main__": main()
