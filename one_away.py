st1='pale'

st2 = 'bake'



if all(l in st1 for l in st2) or all(l in st2 for l in st1):

    print('one edit away')

else:

    print('zero edits away')