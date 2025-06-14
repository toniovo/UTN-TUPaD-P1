# TP7 – Recursividad – Programación I

# 1) Factorial de números entre 1 y n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def ejercicio_1():
    numero = int(input("Ejercicio 1 – Ingresá un número: "))
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Serie de Fibonacci hasta una posición
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def ejercicio_2():
    posicion = int(input("Ejercicio 2 – Ingresá una posición para la serie de Fibonacci: "))
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3) Potencia con recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def ejercicio_3():
    b = int(input("Ejercicio 3 – Base: "))
    e = int(input("Exponente: "))
    print(f"{b}^{e} = {potencia(b, e)}")

# 4) Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio_4():
    numero = int(input("Ejercicio 4 – Ingresá un número decimal: "))
    if numero == 0:
        print("Binario: 0")
    else:
        print(f"Binario: {decimal_a_binario(numero)}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def ejercicio_5():
    texto = input("Ejercicio 5 – Ingresá una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(texto):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

# 6) Suma de dígitos sin strings
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def ejercicio_6():
    numero = int(input("Ejercicio 6 – Ingresá un número entero: "))
    print(f"Suma de dígitos: {suma_digitos(numero)}")

# 7) Contar bloques en pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def ejercicio_7():
    niveles = int(input("Ejercicio 7 – Bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# 8) Contar dígito dentro de un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

def ejercicio_8():
    numero = int(input("Ejercicio 8 – Número: "))
    digito = int(input("Dígito a contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")

# --- MENÚ PRINCIPAL PARA PROBAR LOS EJERCICIOS ---
def menu():
    while True:
        print("\n--- TP7 Recursividad – Elegí un ejercicio (1 a 8) o 0 para salir ---")
        opcion = input("Ejercicio: ")
        if opcion == "0":
            break
        elif opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        else:
            print("Opción inválida.")

# Ejecutar menú
menu()