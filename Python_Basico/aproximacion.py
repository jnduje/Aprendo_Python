def run():
    print('Calculo de la raiz cuadrada')
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01 #Acá elijo los decimales de aproximación 
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print('No se encontro la raiz cuadrada de ' + str(objetivo))
    else:
        print('La raiz cuadrada de ' + str(objetivo) + ' es ' + str(respuesta))
    

if __name__ == '__main__':
    run()
