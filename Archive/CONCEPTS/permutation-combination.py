'''
Given a list of n size L=[a1,a2,...,an] and a number p (p<n)
combination(L, p) -> all possible unique combinations of subsets from L of size p

With recursion:
idea is to fix a positin, then recursively generate elements for rest positions

base case: when generated list becomes given size 'p'
recursive function should include the position, starting from 0
and it must include the current output (baking) initizlized to []

L = ['A', 'B', 'C', 'D']
p = 2

start:
L=[ABCD], P=2, curr=[], start=0
if len(cur) == 2 // base case
    return

for i in range(start,len(L))
    cur.append(L[i])

    combin(L,start+1,cur)

'''
result=[]
def combination(L,p,start=0,curList=[], result=[]):
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

# Example list and p
L = ['A', 'B', 'C', 'D']
p = 2

# Generate combinations
#print(combination(L,p))

print(combination(L,2))
