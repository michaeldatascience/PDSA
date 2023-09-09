'''
https://towardsdatascience.com/10-topics-python-intermediate-programmer-should-know-3c865e8533d6
# General Syntax
# Expression for item in iterable condition

#List Comprehension:
[expr(item) for item in iterable ]

#Set Comprehension:
{expr(item) for item in iterable }

#Dictionary Comprehension:
{expr(key):expr(value) for key,value  in iterable }

#Multiple 
[x,y for x in range(5) for y in range(3)]
same as
for x in range(5):
    for y in range(3):
        values.append(x,y)

# Nested
[[Second Loop] First Loop]

[ [y**2 for y in range(x)] for x in range(5)]
same as

values=[]
for x in range(5):
    inner=[]
    for y in range(x):
        inner.append(y**2)
    
    values.append(inner)

'''
# nested comprehension
values1=[]
values2=[]
for x in range(5):
    #print(f'x:{x}')
    inner=[]
    for y in range(x):
        #print(f'y:{y}')
        inner.append(y**2)
        #print(f'inner:{inner}')
    values1.append(inner)
print(values1)

# nested comprehension 
values2=[[y**2 for y in range(x)] for x in range(5)]
print(values2)



'''
// = xx.yy -> xx
% = xx.yy -> .yy
101 // 4 = 25
101 % 4 = 1

101 = 4 * (101//4) + (101%4)
N = D * ( N // D) + (N % D)
'''




# iterable operations
# index of element 
numbers = [1, 4, 5, 3, 5, 7, 8, 5]
alpha=['a','b','c','d','c','f','g','h','a','b','c','d','a','f']
print(numbers.index(5))

#index of element 'c'in alpha after 3 and before 10
print(alpha.index('c',3,10))

# Generate alphabets (other series)
alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
print(alphabets)


# Return a list of numbers that appear most frequently in an input list
# Show multiple if tied
# Eg. Input: [1, 1, 2, 2, 3]
# Output: [1, 2]

def most_frequent(lst):
    count_dict = {}
    for i in lst:
        if count_dict.get(i) == None:
            count_dict.update({i : lst.count(i)})
    return [x for x in count_dict.keys() if count_dict[x] == max(count_dict.values())]


print(most_frequent([1, 1, 2, 2, 3,1,2,1,4,3,2,1,4,1,32,1]))

raiseTo = lambda x,y : x**y

print(raiseTo(2,10))


# Updating, inserting values to list inside a dict
# Helper function
# note: must always first check if it exists, then append (since value is list)
# otherwise set value to a list []
def dictInsert(D,k,v):
    if k in D:
        D[k].append(v)  # Important this cannot be D[k].append([v])
    else:
        D[k]=[v]
        
D={'a':['alphabet','amazon','apple'],'b':'bbc','c':'caterpillar,cnn'}
F={}

dictInsert(D,'a', 'anotherone')
print(D)
dictInsert(D,'X', 'XXX')
print(D)


# set can never start with { }
# only possible ways to init set are
S = set()
S = {1,2,3}
S = set([1,2,3])


# str object does not support item assignment
word_string = 'abcd'
#word_string[0] = 'z'
#print(word_string)

# strange behavior, when using list inside list, .copy() is doing by reference
# but not so in single list
A = [['A', 'B'], ['C', 'D']]
B = A.copy()	# avoid this for matrices
A[0][0] = 'X'
B[1][1] = 'Y'
print(A)
print(B)




def bin_search(L, start, end, x):
    if start > end:
        return False
    mid = (start + end) // 2
    if x == L[mid]:
        return True
    elif x > L[mid]:
        start = mid + 1
    else:
        end = mid - 1
    return bin_search(L, start, end, x)

print (bin_search('a,s,d,f,g,h,j,k,l,q,w,e,r,t,y,u,i,o,p',0 , 10, 'g' ))

list1 =  [1,2,3,4,5,6,7,8,9,10,1]
s = 0
e = 11
mid = (s+e) // 2
print(mid)