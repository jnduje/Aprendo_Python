
def print_rangoli(size):
    alphabet = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #with = ((size * 2)-1) + ((size * 2)-2)
    with_rangoli = (4*size) - 3
    list_aux = []

    # Imprimo primer línea
    str_aux = alphabet[size]
    print(str_aux.center(with_rangoli,"-"))

    # Imprimo primer recursiva
    for new_range in range(1, size-1):   
        breakpoint()  
        for i in range(1, new_range):
            list_aux.append(alphabet[size - i])
            

        # for i in range(, 1, -1):
        #     list_aux.append(alphabet[i])

            str_aux = "-".join(list_aux)
        print(str_aux.center(with_rangoli,"-"))


    # for i in range(size):
    #     list_aux.append(alphabet[size - i])
    # for i in range(size+1):
    #     list_aux.append(alphabet[i])
    # str_aux = "-".join(list_aux)
    # print(list_aux) 
    # print(str_aux)

    #print(alphabet[size-1].center(with_rangoli,"-"))
    #print(str_aux.center(with_rangoli,"-"))







if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)