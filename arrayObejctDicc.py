personas = [
    {
       "nombre" : "jorge",
       "edad"   : 34 
    },
    {
       "nombre" : "juan",
       "edad"   : 56 
    },
    {
       "nombre" : "daniela",
       "edad"   : 28 
    },
]

print(personas)

for persona in personas:
    print(persona)

for persona in personas:
    print("nombre =>", persona["nombre"])
    print("edad =>", persona["edad"])