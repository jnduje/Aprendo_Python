def read():
    numbers = []
    with open("./archivos/numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)
 
def write():
    names = ['Otro', 'Nico', 'Pepe', 'Carlos', 'Rocío']
    with open ("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')
    

def run():
    #read()
    write()
    



if __name__ == '__main__':
    run()
