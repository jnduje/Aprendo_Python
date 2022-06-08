def run():

    num_students = int (input("Ingrese el total de alumnos: "))   
    nested_list = []
    for i in range(int(num_students)):
        name = input("Ingrese el nombre: ")
        score = float(input("ingrese score: "))
        #nested_list.append([name, score])
        nested_list.append([score, name])
    
    nested_list.sort(reverse=False)
    # min_student = nested_list[0]
    # min_score = min_student[0]

    min_score = nested_list [0][0]
    print(nested_list)
    print(min_score)

    count = 0
    for student in nested_list:
        if student[0] == min_score:
            count += 1

    second_lowest_score = nested_list[count][0] # accedo a la sublista count y su índice 0
    
    print(count)
    print (second_lowest_score)
   
    # for student in nested_list:
    #     if student[0] == second_lowest_score:
    #         print(student[1])
 
    names = []
    names = [name for score, name in nested_list if score == second_lowest_score]

    print ('\n'.join([name for score, name in nested_list if score == second_lowest_score]))



if __name__ == '__main__':
    run()
