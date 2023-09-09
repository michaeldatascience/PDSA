def removeDuplicate(head):
    if head.data == None:
        return
    
    while head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
            
  

# Suffix Code(Do not update or remove this)
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None


def append(head, data):
  if head.data == None:
    head.data = data
  else:
    temp = head
    while temp.next != None:
      temp = temp.next
    temp.next = Node(data)


def display(head):
  temp = head
  while temp != None:
    print(temp.data, end=" ")
    temp = temp.next


print('Output Linked List: ', end="")
inputList = '1 1 2 2 2 3 3 4 4 4 4 5 7 9'
#a = [int(i) for i in input().split(" ")]
a = [int(i) for i in inputList.split(" ")]
head = Node()
for i in a:
  append(head, i)
removeDuplicate(head)
display(head)
