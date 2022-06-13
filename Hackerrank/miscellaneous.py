def run():
    N = int(input("Ingrese la cantidad de comandos: "))
    list = []
      
    for i in range(N):
        print(f"comando N°: {i + 1}")
        comand, *rest = input().split()


        # try:
        #     index = int(rest[0])
        #     integer = int(rest[1])
            
        # except IndexError:
        #     integer = int(rest[0]) 

        if comand == 'insert':
            list.insert(index, integer)
        elif comand == 'print':
            print(list)
        elif comand == 'remove':
            list.remove(integer)
        elif comand == 'append':
            list.append(integer)
        elif comand == 'sort':
            list.sort()
        elif comand == 'pop':
            list.pop()
        elif comand == 'reverse':
            list.reverse()
        

    
if __name__ == '__main__':
    run()