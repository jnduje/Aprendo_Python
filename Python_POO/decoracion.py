
def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje ...")
        funcion()
        print("Este es el primer mensaje ;")
    return wrapper

def zumbido():
    print("Buzzzzzz")

if __name__ == "__main__":
    
    zumbido = funcion_decoradora(zumbido)
    zumbido()
    