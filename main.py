
import random

class queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class patient:
    def __init__(self,time):
        self.timestamp=time
        self.age=random.randrange(20,61)

    def getstamp(self):
        return self.timestamp

    def getage(self):
        return self.age

    def waittime(self, currenttime ):
        return currenttime-self.timestamp


class doctor:
    def __init__(self,rate):
        self.ageRate=rate
        self.currentpatient=None
        self.timeremaining=0

    def tick(self):
        if self.currentpatient!=None:
            self.timeremaining-=1
            if self.timeremaining<=0:
                self.currentpatient==None

    def busy(self):
        if self.currentpatient!=None:
            return True
        else:
            return False

    def patientnext(self,newpatient):
         self.currentpatient=newpatient
         self.timeremaining=(newpatient.getage()/self.ageRate)*60   

def simulation(numseconds,rate):
    simdoctor=doctor(rate)
    patientqueue=queue()
    waitingtimes=[]

    for currentsecond in range (numseconds):
        if random.randrange(1,361)==2:
            pat=patient(currentsecond)
            patientqueue.enqueue(pat)
        if (not simdoctor.busy()) and (not patientqueue.isEmpty()):
            nextpatient=patientqueue.dequeue()
            waitingtimes.append(nextpatient.waittime(currentsecond))
            simdoctor.patientnext(nextpatient)
        simdoctor.tick()
    averagewait=sum(waitingtimes)/len(waitingtimes)

    print("averagewait",averagewait,"sec",",residual patient",patientqueue.size(),"paient")


for i in range (10) :
    simulation(14400,5)

