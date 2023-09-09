'''
dict_to_list({'abc': 3, 'def': 10})
[('abc', 3), ('def', 10)]

list_to_dict([('def', 10), ('abc', 3)])
{'abc': 3, 'def': 10}
'''



def dict_to_list(D):
    #method 1
    V = D.values()
    K = D.keys()
    L = list(zip(K,V))
    print(L)

    #method 2
    L = [(K,V) for k,v in D.items() ]
    return(L)

def list_to_dict(L):
    D = {L[i]:L[i+1] for i in range(len(L)-1) }
    print (D)
    return D
#this method lost order

dict_to_list({'abc': 3, 'def': 10})
list_to_dict([('def', 10), ('abc', 3)])

def dictInsert(D,k,v):
    if k in D:
        D[k].append(v)
    else:
        D[k]=[v]
        

D={'a':['alphabet','amazon','apple'],'b':'bbc','c':'caterpillar,cnn'}
F={}

dictInsert(D,'X', 'anotherone')
print(D)


print(27%26)