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
    
    # count = 0  
    # for value_b in d['B']:
    #     for index, value_a in enumerate(d['A']):
    #         if value_b == value_a:
    #             print_index = index + 1
    #             print(print_index, end=" ")
    #             count += 1
            
    #     if count == 0:
    #         print("-1")
    #     else:
    #         count = 0
    #     print()

    for value_b in d['B']:
        if d['A'].count(value_b) != 0:

            for index, value_a in enumerate(d['A']):
                if value_b == value_a:
                    print(index + 1, end=" ")                
        else:
            print("-1")
        print()

   

if __name__ == '__main__':
    run()
    