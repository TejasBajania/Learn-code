# Avg Length Of Word
# str_input = "I am Prakash Parikh"
# # output = 4.0

# word_len = []

# for words in str_input.split(' '):

#     word_len.append(len(words))

# print(sum(word_len)/len(str_input.split(' ')))

# list1 = [1, 4, 10, 9, 5]
# # Find Maximum and Second Maximum Number without using any default functions.
# # output = 10,9

# for ind1 in range(len(list1)):

#     for ind2 in range(len(list1)):

#         if list1[ind2] > list1[ind1]:

#             list1[ind1], list1[ind2] = list1[ind2], list1[ind1]

#         else:
#             continue

# print(list1[-1],list1[-2])




employees = [{"Name": "Ravi", "Salary": "30000","Location": "Mumbai"},
     {"Name": "Santhosh", "Salary": "20000","Location": "Bangalore"},
     {"Name": "Anu", "Salary": "40000","Location": "Mumbai"},
     {"Name": "Raju", "Salary": "35000","Location": "Bangalore"},
     {"Name": "Sita", "Salary": "25000","Location": "Delhi"}]

""" Minimum, Maximum and Average Salary of each location"""



# Output : Mumbai: 30000,40000, 35000
location_data = {}

for emp in employees:


    if emp['Location'] not in location_data.keys():

        location_data[emp['Location']] = []
    
    location_data[emp['Location']].append(int(emp['Salary']))

location_name = 'Mumbai'

print(location_data)
print(min(location_data[location_name]),max(location_data[location_name]),sum(location_data[location_name])/len(location_data[location_name]))



'\n \n'

'\\n \\n'

