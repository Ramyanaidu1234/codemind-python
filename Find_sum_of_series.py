n=int(input())
i=1
s=0
for i in range(1,n+1):
    s=s+1/i
print('{:.2f}'.format(s))