'''
BubbleSort
'''

def bubbleSort(arr):
    L = arr.copy()
    cycle=0
    while(cycle<len(L)-1):
        for i in range (len(L)-1):
            left = L[i]
            right=  L[i+1]
            if right < left:
                (L[i],L[i+1]) = (right,left)

        cycle+=1
    return L

L=[-2,45,0,11,-9]
print(bubbleSort(L))