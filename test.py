a = ["M","na","i","par"]
b = ["y","me","s","th"]
# # output = ['My', 'name', 'is', 'parth']
# output = []

# for ind1 in range(len(a)):

#     for ind in range(len(b)): 

#         if ind1 == ind:

#             output.append(f'{a[ind1]}{b[ind]}')

# print(output)


# a = ["M","na","i","par", "xyz",'def']
# b = ["y","me","s","th"]
# # output = ['My', 'name', 'is', 'parth', 'xyz','def']
# output = []

# for ind1 in range(len(a)):

#     if ind1 >= len(b):

#         output.append(f'{a[ind1]}')

#     for ind in range(len(b)): 

#         if ind1 == ind:

#             output.append(f'{a[ind1]}{b[ind]}')

# print(output)


# # Query String to Dict
# query = 'a=2&b=23&name=parth'
# # output = {'a':'2','b':'23','name':'parth'}

# output = {}

# for str_1 in query.split('&'):

#     output[str_1.split('=')[0]] = str_1.split('=')[1]

# print(output) 



# employees = [{"Name": "Ravi", "Salary": "30000","Location": "Mumbai"},
#      {"Name": "Santhosh", "Salary": "20000","Location": "Bangalore"},
#      {"Name": "Anu", "Salary": "40000","Location": "Mumbai"},
#      {"Name": "Raju", "Salary": "35000","Location": "Bangalore"},
#      {"Name": "Sita", "Salary": "25000","Location": "Delhi"}]

# """1) No of employees in each location
# 2) Minimum, Maximum and Average Salary of each location"""

# # {'NameOfCity':'NumberOfEmployees'}
# # {'Mumbai':'2'}

# NoOfEmployees = {}
# noOfCities = {}

# for emp in employees:

    

#     if emp['Location'] in noOfCities.keys():
#         noOfCities[emp['Location']]=noOfCities[emp['Location']]+1
#     else:
#         noOfCities[emp['Location']] = 0
# print(noOfCities)


# Find the highest and second highest number without using any default function
lis = [1, 4, 10, 9, 5]

for ind1 in range(len(lis)):

    for ind in range(len(lis)):

        if lis[ind] > lis[ind1]:

            lis[ind1],lis[ind] = lis[ind], lis[ind1]

        else:
            continue

print(lis[-1])
print(lis[-2])

