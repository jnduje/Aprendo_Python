def run():
    # N = int(input("Ingrese la cantidad de comandos: "))
    # list = []
      
    # for i in range(N):
    #     print(f"comando N°: {i + 1}")
    #     comand, *rest = input().split()

    #     if len(rest) == 0:
    #         if comand == 'print':
    #             print(list)
    #         elif comand == 'sort':
    #             list.sort()
    #         elif comand == 'pop':
    #             list.pop()
    #         elif comand == 'reverse':
    #             list.reverse()
    #     elif len(rest) == 1:
    #         integer = int(rest[0]) 

    #         if comand == 'remove':
    #             list.remove(integer)
    #         elif comand == 'append':
    #             list.append(integer)
    #     elif len(rest) == 2:
    #         index = int(rest[0])
    #         integer = int(rest[1])
            
    #         if comand == 'insert':
    #             list.insert(index, integer)

 #  - RESUELVO SEGÚN ELEJEMPLO QUE DIO OTRO ALUMNO DE HackerRank -       
    
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:] # Si leo la lista de esta forma no me da error al tener 1 solo elemento 
       
        print(cmd)
        print (args) 

        if cmd !="print":
            cmd += "("+ ",".join(args) +")" #join une el iterable con el separador especificado "," y lo transforma string
            eval("l."+cmd)      #eval evalúa un string y si es una función de Python la ejecuta.
        else:
            print (l)
          

    
if __name__ == '__main__':
    run()