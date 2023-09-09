def mergeSortedList(head1, head2):
  newL = []
  newHead = Node()
  head3 = newHead
  while head1 != None:
    newL.append(head1.data)
    head1 = head1.next

  while head2 != None:
    newL.append(head2.data)
    head2 = head2.next


  newL.sort()

  for i in range (len(newL)):
    print(f'i:{i} newL[i]:{newL[i]}')
    append(newHead,newL[i])

  return head3


#Suffix Code(Do not update and remove this)
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None


def append(head, data):
  #print(f'append head.data: {head.data} data: {data}')
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
#a = [int(i) for i in input().split(" ")]
#b = [int(i) for i in input().split(" ")]
a = [1, 3, 5, 7, 9, 11]
b = [2, 4, 6]
head1 = Node()
head2 = Node()
for i in a:
  append(head1, i)
for j in b:
  append(head2, j)
c = mergeSortedList(head1, head2)
display(c)