class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Using Linked Lists
def mergeSortedList(head1,head2):
    head3 = curr = Node()
    while (head1 and head2):
        if head1.data < head2.data:
            curr.next = head1
            curr = head1            
            head1= head1.next
        else:
            curr.next = head2
            curr = head2
            head2= head2.next
            
    if head1 or head2:
        if head1:
            curr.next = head1 
        else:
            curr.next = head2
        
    
    return head3.next



# Using Python List
def LL2List(head):
    List = []
    while (head):
        List.append(head.data)
        head = head.next
    
    return List
    
def List2LL(List, head):
    curr = head
    for i in range (len(List)):
        iNode = Node(List[i])
        curr.next = iNode
        curr = curr.next
    
    return head    

def printLL(head):
    curr = head
    while curr is not None:
        print (curr.data, end='->' )
        curr = curr.next
    
def lengthLL(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def _mergeSortedList(head1,head2):
    #Using Python Lists shortcut
    L1 = LL2List(head1)
    L2 = LL2List(head2)
    L3 = L1 + L2
    L3.sort()
    head3 = Merged =  Node(0)
    Merged = List2LL(L3,head3)
    #printLL(Merged)
    
    return Merged.next
# Using Python List




list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10, 12]

def createLinkedList(input_list):
    head = Node(input_list[0])
    curr = head
    for data in input_list[1:]:
        curr.next = Node(data)
        curr = curr.next
    return head

# Convert the lists to linked lists
head1 = createLinkedList(list1)
head2 = createLinkedList(list2)

# Merge the two sorted linked lists
merged_head = mergeSortedList(head1, head2)

# Print the merged linked list
printLL(merged_head)
