# The provided code stub will read in a dictionary containing key/value pairs of name:
# [marks] for a list of students. Print the average of the marks array for the student
# name provided, showing 2 places after the decimal

#import numpy

def run():
    n = int(input("Ingrese la cantidad de estudiantes: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Ingrese datos separados por un espacio: ").split()
        scores = list(map(float, line)) # Hace una lista con el "mapa" de los números flotantes en la lista line
        student_marks[name] = scores
    
    query_name = input("Ingrese el nombre del alumno: ")

    #mean = numpy.average(student_marks[query_name])

    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print ("{:.2f}".format(average))



if __name__ == '__main__':
    run()
    