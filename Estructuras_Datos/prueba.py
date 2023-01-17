entra_a_funcion = 0
sale_de_funcion = 0

def pyramid_sum(lower, upper, margin=0):
    global entra_a_funcion
    global sale_de_funcion

    entra_a_funcion = entra_a_funcion + 1

    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        sale_de_funcion = sale_de_funcion + 1
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        sale_de_funcion =sale_de_funcion + 1
        return result

if __name__ == "__main__":
   _lower = int(input("Ingrese el numero lower: "))
   _upper = int(input("Ingrese el numero upper: "))

   pyramid_sum(_lower,_upper)
  


