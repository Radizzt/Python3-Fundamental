#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        #replace lenmore or nevermore with ###
        print(re.sub('(Len|Neverm)ore',"###", line), end='');
        
    fh.seek(0);
    for line in fh:
        match = re.search("(Len|Neverm)ore", line);
        if match:
            print(type(match));
            print(line.replace(match.group(), "###"), end='');

if __name__ == "__main__": main()
