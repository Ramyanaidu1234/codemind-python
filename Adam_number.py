n=int(input())
s=n*n
o=0
p=0
while n>0:
    r=n%10
    o=o*10+r
    n=n//10
m=o*o
while m>0:
    q=m%10
    p=p*10+q
    m=m//10
if p==s:
    print("True")
else:
    print("False")