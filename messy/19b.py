from collections import Counter
f=open("C:\\Users\\kengq\\OneDrive\\Documents\\Programming\\in.txt","r").readlines()
data=[]
scanners=0
for i in range(len(f)):
    if f[i]=="\n":scanners+=1
    elif f[i][1]=='-':data.append([])
    else:
        a,b,c=map(int,f[i].split(','))
        data[scanners].append((a,b,c))
if f[-1]!="\n":scanners+=1
rotations=[(1,2,3),(1,-2,-3),(1,3,-2),(1,-3,2),\
           (-1,2,-3),(-1,-2,3),(-1,3,2),(-1,-3,-2),\
           (2,1,-3),(2,-1,3),(2,3,1),(2,-3,-1),\
           (-2,1,3),(-2,-1,-3),(-2,3,-1),(-2,-3,1),\
           (3,1,2),(3,-1,-2),(3,2,-1),(3,-2,1),\
           (-3,1,-2),(-3,-1,2),(-3,2,1),(-3,-2,-1)]
def rotate(coords,t):
    result=[0,0,0]
    r=rotations[t]
    for i in range(3):
        result[i]=coords[abs(r[i])-1]
        if r[i]<0:result[i]*=-1
    return (result[0],result[1],result[2])
locations=[[0,0,0] for i in range(scanners)]
orients=[-1]*scanners
newData=[0]*scanners
orients[0]=0
newData[0]=[rotate(x,0) for x in data[0]]
beacons=set()
for x in data[0]:
    beacons.add((x[0],x[1],x[2]))
def compare(A,B):
    for t in range(24):
        diffs=Counter()
        temp=[rotate(x,t) for x in data[B]]
        for i in range(len(newData[A])):
            for j in range(len(data[B])):
                diff=tuple(temp[j][k]-newData[A][i][k] for k in range(3))
                diffs[diff]+=1
        most=diffs.most_common(1)[0]
        if most[1]>=12:
            orients[B]=t
            translate=most[0]
            temp2=[tuple(x[k]-translate[k] for k in range(3)) for x in temp]
            newData[B]=[]
            for x in temp2:
                newData[B].append(x)
                beacons.add(x)
            locations[B]=[-translate[k] for k in range(3)]
            break
def DFS(v):
    for i in range(scanners):
        if orients[i]==-1:
            compare(v,i)
            if orients[i]!=-1:
                DFS(i)
DFS(0)
print(len(beacons))
largest=0
for i in range(scanners):
    for j in range(i+1,scanners):
        d=sum([abs(locations[j][k]-locations[i][k]) for k in range(3)])
        if d>largest:largest=d
print(largest)
