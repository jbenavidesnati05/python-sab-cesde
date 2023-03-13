person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

print(person)

person['twiter'] = 'nicobytes'
print(person)

person['name'] = 'felipe'
print(person)

person.pop('age')
print(person)

print('keys')
print(person.keys())

print('values')
print(person.values())