k=int(100)
for i in range(1,7):
    for j in range(1,7):
        if(j<=i):
            print(k,end=' ')
            k-=5
        else:
            print(' ',end=' ')
    print()
