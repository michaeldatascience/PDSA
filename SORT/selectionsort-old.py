'''
Selection Sort.
Initialize pointer to 1st element in the list
Traverse from 1st position till n position to find the smallest value
replace the smallest value with the value of pointer.
move pointer to second element and trverse from 2nd posoition to end and find the smallest.
repace smallest with pointer

[64, 25, 12, 22, 11] n=5

i   L[i]    L[i:]                   min(L[i:])      before swap L               after swap
0   64      [25, 12, 22, 11]        11              [64*, 25, 12, 22, 11]       [11, 25, 12, 22, 64]
1   25          [12, 22, 64]        12              [11, 25*, 12, 22, 64]       [11, 12, 25, 22, 64]
2   12              [22, 64]        22              [11, 12, 25*, 22, 64]       [11, 12, 22, 25, 64]
3   22              [22, 64]        22              [11, 12, 25, 22*, 64]       [11, 12, 22, 25, 64]
4   64                  [64]        64              [11, 12, 22, 25, 64*]       [11, 12, 22, 25, 64]

'''

def selectionSort(L):
    for start in range (len(L)):
        min_pos = start
        for i in range(start,len(L)):
            if L[i] < L[min_pos]:
                min_pos = i

        (L[start],L[min_pos]) = (L[min_pos], L[start])        


def selectionSort2(L):
    curr = 0
    while (curr < len(L)):
        curr_val = L[curr]
        min_pos = curr
        for i in range (curr,len(L)):
            if L[i]< curr_val:
                min_pos = i
        min_pos = L.index(min_val)
        if curr_val >= min_val:
            (L[curr],L[min_pos]) = (min_val,curr_val)
        
        curr+=1
    
    return L

L=[54, 26, 93, 17, 77, 31, 44, 55, 20, 26, 22, -1]
selectionSort(L)
print(L)


