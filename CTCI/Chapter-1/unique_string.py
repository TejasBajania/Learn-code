def isunique(str_):

    if str_ is None:
        return 'Wrong input'
    
    cur_str = []
    for st in str_:
        if st in cur_str:
            return False
        else:
            cur_str.append(st)

    return True

str_ = input()

if isunique(str_):
    print('Unique')
elif not isunique(str_):
    print('Not unique')
else:
    print(isunique(str_))