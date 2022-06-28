
class Millas:
    def __init__(self):
        self._distancia = 0

    @property
    def obtener_distancia(self):
        print("Llamada al metodo getter")
        return self._distancia
    
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al metodo setter")
        self._distancia = valor


if __name__ == "__main__":
    avion = Millas()
    avion.definir_distancia = 200
    print(avion.definir_distancia)