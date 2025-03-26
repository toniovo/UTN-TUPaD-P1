# 1)
print("Hola Mundo!")

# 2)
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "!")

# 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print("Soy", nombre, apellido, ", tengo", edad, "años y vivo en", lugar, ".")

# 4)
radio = int(input("Ingrese el radio: "))
area = 3.14 * radio ** 2
perimetro = 3.14 * radio * 2
print("El radio es:", round(radio), "y el perimetro es:", round(perimetro))

# 5)
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(segundos, "segundos equivalen a", round(horas), "horas.")

# 6)
tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(tabla, "x", i, "=", tabla * i)

# 7)
num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

# 8)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("Su Indice de Masa Corporal es", round(imc))

# 9)
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(temp_celsius, "°C equivalen a", round(temp_fahrenheit), "°F.")

# 10)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio de los tres números ingresados es", round(promedio))
