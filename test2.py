L1 = [1,2,3,4,5,6]
L2 = [2,3,4,4]
L3 = [3,4,5]
L4 = [1,2,4]
L5 = [5]
 
def is_sublist(lst1,lst2):
	
    if lst2[0] in lst1:
        start_index = lst1.index(lst2[0])
    else:
        return False


    for index1 in range(len(lst1)):

        if lst2 == lst1[index1:index1+len(lst2)]:

            return True
        
        else:

            continue
    
    return False    
    


print(is_sublist(L1,L2)) #-> False
print(is_sublist(L1,L3)) #-> True
print(is_sublist(L1,L4)) #-> False
print(is_sublist(L1,L5)) #-> True




s1 = "onetwotwoplusthree"
s2 = "onetwothreeminustwotwo"

def eval_str(str_):

    alpha_digit = {'one':1,'two':2, 'three':3,'plus':'+','minus':'-'}

    for operator,data  in alpha_digit.items():
        str_ = str_.replace(operator, str(data))

    return eval(str_)    

print(eval_str(s1)) #-> 125
print(eval_str(s2)) #-> 101
