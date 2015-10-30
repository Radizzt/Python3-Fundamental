#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readFile("lisnes.txtd"):
            print(line.strip());
    except IOError as e:
        print("cannot read file. ", e);
    except ValueError as e:
        print("bad filename.", e);

def readFile(fileName):
    if fileName.endswith(".txt"):
        fh = open(fileName);
        return fh.readlines();
    else:
        #raise your own Error exception 
        raise ValueError("must end with .txt or a text file.");

if __name__ == "__main__": main()
