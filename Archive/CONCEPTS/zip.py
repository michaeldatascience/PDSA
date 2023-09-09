keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# combine k,v to dict using zip
myDict = dict(zip(keys,values))
print(myDict)

# using dict {} comprehension
myDict2 = {k:v for (k,v) in zip(keys,values) }
print (myDict2)

