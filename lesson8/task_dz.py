my_dict = {}
my_dict.update(name='John')
my_dict.update(age=25)
my_dict.update(city='New York')
print(my_dict)
my_dict['age'] = 26
my_dict.update(email='john@example.com')
if not 'country' in my_dict:
    print('Ключ "country" в словаре отсутствует')

del my_dict['city']
for key, value in my_dict.items():
    print(f'Ключ: {key}, Значение: {value}')