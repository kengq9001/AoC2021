f=open("input18.txt","r").readlines()
def readPair(pair,string):
    i=1
    leftstart=1
    if string[i]!='[':
        while string[i]!=',':
            i+=1
        leftend=i
        pair[0]=int(string[leftstart:leftend])
    else:
        brackets=0
        while string[i]!=',' or brackets!=0:
            if string[i]=='[':brackets+=1
            if string[i]==']':brackets-=1
            i+=1
        leftend=i
        pair[0]=[-1,-1]
        readPair(pair[0],string[leftstart:leftend])
    i+=1
    rightstart=i
    rightend=len(string)-1
    if string[i]!='[':
        pair[1]=int(string[rightstart:rightend])
    else:
        pair[1]=[-1,-1]
        readPair(pair[1],string[rightstart:rightend])
def findPositions(pair,positions,curr):
    if isinstance(pair,list):
        left=list(curr)
        left.append(0)
        findPositions(pair[0],positions,left)
        right=list(curr)
        right.append(1)
        findPositions(pair[1],positions,right)
    else:
        positions.append(curr)
def locate(pair,dirs):
    curr=pair
    for i in range(len(dirs)):
        curr=curr[dirs[i]]
    return curr
def locateList(pair,dirs):
    curr=pair
    for i in range(len(dirs)-1):
        curr=curr[dirs[i]]
    return curr
def simplify(pair):
    while True:
        explode=0
        split=0
        positions=[]
        findPositions(pair,positions,[])
        for i in range(len(positions)):
            if len(positions[i])>4:
                if i>0:
                    directions=positions[i-1]
                    pred=locateList(pair,directions)
                    pred[directions[-1]]+=locate(pair,positions[i])
                if (i+2)<len(positions):
                    directions=positions[i+2]
                    succ=locateList(pair,directions)
                    succ[directions[-1]]+=locate(pair,positions[i+1])
                curr=locateList(pair,positions[i][:-1])
                curr[positions[i][-2]]=0
                explode=1
                break
        if explode:continue
        for directions in positions:
            n=locate(pair,directions)
            if n>9:
                parent=locateList(pair,directions)
                parent[directions[-1]]=[n//2,(n+1)//2]
                split=1
                break
        if split:continue
        break
def magnitude(pair):
    if isinstance(pair,list):
        return 3*magnitude(pair[0])+2*magnitude(pair[1])
    return pair
best=0
for i in range(len(f)):
    for j in range(len(f)):
        if i==j:continue
        pair1=[-1,-1]
        pair2=[-1,-1]
        readPair(pair1,f[i].rstrip('\n'))
        readPair(pair2,f[j].rstrip('\n'))
        result=[pair1,pair2]
        simplify(result)
        x=magnitude(result)
        if x>best:best=x
print(best)
