'''
Odd One

'''

def odd_one(L):
    resultD = {'int':0, 'float':0, 'str':0, 'bool':0}

    for i in L:
        if type(i)== int:
            resultD['int']+=1
        elif type(i)== float:
            resultD['float']+=1
        elif type(i)==str:
            resultD['str']+=1
        elif type(i)==bool:
            resultD['bool']+=1
        
    #newDict = { key:value for (key,value) in dictOfNames.items() if key % 2 == 0}

    filteredD = {key:value for (key,value) in resultD.items() if value > 0 }
    oddone = min(filteredD,key=filteredD.get)

    print( filteredD)
    print(oddone)
    #keys = resultD.keys()
    #values = resultD.values()

    #return odd

L = [2,13,16,4.5]
odd_one(L)
#print(odd_one(eval(input().strip())))