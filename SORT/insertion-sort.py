'''
Text implementation is little different.

Algorithm:
InsertionSort(L)
pointer1: start from second element till end
    pointer2: start from 0 till pointer1
        if pointer2 > pointer1 // since 0-pointer2 is sorted, find first element that is higher than current pointer 
            Move pointer1 (remove and insert at) to left of above found position

 [9, 6, 5, 0, 8, 2, 7, 1, 3, 4]

 i: 0,1,2...9

 i      L[i]    insert             L
 1      6       9                   [6|, 9, 5, 0, 8, 2, 7, 1, 3, 4]
 2      5       6                   [5, 6|, 9, 0, 8, 2, 7, 1, 3, 4]
 3      0       5                   [0, 5, 6|, 9, 8, 2, 7, 1, 3, 4]
 4      8       6+                  [0, 5, 6, 8|, 9, 2, 7, 1, 3, 4]
 5      2       5                   [0, 2, 5, 6, 8|, 9, 7, 1, 3, 4]
 6      7       6+                  [0, 2, 5, 6, 7, 8|, 9, 1, 3, 4]
 7      1       6+                  [0, 1, 2, 5, 6, 7, 8|, 9, 3, 4]
 8      3       2                   [0, 1, 2, 3, 5, 6, 7, 8|, 9, 4]
 9      4       3+                  [0, 1, 2, 3, 4, 5, 6, 7, 8|, 9]

 outer loop / cycle runs from 1->n (n-1 times)
 for insertion we need to compare n-k elements

 
Time Complexity:B
Best        O(n2)
Average     O(n2)
Worst       O(n2)

There are two loops.. So complexity is n*n = n2
'''

def InsertionSort(L):
    for i in range(1,len(L)):   # starting from 1 till end of the list
        for j in range (len( L[:i])):   # from 0 till i the list is sorted
            if L[j] >= L[i]:            # if value being checked is greater that next value in the sorted list. then place the value beore 
                temp = L[i]             # Hold temporary
                L.remove(temp)          # Remove from the list
                L.insert(j,temp)        # Insert temp value 


L= [9, 6, 5, 0, 8, 2, 7, 1, 3, 4, -1, 10, 19]

InsertionSort(L)
print(L)