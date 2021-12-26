import heapq
f=open("C:\\Users\\kengq\\OneDrive\\Documents\\Programming\\in.txt","r").readlines()
n=len(f)
orders=[]
sweepX=[]
for i in range(n):
    order,line=f[i].split()
    if order=="on":o=1
    else:o=0
    X,Y,Z=line.split(",")
    xs,xe=map(int,X[2:].split(".."))
    ys,ye=map(int,Y[2:].split(".."))
    zs,ze=map(int,Z[2:].split(".."))
    orders.append([o,xs,xe,ys,ye,zs,ze])
    sweepX.append([xs,1,i])
    sweepX.append([xe+1,2,i])
sweepX.sort()
activeX=[0]*n
answer=0
for i in range(len(sweepX)-1):
    if sweepX[i][1]==1:activeX[sweepX[i][2]]=1
    else:activeX[sweepX[i][2]]=0
    sweepY=[]
    for j in range(n):
        if activeX[j]:
            order=orders[j]
            sweepY.append([order[3],1,j])
            sweepY.append([order[4]+1,2,j])
    sweepY.sort()
    activeY=[0]*n
    answerX=0
    for j in range(len(sweepY)-1):
        if sweepY[j][1]==1:activeY[sweepY[j][2]]=1
        else:activeY[sweepY[j][2]]=0
        sweepZ=[]
        for k in range(n):
            if activeY[k]:
                order=orders[k]
                sweepZ.append([order[5],1,k])
                sweepZ.append([order[6]+1,2,k])
        sweepZ.sort()
        activeZ=[0]*n
        answerY=0
        actives=[]
        for k in range(len(sweepZ)-1):
            if sweepZ[k][1]==1:
                order=sweepZ[k][2]
                activeZ[order]=1
                heapq.heappush(actives,[-order,orders[order][0]])
            else:
                activeZ[sweepZ[k][2]]=0
            while actives and not activeZ[-actives[0][0]]:
                heapq.heappop(actives)
            answerZ=0
            if actives and actives[0][1]:answerZ=1
            answerY+=(sweepZ[k+1][0]-sweepZ[k][0])*answerZ
        answerX+=(sweepY[j+1][0]-sweepY[j][0])*answerY
    answer+=(sweepX[i+1][0]-sweepX[i][0])*answerX
print(answer)
