"""" Program which will keep on adding a stream of numbers inputted by the user. The adding stops as soon as a user presses 'enter' or 'q'"""

sum = 0
count = 0
it_details = [] 

while(True):

    user_input = input("Enter the price \n Or press 'q' to quit \n")

    if user_input != 'q':

        sum = sum+int(user_input)
        count= count + 1
        it_details.append({count:user_input})

    else:
        print('\n --- Your Bill summary ---')
        for ke_val in it_details:
            print('\n {}. price:- {} rs'.format(list(ke_val.keys())[0],list(ke_val.keys())[0]))
        print('\n Bill total is {}'.format(sum))
        print('\n Thanks for Shopping')
        break