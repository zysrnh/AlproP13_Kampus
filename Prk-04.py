aZ=[1,12,-1,-12,3.5];
xR=[0,0,0];
xR[1-1]=aZ[5-1];
xR[2-1]=aZ[2-1];
xR[3-1]=aZ[4-1];
N=len(xR);
for i in range(N):
    print(xR[i],end=' ')