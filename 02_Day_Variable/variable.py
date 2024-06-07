# Variables in Python

first_name = 'Rifki'
last_name = 'Maulana'
country = 'Indonesia'
city = 'Surakarta'
age = 19
person_info = {
    'firstname':'Rifki', 
    'lastname':'Maulana', 
    'country':'Indonesia',
    'city':'Surakarta'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age = 'Rifki', 'Maulana', 'Indonesia', 19

print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)