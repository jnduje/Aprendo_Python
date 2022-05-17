#Programa de ejemplo para saber como tratar con excepciones y asi
#evitar tener bugs en el programa. 
#Se utiliza try y except.

def divide_elementos_de_lista (lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e) #e es el error
        return lista #Si se genera el error devuelve la lista como esta


lista = list(range(10))
divisor = 0 #Todo numero divido por cero genera un ZeroDivisionError
#divisor = 3 -> si divisor no es cero el programa no genera error

print(divide_elementos_de_lista(lista, divisor))
