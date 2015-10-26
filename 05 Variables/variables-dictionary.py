#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = {'one': 1, "two": 2, "three": 3, "four": 4}
    print(d["one"]);
    print(d);
    #sorted by the keys
    for k in sorted(d.keys()):
        print(k, d[k]);
        
    #alternative way to write a dictionary
    d2 = dict(
              one = 1, two = 2, three = 3, four = 4, five = "five"
              )
    print(d2)
    d2['seven'] = 7;
    for k in sorted(d2.keys()):
        print(k, d2[k]);

if __name__ == "__main__": main()
