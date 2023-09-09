'''
Min Difference in list
'''

def findDiff(L):
    return max(L) - min(L)



# combination with recursion
def combinationR(L,p,start=0,curList=[], result=[]):
    #base case
    if len(curList)==p:
        # add curent to result
        result.append(curList[:])   # slicing creates a copy of curList
        return
    
    for i in range(start,len(L)):
        # include l[i] in curlist
        curList.append(L[i])

        #recursively generate combination of remaining lists
        combination(L,p,i+1,curList, result)
        curList.pop()

    if start==0:                #when recursion cycle is complete return result
        return result


def combinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += combinations(array[i+1:], tuple_length, prev_array_extended)
    return combs


def find_Min_Difference(L,P):
    combinationMatrix= combinations(L,P)
    combinationD={}
    for C in (combinationMatrix):
        combinationD[ findDiff(C) ] = C

    print (min(combinationD))


#def find_Min_Difference(L,P):


L= [3,4,1,9,56,7,9,12]     #eval(input().strip())
P= 5       #int(input())
#print(find_Min_Difference(L,P))

find_Min_Difference(L,P)
#print(combinations(L, 3))