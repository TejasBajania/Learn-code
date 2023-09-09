def is_permutation(str1,str2):
    
    if len(str1) != len(str2):
        return False
    count = len(str1)
    res = 0

    for st in str1:

        if st in str2:

            res = res +1
        else:
            continue
    
    return res == count

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


if is_permutation(str1,str2):
    print('Give string is permutation of other')
elif not is_permutation(str1,str2):
    print('Give string is not permutation of other')
else:
    print(is_permutation(str1,str2))