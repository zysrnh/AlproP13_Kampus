bT=['s','e','m','a','p','u','t'];
N=len(bT);
nm=(N-1)/2;
nm=int(nm);
for i in range(nm):
    temp=bT[i];
    bT[i]=bT[N-1-i];
    bT[N-1-i]=temp;
for i in range(N):
    print(bT[i],end=' ')