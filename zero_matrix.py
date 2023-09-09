matrixx = [[1,2,3],[4,0,6],[7,8,9]]

for i in range(len(matrixx)):

    for j in matrixx[i]:

        # print(i,',',j)
        if j == 0:
            matrixx[i] = [0]*len(matrixx[i])
            break
print(matrixx)


