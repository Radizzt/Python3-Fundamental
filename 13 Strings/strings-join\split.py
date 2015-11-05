#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    s2= "this,is,a,string";
    print(s.split());
    print(s2.split(","));
    
    words = s.split();
    for w in words:
        print(w);
        
    new = "*".join(words);
    print(new);
    print("^".join(words));
    

if __name__ == "__main__": main()
