#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

#for more Module: http://docs.python.org/py3k/library/index.html
#for third party module: http://pypi.python.org/pypi

import sys

def main():
    print('Python version {}.{}.{}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    import os;
    print(os.name);
    print(os.getenv("PATH"));
    print(os.getcwd());
    print(os.urandom(24));
    
#     import urllib.request;
#     page = urllib.request.urlopen("http://bw.org/")
#     c = 0;
#     for line in page:
#         c+=1;
#         print(str(line, encoding = "utf_8"), end = "{}".format(c));
        
    import random;#random generator
    print(random.randint(1,1000));
    l = list(range(25));
    print(l);
    random.shuffle(l)
    print(l);
    
    import datetime;#date
    now = datetime.datetime.now();
    print(now);
    print(now.year, now.month, now.day, now.hour)
    
if __name__ == "__main__": main()
