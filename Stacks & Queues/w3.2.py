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

  # write code here
  def insert_at_pos(self, data, pos):
    # initialize current pointer to head
    cur = self.head
    # traverse the current pointer sequencially to reach the desired position
    for i in range(pos):
      cur = cur.next

    newNode = Node(data)
    newNode.prev = cur
    newNode.next = cur.next


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

ins = '1,3,5,7,9' #eval(input())
data = 20 #int(input())
pos = 2 #int(input())
A = doubly_linked_list()
for i in ins:
  A.insert_end(i)
A.insert_at_pos(data, pos)
A.traverse()
A.traverse_rev()

