# CRUD 
numbers = [1,2,3,4,5,6,7,8,9]
tasks = ["lavar", "jugar","comer"]


print(numbers[0])

numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0,"hola")
print(numbers)
numbers.insert(-1,"hola")
print(numbers)

newList = numbers + tasks
print(newList)

index = newList.index("jugar")
print(index)
newList[index] = "dormir"
print(newList)

newList.remove("dormir")
print(newList)

newList.pop()
print(newList)

newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numbers2 = [1,2,56,23,14,65,6,787,8,99]
numbers2.sort()
print(numbers2)