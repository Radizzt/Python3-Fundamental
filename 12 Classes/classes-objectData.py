#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    #constructor accepting keyword arguments
    def __init__(self, **kwargs):
        self._instances= kwargs;
        
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
        
    def set_instance(self,k,v):
        self._instances[k] = v;
        
    def get_instance(self, k):
        return self._instances.get(k, None);

def main():
    donald = Duck();
    goofy = Duck(colour ="red", feet="4");
#     donald.set_clr("blue");
#     print(donald.get_clr());
#     donald._clr="pink";
    donald.set_instance("feet", "2");
    donald.set_instance("colour", "pink");
    print(donald.get_instance("feet"));
    print(donald.get_instance("colour"));
    print(goofy.get_instance("feet"));
    print(goofy.get_instance("colour"));
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
