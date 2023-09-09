st1='waterbottle'

st2 = 'erbottlewat'



if all(l in st1 for l in st2) or all(l in st2 for l in st1):
    print('Is rotation')

else:
    print('Not a rotation')