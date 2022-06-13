from collections import namedtuple

def run():
    
    print("Ingrese la cantidad de alumnos: ")
    N = int(input())
    print("Ingrese los nombres de columnas: ")
    columns = input().split() 
    spreadsheet = namedtuple('spreadsheet', columns)
    
    sum = 0
    for i in range(N):
        c1, c2, c3, c4 = input().split()
        student = spreadsheet(c1, c2, c3, c4)
        sum += int(student.MARKS)

    average = float(sum/N)

    print("El promedio es: " + "{:.2f}".format(average))    
   

if __name__ == '__main__':
    run()
    