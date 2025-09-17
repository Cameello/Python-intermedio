#Calcular el mayor de dos números ingresados por teclado usando un operador ternario
 #Buscar una palabra en una lista ingresada por teclado usando args y un operado ternario
 #Determinar si un número es par o impar
 #Calcular el promedio de una lista de números usando args y un operador ternario
 #Imprimir un mensaje de error si no se pasan suficientes argumentos

def mensaje_error(funcion):
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            return "Error: No se pasaron suficientes argumentos."
        return funcion(*args, **kwargs)
    return wrapper

def mayor_numero():
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
    except ValueError:
        return "Error: Debe ingresar números enteros."

    mayor = numero1 if numero1 > numero2 else numero2
    return f"El número mayor es: {mayor}"
 
@mensaje_error
def buscar_palabra(*args):
    palabra = input("Ingrese la palabra a buscar: ")

    if len(args) > 1:
        return "Error: Solo se debe pasar 1 argumento"

    lista_input = input("Ingrese la lista de palabras separadas por comas: ")
    lista = [p.strip() for p in lista_input.split(",")]

    return f'La palabra "{palabra}" {"se encuentra" if palabra in lista else "no se encuentra"} en la lista.'


        
@mensaje_error
def par_impar(a):
    return f'El número {a} es {"par" if a % 2 == 0 else "impar"}.'


@mensaje_error
def promedio(*args):
  return f"El promedio es {sum(args)/len(args) if args else 'Error: no se pasaron números'}"


print(mayor_numero())
print(buscar_palabra(1))
print(par_impar(7))
print(promedio(3, 4, 5))