aX=[12,-91,-2,15,0.5,-3,-21,7,10,-10]
N=len(aX)
for i in range(N):
    for j in range(N-1):
        if aX[j]>aX[j+1]:
            temp=aX[j]
            aX[j]=aX[j+1]
            aX[j+1]=temp
for i in range(N):
    print(aX[i],end=' ')