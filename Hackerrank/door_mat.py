
def header(rows, columns):
    text = '.|.'
   
    for i in range(rows):
        j = 1 + (2*i)
        print_text = text * j
        print (print_text.center(columns,'-'))
  
def center(columns):
    print ('WELCOME'.center(columns,'-'))
    
def footer(rows, columns):
    text = '.|.'
    
    for i in range(rows):
        j = (rows*2) - (1 + (2*i))
        print_text = text * j
        print (print_text.center(columns,'-'))
       

if __name__ == '__main__':

    introduction = '''
    Se debe ingresar primero la cantidad de filas, un espacio y la cantidad de columnas. 
    Las columnas tienen que ser un múltiplo de las filas. 
    Ejemplo: 
            7 21
            11 33
            22 66
    '''
    print(introduction)
    s = input().split()
    rows = int(s[0])
    columns = int(s[1])
      
    rows_sides = int (rows//2)
    header(rows_sides, columns)
    center(columns)
    footer(rows_sides, columns)
    
    

   