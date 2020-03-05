import math as m
p=int(input("enter a prime integer p "))
q=int(input("enter a prime integer q "))
num=int(input("enter a number to encrypt "))
n=p*q
z=(p-1)*(q-1)
for e in range(2,z):
	if m.gcd(e,z)==1:
		break
for i in range(1,10):
	x=1+i*z
	
	if x%e==0:
		d=int(x/e)
		break
alpha=pow(num,e)
ctt=alpha % n

beta=pow(ctt,d)
ptt=beta % n


print("PUBLIC-KEY({},{}) PRIVATE-KEY({},{})".format(n,e,n,d))
print("cipher \n{}".format(ctt))
print("plaintext \n{}".format(ptt))

