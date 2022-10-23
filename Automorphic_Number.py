n=int(input())
num=len(str(n))
sqr=n**2
last=sqr%pow(10,num)
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")