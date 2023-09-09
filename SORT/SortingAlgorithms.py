'''
Comparison based sorting algorithms
Bubble, Selection, Insert, Merge, Quick
not better than O(n log n)

'''
# BUBBLE SORT
# Repeatedly compares adjacent elements and swaps them if in wrong order. Each cycle results in one element (heighest or lowest) to be
# placed at correct position, bubbling up to its correct position.
# STABLE
# Time: O(n^2)
# Space: O(1) as it sorts the list in-place (without requiring additional memory)
# Two Loops, Comparison based, adjacent elements swapped, optimization using swap flag

def bubbleSort(L):
    n = len(L)
    swapped = True
    for i in range (n-1,0,-1):
        if not swapped:
            break
        swapped = False
        for j in range (0,i):
            if L[j]>L[j+1]:
                (L[j+1],L[j]) = (L[j],L[j+1])
                swapped = True

    return (L)




# SELECTION SORT    
# (comparison at time of selection, no new list created)
# Simple comparision based algorithm, divides the list into two parts (sorted and unsorted)
# In each iteration it swaps the smallest element from unsorted part with fist element of sorted part
# Time Complexity: O(N^2)
# Comparision Based, Selection of smallest element, swapping elements, maintaining sorted and unsorted parts
# Chosing (or selecting) smallest element and placing it at its correct place

# set MIN to 0th element
# search for minimum element in the min+1 to entire list
# swap the value of minimum element with min position
# increment to next element
# Stable: NO
# Sort in place: Yes


def selectionSort(L):
    min_val = 0
    for step in range(0, len(L)):                           # Holds last sorted value index
        min_index = step                                    # initialize min_index, considering first new element to be smallest
        for i in range(step+1, len(L)):                     # from next to last sorted index till end
            if L[i] < L[min_index]:                         # compare 
                min_index = i                               # if minimum found, keep in min_index
        
        (L[min_index], L[step]) = (L[step], L[min_index])   # at this time, min_index is either first element or minimum
                                                            # step is the position for next smallest index 

    return (L)


'''
INSERTION SORT  
(comparison at the time of insertion)
Repeat (n-1) times
    get the next element
        starting from this this element till the beginning 
            if current element is smamler than previous then swap
            
        stop untill you
'''
def insertionSort(L):
    n = len(L)
    for next in range(1, len(L)):
        # next element starts from 1 and continues till end of list
        j = next
        # starting from next element go back till first element
        while (j-1>=0 and L[j] <= L[j-1]):
            # keep swapping and going down as long as you find larger element
            (L[j],L[j-1])= (L[j-1],L[j])
            j = j-1

    return (L)


'''
MERGE SORT  (divide and conquer)

L=[12,4,10,1,-19]
[12,4,10]         [1,19]
[12,4] [10]         [1] [19]
[12] [4]            ---------
--------    
[4, 12]             [1,19]
[4,10,12]           
[1,4,10,12,19]

'''


def merge(A,B):
    (a,b) = (len(A),len(B))
    (L,i,j) = ([],0,0)
    while (i < a and j < b):
        if (A[i] < B[j]):
            L.append(A[i])
            i += 1
        else:
            L.append(B[j])
            j += 1
    while (i < a):  # Append any remaining elements in A
        L.append(A[i])
        i += 1
    while (j < b):  # Append any remaining elements in B
        L.append(B[j])
        j += 1
    return L



def mergeSort(L):
    # Divide option.
    n = len(L)
    if (n<=1):
        return L
    
    left = mergeSort(L[:n//2])
    right = mergeSort(L[n//2:])
    combined = merge(left,right)
    return combined


#L=[12,4,10,1,-19]
#print(mergeSort(L))


'''
quickSort
countingSort
radixSort

'''



print(4//2)