def run():
    print('Ingrese el numero')
    n = int(input())
    
    for i in range(0, n):
        resultado = i ** 2
        print (str(resultado))
    

if __name__ == '__main__':
    run()
