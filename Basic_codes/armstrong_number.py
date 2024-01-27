def armstrong_number_check(number):

    if number < 0:
        print('Please enter valid number')
        return 
    order = len(str(number))
    armstrong = 0
    curr_number = number
    
    while number > 0:

        digit = number % 10
        armstrong = armstrong + digit ** order 
        number = number // 10

    if curr_number == armstrong:

        print("It's an armstrong")
    
    else:

        print("Not an armstrong")

number = int(input('Enter a number for arm strong check: \n')) 

armstrong_number_check(number)
        