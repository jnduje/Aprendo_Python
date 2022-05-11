def run():
    n = int(input('Ingrese un número: '))
    potencia = n - 1
    num = 0

    for i in range (1, n + 1):
        num_aux = i * (10**potencia)
        num = num + num_aux
        potencia = potencia - 1


    print(str(num))
           

if __name__ == '__main__':
    run()
