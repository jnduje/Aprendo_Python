if __name__ == '__main__':
    n = int(input())
    # arr = map(int, input().split())

    # score_list = list(arr)
    # winner = max(score_list)
    # runner_up = min(score_list)

    # for i in range (n):
    #     print (f'{score_list[i]}')
    #     if score_list[i] > runner_up and score_list[i] != winner:
    #         runner_up = score_list[i] 
    # print(f'El subcambepon es: {runner_up}')

    #-- EJERCICIO RESUELTO POR OTRO ESTUDIANTE DE HACKERRANCK --
    # Ordena la lista con sorted y reverse=True de mayor a menor
    

    arr = sorted(map(int, input().split()), reverse=True)
    print(arr[arr.count(arr[0])]) 

    # Primero cuenta cuantas veces se repite el numero mayor que al estar ordenado se encuentra en el primer lugar 
    # 
    # arr.count(arr[0])
    #
    # Luego imprime el valor que se encuentra en el indice que devuelve el conteo. Este valor va a ser el siguiente después del numero mayor. 
    # Ejemplo: si el numero mayor es 8 y se repite 3 veces, el siguiente va a ser el numero buscado.
    #
    # arr[arr.count(arr[0])] 
    # arr[arr.count(8)]
    # arr [3]
    #
    # numero buscado