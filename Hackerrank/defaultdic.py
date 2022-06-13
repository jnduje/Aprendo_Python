from collections import defaultdict

def run():
    d = defaultdict(list)
    print("Ingrese separado por un espacio la cantidad de valores de cada grupo: ")
    group_a, group_b = input().split()

    print("Ingrese los valores del grupo A: ") 
    for i in range(int(group_a)):
        d['A'].append(input()) 
    
    print("Ingrese los valores del grupo B: ")
    for i in range(int(group_b)):
        d['B'].append(input()) 
    
    for value_b in d['B']:
        if d['A'].count(value_b) != 0:

            for index, value_a in enumerate(d['A']):
                if value_b == value_a:
                    print(index + 1, end=" ")                
        else:
            print("-1", end="")
        print()

   

if __name__ == '__main__':
    run()
    