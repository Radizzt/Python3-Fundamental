#!/usr/bin/python3

a, b = 0, 1 #assign a with 0 b with 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b)) #replace each {} with the format
else:
    print('a ({}) is not less than b ({})'.format(a, b))

#print(a < b ? "foo" : "bar");
print("foo" if a < b else "bar");