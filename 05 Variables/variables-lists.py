#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    tuple1 = (1,2,3); #tuples object, immutable
    list1 = [1,2,3]; #list object, mutable
    str = "String"; #is like a list/array can use index on them
    print(type(tuple1), tuple1);
    print(type(list1), list1);
    list1.append(5);
    list1.insert(2, 7);
    print(type(list1), list1);
    print(type(str), str[2:4]);
    
    for i in tuple1:
        print(i);
    
if __name__ == "__main__": main()
