persona ={
    'nombre'    :'nico',
    'apellido'  :'molina',
    'stack'     :['pyhon','js'],
    'edad'      : 23
}
print(persona)

persona['nombre'] = "santi"
print(persona)

persona['edad'] = persona['edad'] + 10
print(persona)

persona['stack'].append('php')
print(persona)

del persona['apellido']
print(persona)

persona.pop('edad')
print(persona)

print('items')
print(persona.items())

print('keys')
print(persona.keys())

print('values')
print(persona.values())
