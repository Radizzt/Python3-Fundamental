#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)
    
    def __del__(self):
        print("removing object");
    
    #@property turns it to an accessor for color variable
    @property
    def color(self):
        return self.properties.get("color", None);

    @color.setter
    def color(self, c):
        print("setting colours");
        self.properties["color"] = c;
        
    @color.deleter
    def color(self):
        print("deleting colour");
        del self.properties['color'];
        
def main():
    donald = Duck();
    test = Duck();
    donald.color ="blue"
    del test;
    print(donald.color);
    del donald;


if __name__ == "__main__": main()
