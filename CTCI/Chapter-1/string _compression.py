stinpt = 'aabcccccaaa'

resp = ''
cnt = 1

for ind in range(1,len(stinpt)):
    
    if stinpt[ind-1] == stinpt[ind]:
        cnt+=1 
    else:
        resp=resp+stinpt[ind-1]
        if cnt >=1:
            resp=resp+str(cnt)
        cnt =1 
print(cnt)    

resp = resp + stinpt[-1]
if cnt >=1:
    resp += str(cnt)


print(resp)