s=int(input())
n=0
for i in range(1,s):
    if s%i==0:
        n+=i
if n>s:
    print("True")
else:
    print("False")