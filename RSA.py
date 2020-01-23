import sympy as ss
import math
    
print("RSA ALGO IMPLEMENTATION--PY--OVERRKILL ")

def rsa(p,q):
    #check
    if ss.isprime(p) and ss.isprime(q) and p!=q:
        pass
    else:
        print("fatal error")
        return 0
    n=p*q
    t=(p-1)*(q-1)
    print("choose e such that greater than 1 less than ",p-1," & ",q-1)
    e=int(input())
    while(math.gcd(t,e)!=1 and e>=p and e>=q):
        e=int(input("enter a correct value that meets condition"))
    print("YOUR PUBLIC KEY IS : ",n,",",e)
    print("YOUR PRIVATE KEY IS : ",1/e," mod ",t ," OR ",(1/e)%t)
#CIPHER 
    print(88*(e%n))
#PLAIN
    u=88*(e%n)
    print(u*((1/e)%t))
rsa(11,17)
