#Dictionary Comprehension
'''
L= 'one,four,one,six,five,one,four,two,nine,one'
Convert this to Dict with frequency as value
i.e. 
D={'one':4,'two':1}

'''
input= 'one,four,one,six,five,one,four,two,nine,one'
L=input.split(',')
D = {key:L.count(key) for key in L}
print(L)
print(D)


'''
Write a function named value_to_keys that accepts a dictionary D and a variable named value as arguments. It should return the list of all keys in the dictionary 
that have value equal to value. If the value is not present in the dictionary, the function should return the empty list.

value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10)  [1, 4]
value_to_keys({'good': 'boy', 'great': 'expectations'}, 'great') []

'''

def value_to_keys(D, value):
    L=[]
    for i in D.keys():
        if(D[i]==value):
            L.append(i)
    
    print(L)

def value_to_keys2(D, value):
    L = [k for k,v in D.items() if v==value]
    print(L)

#value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10) 
#output [1, 4]
value_to_keys2({1: 10, 2: 100, 3: 1000, 4: 10}, 10) 

#value_to_keys({'good': 'boy', 'great': 'expectations'}, 'great') 
#output[]


# Try to debug and understand
#Graded Assignment 11
#Q4
L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(f'L ={L}')

L1 = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L1.append(y - x)
print(f'L1={L1}')

L2 = [ ]
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L2.append(y - x)
print(f'L2={L2}')


L3 = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L3 += [y - x]
print(f'L3={L3}')

L4 = []
for y in [3, 4, 5]:
    for x in [1, 2, 3]:
        if y > x:
            L4 += [y -x]
print(f'L4={L4}')