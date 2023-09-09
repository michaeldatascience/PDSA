"""
Need to understand it better

Divide and Conquer
Recursive

Divide: Split the list in two halves recursively untill it can be no longer divided.
Conquer: Merge back the elements or sub-arrays into a sorted array

"""

def merge(L,R):
    i=j=0
    merged=[]
    while (i<len(L) and j<len(R)):
        if L[i] < R[j]:
            merged.append(L[i])
            i+=1
        else:
            merged.append(R[j])
            j+=1
        
    while (i < len(L)):
        merged.append(L[i])
        i+=1

    while (j < len(R)):
        merged.append(R[j])
        j+=1
    
    return merged
def mergeSort(L):
    n = len(L)
    if n < 2:
        return L
    
    mid = n//2

    left = L[:mid]
    right = L[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft,sortedRight)


array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = mergeSort(array)
print(sorted_array)