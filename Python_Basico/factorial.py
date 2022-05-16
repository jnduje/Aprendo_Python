def factorial(n):
    """
    Calcula el facatorial de n.

    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factorial (n-1)

numero = int(input('Escribe un entero: '))
print (factorial(numero))

