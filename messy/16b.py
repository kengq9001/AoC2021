hex_data=open("C:\\Users\\kengq\\OneDrive\\Documents\\Programming\\in.txt","r").read()
def hex_to_4_digit_binary(char):
    n=int(char,16)
    res=[0]*4
    for i in range(4):
        res[-1-i]=str(n%2)
        n//=2
    return "".join(res)
def bin_to_int(S):
    res=0
    for i in range(len(S)):
        res*=2
        res+=int(S[i])
    return res
string="".join([hex_to_4_digit_binary(hex_data[i]) for i in range(len(hex_data))])
class Packet:
    def __init__(self,start):
        self.start=start
        self.version=bin_to_int(string[start:start+3])
        self.type=bin_to_int(string[start+3:start+6])
        if self.type==4:
            i=start+6
            self.value=0
            while True:
                self.value*=16
                self.value+=bin_to_int(string[i+1:i+5])
                i+=5
                if string[i-5]=='0':break
            self.end=i
        else:
            self.subpackets=[]
            if string[start+6]=='0':
                length=bin_to_int(string[start+7:start+22])
                i=start+22
                self.end=i+length
                while True:
                    self.subpackets.append(Packet(i))
                    if self.subpackets[-1].end==self.end:
                        break
                    else:
                        i=self.subpackets[-1].end
            else:
                num_subpackets=bin_to_int(string[start+7:start+18])
                i=start+18
                for j in range(num_subpackets):
                    self.subpackets.append(Packet(i))
                    i=self.subpackets[-1].end
                self.end=i
    def printInfo(self):
        print("Version Number: "+str(self.version))
        print("Type: "+str(self.type))
        if self.type==4:
            print("Value: "+str(self.value))
        else:
            print("Subpackets: ")
            print(self.subpackets)
        print("Start: "+str(self.start))
        print("End: "+str(self.end))
    def versionNumberSum(self):
        res=self.version
        if self.type!=4:
            for subpacket in self.subpackets:
                res+=subpacket.versionNumberSum()
        return res
    def Value(self):
        if self.type==0:
            res=0
            for subpacket in self.subpackets:
                res+=subpacket.Value()
            return res
        if self.type==1:
            res=1
            for subpacket in self.subpackets:
                res*=subpacket.Value()
            return res
        if self.type==2:
            return min([subpacket.Value() for subpacket in self.subpackets])
        if self.type==3:
            return max([subpacket.Value() for subpacket in self.subpackets])
        if self.type==4:
            return self.value
        if self.type==5:
            if self.subpackets[0].Value()>self.subpackets[1].Value():
                return 1
            else:
                return 0
        if self.type==6:
            if self.subpackets[0].Value()<self.subpackets[1].Value():
                return 1
            else:
                return 0
        if self.type==7:
            if self.subpackets[0].Value()==self.subpackets[1].Value():
                return 1
            else:
                return 0
mainPacket=Packet(0)
print(mainPacket.versionNumberSum())
print(mainPacket.Value())
