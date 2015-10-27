#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):#match the line with Lenore or Nevermore
            print(line, end='')

    fh.seek(0);#re read the file from the beginning
    for line in fh:
        match = re.search('(Len|Neverm)ore', line);
        if match:
            print(match.group());
if __name__ == "__main__": main()
