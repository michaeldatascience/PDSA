class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def removeDuplicate(head):
    #print(f'traversing')
    h2 = head
    while (head.next):
        #print('head: {head.data}')
        if (head.data == head.next.data) :
            #print(f'head.data=head.next.data')
            head.next = head.next.next
        else:
            #print(f'Next')
            head = head.next
        
        

list1 = [1, 1, 5, 5, 5, 6, 8, 8, 8, 10, 12 , 12 , 18 , 23 ,24]

def createLinkedList(input_list):
    head = Node(input_list[0])
    curr = head
    for data in input_list[1:]:
        curr.next = Node(data)
        curr = curr.next
    return head

def printLL(head):
    curr = head
    while curr is not None:
        print (curr.data, end=' ' )
        curr = curr.next

# Convert the lists to linked lists
head1 = createLinkedList(list1)

removeDuplicate(head1)
printLL(head1)