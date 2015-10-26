#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42;
    s = "this is a \n string {}!".format(n);#python 3
    s2 = "this is a \n string %s!" %n;#python 2 version getting obsolete
    #''' or """ allows you to have a string that span several lines
    #'\' in the beginning escape the new line
    s3 = '''\
    this is a string! 
    this is line 2
    this is line 3.
    '''
    print(s);
    print(s2);
    print(s3);

if __name__ == "__main__": main()
