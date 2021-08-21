print("Hello World\n")

# Listas (como los arrays para lenguajes como Java)
fruits = ["Apple","Orange","Watermelon"]
print(fruits[0]) #Apple
print(fruits[1]) #Orange
print(fruits[2]) #Watermelon
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

numbers = [0,1,2,3,4,5,6,7,8,9]
from_2_to_6 = numbers[2:7] #números del 2 al 7
print(from_2_to_6)
greater_than_4 = numbers[5:]
print(greater_than_4)
print(numbers[::2]) #obtener números pares de la lista
print(numbers[1::2]) #obtener números impares de la lista
print(4 in numbers) #indica que el nº 4 está en la lista (True)
print(10 in numbers) #indica que el nº 10 no está en la lista (False)

#-------------Diccionarios (es una colección de las claves con sus valores correspondientes)---------
#Nota: todo diccionario es un objeto
fighter = {"name": "Chuck", "lastname": "Norris", "technique": "Karate"}
print(fighter["name"]) #para acceder al valor de la clave (manera incorrecta)
print(fighter.get("nombre")) #devuelve None (que es el valor null)

# True, False, None ==> TRUE, FALSE Y NULL
print("\nFrutas de la función:")
def print_fruits(fruits_list): #sintáxis de como crear una función
	for fruit in fruits_list:
		print(fruit)

print_fruits(fruits) #para llamar a la función