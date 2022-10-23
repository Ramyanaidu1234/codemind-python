n=input()
k=0
for i in n:
    k=n.count(i)
    if k>1:
        print("Not Unique Number")
        break
else:
    print("Unique Number")