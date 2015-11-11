#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    tup = tuple(range(25));
    print(tup);
    print(10 in tup);
    print(tup.index(3));
    print(tup.count(5));

    for i in tup:
        print(i);
        if(i == 5):
            break;
    
    l = list(range(25));
    print(l);
    l.append(100);
    print(l);
    l.extend(range(10));
    print(l);
    l.insert(0, 1111); #insert(index, object)
    print(l);
    l.remove(12);#remove value 12.
    del l[1]; #remove index 1
    print(l);
    print(l.pop());
    
    
if __name__ == "__main__": main()
