
def print_formatted(n):

    row_with = len(bin(n)[2:])

    for i in range(0, n):
        i += 1
        str_dec = str(i)
        str_oct = str(oct(i))
        str_hex = hex(i)
        str_bin = bin(i)
       # print(f'{i} {str_oct[2:].rjust(row_with)} {str_hex[2:].upper().rjust(row_with)} {str_bin[2:].rjust(row_with)}')
        print(f'{str_dec.rjust(row_with)}', end = " ")
        print(f'{str_oct[2:].rjust(row_with)}', end = " ")
        print(f'{str_hex[2:].upper().rjust(row_with)}', end = " ")
        print(f'{str_bin[2:].rjust(row_with)}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    # Octal oct(num)
    # Binario bin(num)
    # Hexadecimal hex(num)   
    
    

   