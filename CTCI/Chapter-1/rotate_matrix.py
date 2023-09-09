matrixx = [[1,2,3],[4,5,6],[7,8,9]]


r = []

i = 0 

for row in matrixx:
    listtoADD = [item[i] for item in matrixx]
    r.append(listtoADD)
    i = i+1

print(r[::-1])
print(r)

# ALter way
print([[x[i] for x in matrixx] for i in range(len(matrixx))][::-1])