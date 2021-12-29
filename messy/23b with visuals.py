import heapq
import time
start_time=time.time()
f=open("input23b.txt","r").readlines()
depth=len(f)-3
class state():
    def readInput(self):
        self.hallway=[-1]*11
        self.rooms=[[0]*depth for i in range(4)]
        for i in range(4):
            for j in range(depth):
                self.rooms[i][j]=ord(f[1+depth-j][2*i+3])-ord('A')
        self.parent=None
    def copy(self):
        new=state()
        new.hallway=[x for x in self.hallway]
        new.rooms=[0]*4
        for i in range(4):
            new.rooms[i]=[x for x in self.rooms[i]]
        return new
    def solved(self):
        result=[0]*4
        for i in range(4):
            for j in range(depth):
                if len(self.rooms[i])>=j+1 and self.rooms[i][j]==i:
                    result[i]+=1
                else:
                    break
        return result
    def flatten(self):
        return (tuple(self.hallway),tuple(self.rooms[0]),tuple(self.rooms[1]),tuple(self.rooms[2]),tuple(self.rooms[3]))
    def printMap(self):
        ref={-1:'.',0:'A',1:'B',2:'C',3:'D'}
        Map=[[0]*13 for i in range(3+depth)]
        Map[0]=['#']*13
        Map[1][0]=Map[1][12]='#'
        for i in range(13):
            if i==3 or i==5 or i==7 or i==9:continue
            Map[2][i]='#'
        for i in range(3,2+depth):
            Map[i][2]=Map[i][4]=Map[i][6]=Map[i][8]=Map[i][10]='#'
            Map[i][0]=Map[i][1]=Map[i][11]=Map[i][12]=' '
        for i in range(2,11):
            Map[2+depth][i]='#'
        Map[2+depth][0]=Map[2+depth][1]=Map[2+depth][11]=Map[2+depth][12]=' '
        for i in range(11):
            Map[1][i+1]=ref[self.hallway[i]]
        for i in range(4):
            temp=[x for x in self.rooms[i]]
            while len(temp)<depth:temp.append(-1)
            for j in range(depth):
                Map[1+depth-j][2*i+3]=ref[temp[j]]
        for line in Map:
            print("".join(line))
initial=state()
initial.readInput()
PQ=[(0,0,initial)]
numStates=1
seen=set()
solution=[]
while PQ:
    cost,n,position=heapq.heappop(PQ)
    flat=position.flatten()
    if flat in seen:continue
    seen.add(flat)
    solved=position.solved()
    if sum(solved)==4*depth:
        print("Minimum Cost :",str(cost))
        while position:
            solution.append(position)
            position=position.parent
        break
    for i in range(4):
        if len(position.rooms[i])==solved[i]:continue
        temp=position.copy()
        mover=temp.rooms[i].pop()
        moves1=depth-len(temp.rooms[i])
        newpos=2*i+2
        left,right=newpos,newpos
        while left>0:
            if temp.hallway[left-1]==-1:left-=1
            else:break
        while right<10:
            if temp.hallway[right+1]==-1:right+=1
            else:break
        for j in range(left,right+1):
            if j%2==1 or j%5==0:
                temp2=temp.copy()
                temp2.hallway[j]=mover
                moves2=abs(newpos-j)
                temp2.parent=position
                temp2.extra=(10**mover)*(moves1+moves2)
                numStates+=1
                heapq.heappush(PQ,(cost+temp2.extra,numStates,temp2))
    for i in range(11):
        mover=position.hallway[i]
        if mover==-1:continue
        if len(position.rooms[mover])==solved[mover]:
            target=2*mover+2
            direction=1
            if i>target:direction=-1
            valid=1
            for j in range(i+direction,target,direction):
                if position.hallway[j]!=-1:valid=0
            if valid:
                moves2=depth-len(position.rooms[mover])
                temp=position.copy()
                temp.hallway[i]=-1
                temp.rooms[mover].append(mover)
                moves1=abs(target-i)
                temp.parent=position
                temp.extra=(10**mover)*(moves1+moves2)
                numStates+=1
                heapq.heappush(PQ,(cost+temp.extra,numStates,temp))
print("Solution found in %s seconds"%(time.time()-start_time))
total=0
while solution:
    S=solution.pop()
    S.printMap()
    if S.parent:
        total+=S.extra
        print('+',str(S.extra),'=',str(total))
    else:
        print(total)
    print()
print("%s seconds"%(time.time()-start_time))
