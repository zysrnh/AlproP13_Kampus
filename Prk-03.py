xR=['k','a','l','e','n','d','e','r']
N=len(xR)
for i in range(N):
    if i%2!=0:  
        xR[i]='0'
for i in range(N):
    print(xR[i],end=' ')