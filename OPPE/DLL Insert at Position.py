# Prefix Code
class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class doubly_linked_list:

  def __init__(self):
    self.head = None
    self.last = None

  def insert_end(self, data):
    newnode = Node(data)
    newnode.prev = self.last
    if self.head == None:
      self.head = newnode
      self.last = newnode
    else:
      self.last.next = newnode
      self.last = newnode


  def insert_at_pos(self,data,pos):
    # Node: node.data, node.next, node.prev
    # DLL: self.head, self.last

    # Create the new node
    newNode = Node(data)
    curr = self.head
    # Traverse the DLL
    for i in range(1,pos):
      curr = curr.next
    
    right = curr
    left = curr.prev
    
    newNode.prev = left  #    1 2 3 4 <-[x] 5 6 7
    newNode.next = right  #    1 2 3 4 [x]-> 5 6 7
    right.prev = newNode #    1 2 3 4-> [x] 5 6 7 
    left.next = newNode #    1 2 3 4 [x] <- 5 6 7
    


  
  def _insert_at_pos(self, data, pos):
    # initialize current pointer to head
    cur = self.head
    # traverse the current pointer sequencially to reach the desired position
    for i in range(pos - 1):
      #print(f'i: {i} cur.data: {cur.data}')
      cur = cur.next

    # Create the new Node
    newNode = Node(data)
    # copy ref of last node
    lastNode = cur.prev
    lastNode.next = newNode
    newNode.prev = lastNode
    newNode.next = cur
    cur.prev = newNode


# Suffix Code

  def traverse(self):
    temp = self.head
    while temp != None:
      if temp.next != None:
        print(temp.data, end=',')
      else:
        print(temp.data)
      temp = temp.next

  def traverse_rev(self):
    temp = self.last
    while temp != None:
      if temp.prev != None:
        print(temp.data, end=',')
      else:
        print(temp.data)
      temp = temp.prev

#ins = eval(input())
#data = int(input())
#pos = int(input())

ins = [1,3,5,7,9]
data = 20
pos = 2


A = doubly_linked_list()
for i in ins:
  A.insert_end(i)

print (f'A: {ins}, insert {data} at {pos}')
A.insert_at_pos(data, pos)
A.traverse()
A.traverse_rev()
