import heapq
import time
start_time=time.time()
f=open("C:\\Users\\kengq\\OneDrive\\Documents\\Programming\\in.txt","r").readlines()
depth=len(f)-3
class state():
    def readInput(self):
        self.hallway=[-1]*11
        self.rooms=[[0]*depth for i in range(4)]
        for i in range(4):
            for j in range(depth):
                self.rooms[i][j]=ord(f[1+depth-j][2*i+3])-ord('A')
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
    if sum(solved)==4*depth:
        print(cost)
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
                moves2=depth-len(position.rooms[mover])
                temp=position.copy()
                temp.hallway[i]=-1
                temp.rooms[mover].append(mover)
                moves1=abs(target-i)
                numStates+=1
                heapq.heappush(PQ,(cost+(10**mover)*(moves1+moves2),numStates,temp))
print("%s seconds" % (time.time() - start_time))
