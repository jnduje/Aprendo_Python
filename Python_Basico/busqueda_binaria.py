def run():
    print('Calculo de la raiz cuadrada')
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01 #Acá elijo los decimales de aproximación 
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    
    print(f'La raiz cuadrada de {objetivo} es: {respuesta}')

if __name__ == '__main__':
    run()
