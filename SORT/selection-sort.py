'''
Algorithm:
SelectionSort(L)
  repeat(size(L)-1)
    set first unsorted element as minimum
    for each element of unsorted list
      if element <  minimum
        set element as new minimum
    
    swap element with new minimum
        
    
[20,12,10,15,2] 20<-2
[2,12,10,15,20] 12<-10
[2,10,12,15,20] 

Time Complexity:B
Best        O(n2)
Average     O(n2)
Worst       O(n2)

There are two loops.. So complexity is n*n = n2
'''


def selectionSort(L):
    for start in range(len(L)):
        min=start
        for i in range(start,len(L)):
            if L[i] < L[min]:
                min = i
        
        (L[start], L[i])=(L[min],L[start])


L=[20,12,10,15,2]
selectionSort(L)
print(L)