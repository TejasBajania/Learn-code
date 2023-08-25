def prime(n):
    flag = False
    if n > 1:
        for  i in range(2,n):
            if (n % i) == 0:
                flag = True
                break
    if flag:
        return "Not a prime"
    else:
        return "Prime number"
num = int(input("Enter number"))
print(prime(num))