#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
<<<<<<< HEAD
#     a, b = 1, 1;
#     if a < b:
#         print("a is less than b");
#     elif a > b:
#         print("a is greater than b");
#     else:
#         print ("a is equal b");

# Ternary Operator <condition> ? <true> : <false>
    a , b = 0,1;
    s = "a " + "less than" if a < b else "not less than";
    print(s);
=======
    print("This is the syntax.py file.")
>>>>>>> 83390c1eb586157f13ec6ce80cfb9aa18c54a5b9

if __name__ == "__main__": main(); #let you call function after their call
