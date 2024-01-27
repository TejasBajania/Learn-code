with open('E:\Code learning\Learn-code\Basic_codes\curreny_data.txt') as f:

    lines = f.readlines()

curren_dict = {}
for line in lines:
    parsed = line.split('\t')
    print(parsed)
    curren_dict[parsed[0]] = parsed[1]

print(curren_dict)
amount = int(input("Enter amount \n"))
print('Enter name of currency you want to convert this amount to?')
[print(item) for item in curren_dict.keys()]

currency = input('Please enter any one of these \n')   

print(f'{amount} INR is equal to {amount*float(curren_dict[currency])} {currency}')




