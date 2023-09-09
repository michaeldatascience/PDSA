'''
[13,12,11,13,14,13,7,7,13,14,12]
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]
'''
# write code here

    
def histogram(L):
    output = []
    for i in range (len(L)):
        record = ()
        record = (*record, L[i])
        record = (*record, L.count(L[i]))
        if output.count(record) ==0:
            output.append(record)

    output.sort(key=lambda a: (a[1],a[0]))

    return output

# sufix code
L= [13,12,11,13,14,13,7,7,13,14,12]
print(histogram(L)) 