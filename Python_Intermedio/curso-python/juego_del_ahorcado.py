import random
import os

def read_word():
    list_words = []
    with open ('./archivos/data.txt', 'r', encoding= 'utf-8') as f:
        for word in f:
            word = word.strip('\n')
            word = word.upper()
            list_words.append(word)
    return random.choice(list_words)

# def secret_word_to_list(word):
#     secret_list = []
#     for c in word:
#         secret_list = secret_list.append(c)
#     return secret_list



# def print_result (word, caracter):
#     result = ""
#     for i in word:
#         result += "_ "
        
#     # for index, caracter in enumerate (word):
#     #     print(index)
#     #     print("  ")
#     #     print(caracter)
#     for i in word:
#     #     if caracter == "_":

#     #         result += i
#     #     else:
#     #         result += "_"
    
#     # print("resultado")
#     print(result)
    
    return result


def run():
    
    secret_word = read_word()
    chosen_word_list = [letter for letter in secret_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    
    #print(secret_word)
    #input("Ayuda para crear el programa")

    while True:
        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        caracter = input("Ingrese una letra: ")
        assert caracter.isalpha(), "Solo puedes ingresar letras"

        count = 0
        for c in chosen_word_list:
            if caracter.upper() == c:
                chosen_word_list_underscores[count] = c
            count += 1
        
        if "_" not in chosen_word_list_underscores:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era", secret_word)
            break
    

if __name__ == '__main__':
    run()
