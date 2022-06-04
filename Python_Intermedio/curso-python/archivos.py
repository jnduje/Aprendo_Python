def read():
    numbers = []
    with open("./archivos/numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)
 
def write():
    names = ['Facundo', 'Nico', 'Pepe', 'Carlos', 'Rocío']
    with open ("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.writ(name)
            f.write('\n')
    print("estoy dentro de write")


def run():
    read()
    # write()
    print("estoy en run")



if '__name__' == '__main__':
    run()