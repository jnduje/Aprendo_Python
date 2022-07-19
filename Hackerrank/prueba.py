
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

    num = int(input())

    # Octal oct(num)
    # Binario bin(num)
    # Hexadecimal hex(num)   
    
    

   