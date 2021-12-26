ref=[0,0,0,1,3,6,7,6,3,1]
def my_mod10(x):
    if x%10==0:return 10
    return x%10
winDP={}
loseDP={}
def calcWin(p1,s1,p2,s2):
    if s1>=21:return 1
    if s2>=21:return 0
    if (p1,s1,p2,s2) in winDP:return winDP[(p1,s1,p2,s2)]
    ways=0
    for i in range(3,10):
        ways+=ref[i]*calcLose(p2,s2,my_mod10(p1+i),s1+my_mod10(p1+i))
    winDP[(p1,s1,p2,s2)]=ways
    return ways
def calcLose(p1,s1,p2,s2):
    if s2>=21:return 1
    if s1>=21:return 0
    if (p1,s1,p2,s2) in loseDP:return loseDP[(p1,s1,p2,s2)]
    ways=0
    for i in range(3,10):
        ways+=ref[i]*calcWin(p2,s2,my_mod10(p1+i),s1+my_mod10(p1+i))
    loseDP[(p1,s1,p2,s2)]=ways
    return ways
print(calcWin(8,0,2,0))
print(calcLose(8,0,2,0))
