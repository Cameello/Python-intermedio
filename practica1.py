# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima elconjunto de los elementos que se encuentran en A o en B, pero no en ambos.
# Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
# Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

def union_conjuntos(a, b):

    return a | b

def interseccion_conjuntos(a,b):

    return a & b

def diferencia_simetrica(a,b):

    return a.symmetric_difference(b)

def es_subconjunto(a,b):

    return a.issubset(b)

def numero_elementos(a):

    return len(a)

print("Elementos en A o en B, o en ambos:", union_conjuntos(A, B))
print("Elementos en A y en B:", interseccion_conjuntos(A, B))
print("Elementos en A o en B, pero no en ambos:", diferencia_simetrica(A, B))
print("El conjunto A es un subconjunto de otro conjunto, B.?:", es_subconjunto(A, B))
print("El número de elementos del conjunto es:", numero_elementos(A))

