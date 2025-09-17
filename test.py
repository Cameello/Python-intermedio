def agregar_mensaje(mensaje):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            return mensaje + resultado
        return wrapper
    return decorador


@agregar_mensaje("Hola, ")

def nombre():
    return "Martín"

print(nombre())  # "Hola, Martín"