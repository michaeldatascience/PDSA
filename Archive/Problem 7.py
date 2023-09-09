'''
Problem statement:

You are given a grid of m x n size. 
'''
def Min_X(n, m):
    '''
    we know that 3 block takes 1 X. 2 block takes 1 X.
    Smallest division is 2

    Logic:  find max(m,n). Call this row. Smaller is column
    case:  	row % 3
            0  // Divisible by 3. Best case
            count = (x//3) x column
            1  // e.g. 4, 7, 10, 13
            count = (x//3)-1
            row = (x % 3) + 3
            Calculate using 2-block
            2  //  e.g. 5, 8, 11
            count = (x//3)
            row = x % 3
            Calculate using 2-block
    '''
    count = 0

    while (m > 2 or n > 2):
        (row,col) = (max(m,n), min(m,n))

        #if row // 3 < 2:
        #    break

        remainder3 = row % 3
        if remainder3 == 0:    # 6,9
            count += ((row // 3) * col)    #  2, 3
            m = remainder3 # 0
            n = col
        elif remainder3 == 1:    #4, 7
            if col < 2:             # Not very elagent.
                break
            else:
                count += (((row//3)) * col)
                m = remainder3
                n = col
        elif remainder3 == 2:   # 5, 8, 11, 14
            count += ((row//3) * col) # 1, 2 , 3
            m = remainder3
            n = col

    (row,col) = (max(m,n), min(m,n))
    if row % 2 == 0:
        count += (row // 2)

    return count
  
# Suffix Code( Don't remove)
#n = int(input())
#m = int(input())
(m,n) = (7,4)
print(Min_X(n,m))