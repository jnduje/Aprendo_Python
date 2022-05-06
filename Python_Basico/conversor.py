menu = """
Bienvenido al conversor de monedas 💰

Ingrese la mondea del país: 

1 - Pesos colombianos
2 - Pesos argentinos 

"""

pais = int(input(menu))

if pais == 1:    
    pesos = input ("Ingrese la cantidad de pesos colombianos: ")
    pesos = int(pesos)
    cotizacion = 3700
    dolares = round ( float(pesos / cotizacion), 2 )
    dolares = str (dolares)
    print ("Tienes U$D " + dolares + " dolares")
elif pais == 2:
    pesos = input ("Ingrese la cantidad de pesos argentinos: ")
    pesos = int(pesos)
    cotizacion = 205
    dolares = round ( float(pesos / cotizacion), 2 )
    dolares = str (dolares)
    print ("Tienes U$D " + dolares + " dolares")
else:
    print ("País no soportado")

