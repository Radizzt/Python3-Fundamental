#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        fh = open('lixnes.txt')
    except IOError as e:
        print("could not open file, bleh", e);
    #run's if no exceptions
    else:
        for line in fh: print(line.strip());#strip end line
    

if __name__ == "__main__": main()
