#!/usr/bin/python3

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

#generator function
def primes(n = 1):
   while(True):
       #yield is like return but halts the function until it's call again and
       #continue on in the next line instead of restarting
       if isprime(n): yield n 
       n += 1 

for n in primes():
    if n > 100: break
    print(n)

