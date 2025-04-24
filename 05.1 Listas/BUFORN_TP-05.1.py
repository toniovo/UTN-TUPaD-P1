# 1)
multiplos_de_4 = list(range(4, 101, 4))
print("Múltiplos de 4:", multiplos_de_4)

# 2)
gustos = ["pizza", "helado", "videojuegos", "guitarra", "fútbol"]
print("Penúltimo elemento:", gustos[-2])

# 3)
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Lista con append:", lista_vacia)

# 4)
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista animales modificada:", animales)

# 5)
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# 6)
numeros = list(range(10, 31, 5))
print("Primeros dos números:", numeros[:2])

# 7)
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mustang", "camaro"]
print("Lista autos modificada:", autos)

# 8)
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista dobles:", dobles)

# 9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista compras modificada:", compras)

# 10)
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Lista anidada:", lista_anidada)
