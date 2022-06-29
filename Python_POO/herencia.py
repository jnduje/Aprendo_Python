
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

#Defino la Sub Clase (o clase hijo)
class Cuadrado(Rectangulo): #Llamo a la super clase
    def __init__(self, lado):
        super().__init__(lado, lado) 

# Super() es una función que permite obtener una referencia directa de la superclase.

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
    


