#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict(
        one = "first",
        two = "two",
        three = "third"
     )

    v='wee'
    print(choices.get(v,"other")); #looks for the key, if not available display 'other'
if __name__ == "__main__": main()
