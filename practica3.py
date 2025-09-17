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
  return f"El promedio es {sum(args)/len(args) if args else 'Error: no se pasaron numeros'}"


print(mayor_numero())
print(buscar_palabra(1))
print(par_impar(7))
print(promedio(3, 4, 5))

#Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
#Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
#Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra uEsncrmensaje de error al usuario. 
#escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción  FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
#Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

def dividir():
    try:
        a = 10
        b = 0
        resultado = a / b
        print(f"El resultado de la division es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")

def sumar_numero_cadena():
    try:
        x = 10
        y = "5"
        resultado = x + y
        print(f"El resultado de la suma es: {resultado}")
    except TypeError:
        print("Error: No se puede sumar un numero con una cadena")

def acceso_diccionario():
    dic = {"a": 1, "b": 2}
    try:
        clave = "c"
        valor = dic[clave]
        print(f"El valor de la clave '{clave}' es {valor}")
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario")

def abrir_archivo():
    nombre_archivo = "archivo_ejemplo.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe, Se creara uno nuevo")
        with open(nombre_archivo, "w") as archivo:
            archivo.write("")

def dividir_valores():
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a / b
        print(f"El resultado de la division es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    except ValueError:
        print("Error: Debe ingresar números valid")
