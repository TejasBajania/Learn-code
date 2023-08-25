# 1,1,2,3,5,8,13,21,34

def fibnacci(num):

    fibolist = []
    count = 0
    n1, n2 = 0,1
    while count < num:
       fibolist.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    
    return fibolist
    
number = int(input("Enter number upto which you required fibnacci"))

print(fibnacci(number))