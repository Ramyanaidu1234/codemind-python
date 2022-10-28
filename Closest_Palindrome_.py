def pal(n):
    t=n
    q=0
    while t:
        r=t%10
        q=q*10+r
        t=t//10
    if q==n:
        return True
    else:
        return False
n=int(input())
a=n+1
while True:
    if pal(a):
        break
    else:
        a=a+1
b=n-1
while True:
    if pal(b):
        break
    else:
        b=b-1
if abs(n-b)==abs(n-a):
    print(b,a)
elif abs(n-a)>abs(n-b):
    print(b)
else:
    print(a)