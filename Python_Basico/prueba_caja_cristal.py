import unittest

#Estas pruebas asumen que ya hay codigo escrito
#Por eso primero creo el codigo para tener un ejemplo y
#luego la clase. 

def es_mayor_de_edad (edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest (unittest.TestCase):
#Primer camino que puede tomar una edad (si es mayor)
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)

#Creo otro test para corrobar el segundo camino (si es menor)
    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()