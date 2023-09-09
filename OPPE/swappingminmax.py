def listAppend(head,data):
    newNode = Node(data)
    head.next = newNode
    head = head.next
    
def mergeSortedList(head1,head2):
    head3 = Node()
    newHead = head3
    while (head1 and head2):
        if head1.data > head2.data:
            listAppend(head3,head2.data)
            listAppend(head3,head1.data)
        else:
            listAppend(head3,head1.data)     
            listAppend(head3,head2.data)

        head1 = head1.next
        head2 = head2.next
        #print(f'new node {nextNode.data} added')
    
    #print(f'Check anything left')
    while(head1):
        head1 = head1.next
        listAppend(head3,head1.data)
        
    while(head2):
        head2 = head2.next
        listAppend(head3,head2.data)
        
    return newHead

