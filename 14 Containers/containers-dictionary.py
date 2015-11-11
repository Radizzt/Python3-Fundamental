#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    dic = {"one":1,"two":2,"three":3};
    dic2 = dict(one = 2, two =2, three=3);
    
    print(dic);
    print(dic2);
    
    dic3 = dict(four=4,five=5,six=6, **dic2);
    print(dic3);
    
    for k in dic3:
        print(k);
    
    for k, v in dic3.items():
        print(k, v);
        
    print(dic.get("eight", "not found"));
    del dic3["six"];
    print(dic3.pop("one"), dic3);

if __name__ == "__main__": main()
