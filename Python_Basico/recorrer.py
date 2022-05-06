def run():
    # frase = input('Escribe una frase: ')
    # for caracter in frase: 

    for i in range(20):
        print ("estoy en el for " + str(i))
        if i > 10:
            print ("estoy dentro del if" + str(i))
            continue
        else:
            print ('estoy dentro del else' + str(i))
        


if __name__ == "__main__":
    run()