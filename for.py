# for element in range(1,21):
#     print(element)


# lista =[1,2,4,5,6,7]

# for element in lista:
#     print(element)

producto = {
    "nombre"    :"camisa",
    "precio"    : 100,
    "stock"     : 20
}    

print(producto)

# for key in producto:
#     print(key, "=>", producto[key])

for key, value in producto.items():
    print(key, '=>', value)