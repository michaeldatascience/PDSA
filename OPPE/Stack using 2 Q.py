# Prefix Code
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()
            
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    #Write code here
    #Costly Push Method.
    def push(self,data):
        self.q1.enqueue(data)
        self.size +=1

        while len(self.q2.items)>0:
          print(f'q2.items {len(self.q2.items)}')
          self.q1.enqueue(self.q2.dequeue())
          #print(f'q1 {self.q1.items}')

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
      
    def pop(self):
        if len(self.q2.items)==0:
            return 'Stack is empty'
        else:
            self.size -=1
            return (self.q2.dequeue())
        
    def top(self):
        if len(self.q2.items)==0:
            return 'Stack is empty'
        else:
            return (self.q2.items[-1])

    def isempty(self):
        if self.size ==0:
            return True
        else:
            return False
        
# Suffix Code
#inp = eval(input())
#dl = int(input())
inp = [10,20,30,40,50]
dl = 2
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())

        
    