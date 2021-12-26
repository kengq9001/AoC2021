import heapq
import time
start_time=time.time()
f=open("input23a.txt","r").readlines()
class state():
    def readInput(self):
        self.hallway=[-1]*11
        self.rooms=[[0,0] for i in range(4)]
        for i in range(4):
            self.rooms[i][1]=ord(f[2][2*i+3])-ord('A')
            self.rooms[i][0]=ord(f[3][2*i+3])-ord('A')
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
            if self.rooms[i]:
                if self.rooms[i][0]==i:
                    if len(self.rooms[i])==1 or self.rooms[i][1]!=i:
                        result[i]=1
                    else:
                        result[i]=2
        return result
    def flatten(self):
        return (tuple(self.hallway),tuple(self.rooms[0]),tuple(self.rooms[1]),tuple(self.rooms[2]),tuple(self.rooms[3]))
initial=state()
initial.readInput()
PQ=[(0,0,initial)]
numStates=1
seen=set()
while PQ:
    cost,n,position=heapq.heappop(PQ)
    flat=position.flatten()
    if flat in seen:continue
    seen.add(flat)
    solved=position.solved()
    if sum(solved)==8:
        print(cost)
        break
    for i in range(4):
        if len(position.rooms[i])==solved[i]:continue
        temp=position.copy()
        mover=temp.rooms[i].pop()
        moves1=2-len(temp.rooms[i])
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
                numStates+=1
                heapq.heappush(PQ,(cost+(10**mover)*(moves1+moves2),numStates,temp2))
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
                temp=position.copy()
                temp.hallway[i]=-1
                temp.rooms[mover].append(mover)
                moves1=abs(target-i)
                moves2=3-len(temp.rooms[mover])
                numStates+=1
                heapq.heappush(PQ,(cost+(10**mover)*(moves1+moves2),numStates,temp))
print("%s seconds" % (time.time() - start_time))
