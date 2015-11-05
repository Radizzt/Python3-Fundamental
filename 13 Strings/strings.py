#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


#Documentation at http://docs.python.org/py3k/library/stdtypes.html
def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print("    this is a string      ".rstrip());#remove space/newline at teh end only
    print(s.isalnum());#check if only alphanumeric string
    print(s.isalpha())#Check if only alphabit 
    print(s.isdigit())#check if it's only digit
    print(s.isprintable())#check if string is printable.

if __name__ == "__main__": main()
