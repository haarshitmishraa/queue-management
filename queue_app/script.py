

class Queue:
    tokenNO=0
    #flag=0
    total=[]
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self,tokenNO):
        self.tokenNO =tokenNO
        self.items.insert(0,tokenNO)
     
        s = len(self.items)
        print("Your token no. is  ",self.tokenNO )
        
        print("total size ", s)
        
        
        q.tokenNO+=1
        #flag++
        return self.tokenNO, q.after(tokenNO)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueus(self):
        for item in self.items:
            print(item)
            q.total.append(item)
            return q.total
    
    def after(self,item):
        s = len(self.items)
       
        return s - (self.items.index(item)+1)

q = Queue()


def calll():
   return q.enqueue(q.tokenNO)

def next():
    q.dequeue()
    return q.size

def count():
    return q.size