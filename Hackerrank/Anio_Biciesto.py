def is_leap(anio):

    # div4 = anio % 4
    # div100 = anio % 100
    # div400 = anio % 400

    if anio % 4 == 0:
        if anio % 400 == 0:
            biciesto = True
        elif anio % 100 == 0:
            biciesto = False
        else:
            biciesto = True
    else:
        biciesto = False

    # if div4 == 0:
    #     if div400 == 0:
    #         biciesto = True
    #     elif div100 == 0:
    #         biciesto = False
    #     else:
    #         biciesto = True
    # else:
    #     biciesto = False


    # if anio % 4 == 0:
        # if anio % 100 == 0 and anio % 400 == 0:
        #     biciesto = True
        # else:
        #     biciesto = False
    #     biciesto = True    
    # else:
    #     biciesto = False

    return biciesto        

def run():
    year = int(input('Ingrese un resultado: '))
    print(is_leap(year))


if __name__ == '__main__':
    run()
