"""
Part 1

Calculate Factorial of a number

EX: - 7! = 7*6*5*4*3*2*1

Part 2

Find the number of trailing zeroes
"""

def factorial(n):

    if n == 1 or n == 0:

        return 1 
    
    else:

        fact_resp = 1

        for i in range(1, n+1):
            
            fact_resp = fact_resp * i

    return fact_resp

def factorial_trailing_zeroes(n): 
    """ Brute-force approach"""
    # fac = factorial(n)
    # count = 0 

    # while (fac%10 == 0):
    #     fac = fac / 10
    #     count = count + 1
    # return count
    """ Optimal approach"""
    # 5! = 5*4*3*2*1
    # 6! = 6*5*4*3*2*1
    # 100! = 100//5 + 100//5*5
    count = 0
    i = 5
    while (n//i)!=0:
        count += int(n/i)
        i = i * 5
    return count

if __name__ == '__main__':

    number = int(input("Enter a number for factorial: \n"))

    print("Factorial: {}".format(factorial(number)))
    print("Trailing zeroes: {}".format(factorial_trailing_zeroes(number)))



