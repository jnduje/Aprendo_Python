def run():
    my_list= [1, 'Hello', True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

# Esto es una lista de diccionarios
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "García"},
    ]

# Esto es un diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 4, 5],
        "floatingn_nums": [1.1, 4.5, 6.43]
    }

# Imprimo el super diccionario
    # for key, value in super_dict.items():
    #     print(key, "-", value)

# Imprimo la super lista 
    for diccionario in super_list:
        for key, value in diccionario.items():
            print (key, "-", value)



if __name__ == '__main__':
    run()