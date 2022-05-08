def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_diccionario)

    print(mi_diccionario['llave1'])


    for llaves in mi_diccionario.keys():
        print(llaves)


if __name__ == '__main__':
    run()