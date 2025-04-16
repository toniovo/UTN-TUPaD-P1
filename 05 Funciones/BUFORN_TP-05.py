# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido + ", tengo", edad, "años y vivo en", residencia)

# 4
def calcular_area_circulo(radio):
    return 3.14 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

# 5
def segundos_a_horas(segundos):
    return segundos / 3600

# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

# 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal

# 1
imprimir_hola_mundo()

# 2
nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))

# 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("Ingresá el radio de un círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

# 5
segundos = int(input("Ingresá una cantidad de segundos: "))
print("Equivale a", segundos_a_horas(segundos), "horas")

# 6
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print("Suma:", suma, "Resta:", resta, "Multiplicación:", mult, "División:", div)

# 8
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = calcular_imc(peso, altura)
print("Tu IMC es:", imc)

# 9
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(celsius, "°C equivale a", fahrenheit, "°F")

# 10
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
print("Promedio:", calcular_promedio(n1, n2, n3))
