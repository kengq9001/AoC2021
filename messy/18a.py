f=open("C:\\Users\\kengq\\OneDrive\\Documents\\Programming\\in.txt","r").readlines()
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
result=[-1,-1]
readPair(result,f[0].rstrip('\n'))
for i in range(1,len(f)):
    Next=[-1,-1]
    readPair(Next,f[i].rstrip('\n'))
    newResult=[result,Next]
    result=newResult
    simplify(result)
def magnitude(pair):
    if isinstance(pair,list):
        return 3*magnitude(pair[0])+2*magnitude(pair[1])
    return pair
print(magnitude(result))
