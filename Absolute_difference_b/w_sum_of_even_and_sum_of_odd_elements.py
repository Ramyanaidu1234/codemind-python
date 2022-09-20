n=int(input())
a=list(map(int,input().split(" ")))
se=0
for i in range(n):
    if a[i]%2==0:
        se+=a[i]
so=0
for i in range(n):
    if a[i]%2==1:
        so+=a[i]
print(abs(se-so))