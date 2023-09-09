def str_to_url(str_, len_):
    res_str = ''
    for ind in range(len_):

        if ind == len_:
            break

        if str_[ind] == ' ':
            res_str = res_str + '%20'
        else:
            res_str = res_str + str_[ind]
    
    return res_str
    

str_ = input()
len_ = int(input())


url_str = str_to_url(str_, len_)

print(url_str)

