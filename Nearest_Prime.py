t=int(input())
for i in range(t):
    n=int(input())
    np=n
    pp=n
    while True:
        f=0
        for i in range(1,np+1):
            if np%i==0:
                f+=1
        if f==2:
            break
        np+=1
    while True:
        f=0
        for i in range(1,pp+1):
            if pp%i==0:
                f+=1
        if f==2:
            break
        pp-=1
    if n-pp<=np-n:
        print(pp)
    else:
        print(np)
