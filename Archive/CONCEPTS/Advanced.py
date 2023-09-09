'''
Everything in python is an object. Including variables, function, even modules
'''
def hello():
    print("say hello")


hi = hello  # function is assigned to a variable (without () )
hi()

'''
iter
'''

'''
Comprehensions
'''


'''
extend arguments 
'''

'''
Closure and Decorators
'''


'''
generator and iterable
'''

'''
Context Manager
'''

'''
__slots__
'''

'''
for and while loop can have else
while (somecondition):
    if (some other condition)
        do something
        break

else
    loop exited without if condition
'''


'''
Filtering a list/dictionary
Finding min/max in  dictionary 

filteredD = {key:value for (key,value) in resultD.items() if value > 0 }
oddone = min(filteredD,key=filteredD.get)
'''

'''
Typeerror and ValueError
val= (10.10)
try:
    result = int(val)
    print('no error')

except TypeError:
    print('TypeError')

except ValueError:
    print('ValuError')

 
'''