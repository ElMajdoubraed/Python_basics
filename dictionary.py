# How to create dictionary
dict1 = {
    'name': 'Raed',
    'email': 'raed.elmajdoub@gmail.com',
    'age':21
}

print(type(dict1))

# How to acces item in dictionary via keys
print(dict1['age'])

# loop through keys using keys() function
for i in dict1.keys():
    print(1)

# loop through values using values() function
for j in dict1.values():
    print(j)

# loop through items using items() function
for i, j in dict1.items():
    print(i , j)

# How to add item in dictionay
dict1['coding'] = 'python'
print(dict1)

# add  item using setDefault()

dict1.setdefault('city', 'kelibia')
print(dict1)
# get keys and store them in list

keysList = list(dict1.keys())
print(keysList)

# list of user - each user type is dictionary

dict2 = [
    {
        'name': 'mohamed',
        'email': 'mohamed@test.com',
    },
    {
        'name': 'saleh',
        'email': 'saleh@test.com',
    },
    {
        'name': 'ahmed',
        'email': 'ahmed@test.com',
    },
    {
        'name':'ali',
        'email':'ali@test.com',
        'age':32,
        'coding':['python','java','javaScript',{'reactjs','vuejs','nodejs'}]
    }

]

#print(dict2)
#print(dict2[0])
print(dict2[3]['coding'][3])
