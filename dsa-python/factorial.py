def fact(n):
    if n ==1 or n ==0: 
        return 1
    else:
        fac_resp = 1
        for i in range(1,n+1):
            fac_resp=fac_resp*i
        return fac_resp
print(fact(5))