#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fin = open("utf8.txt", "r", encoding="utf_8");#read it as utf8
    fout = open("utf8.html", "w");
    outBytes = bytearray()#mutable list of bytes
    for line in fin:
        for c in line:
            #ord(c)looks at a character and return the unicode of it
            #look at the unicode of each character and see the unicode, if its
            #greater than 127 put it into the bytearray with the format
            if ord(c) > 127:
                outBytes += bytes("#{:04d};".format(ord(c)), encoding="utf_8")
            else:
                outBytes.append(ord(c));
    
    outstr = str(outBytes, encoding="utf_8")
    print(outstr, file = fout);
    print(outstr);
    print("done");

if __name__ == "__main__": main();