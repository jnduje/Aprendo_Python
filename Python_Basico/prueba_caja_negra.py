import unittest

def suma(num_1, num_2):
    return num_1 + num_2

#Primero genero la clase que hace el test. 

class caja_negra(unittest.TestCase):

#Luego genero el test para sumar y por ultimo la funcion
#suma con sus parametros y el return
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

#Ahora genero otro test para sumar numeros negativos
    def test_suma_dos_negativos (self):
        num_1 = -10 #numeros que va a usar el test
        num_2 = -7 # y se van a pasar como parametros 
    
        resultado = suma (num_1, num_2)

        self.assertEqual(resultado, -17)


        
if __name__ == '__main__':
    unittest.main()