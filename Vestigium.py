import numpy as np
t=int(input())
for i in range(1,t+1):
    if i==1:
        a=np.array([[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]])
        r=0
        q=0
    if i==2:
        a=np.array([[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]])
        r=4
        q=4
    if i==3:
        a=np.array([[1,2,3],[1,3,2],[1,2,3]])
        r=0
        q=2
    m=np.trace(a)
    print("Case #{}: {} {} {}\n".format(i,m,r,q))