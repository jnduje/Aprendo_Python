import random

def read_word():
    list_words = []
    with open ('./archivos/data.txt', 'r', encoding= 'utf-8') as f:
        for word in f:
            word = word.strip('\n')
            list_words.append(word)
         
    return random.choice(list_words)


def word_to_list(word):
    result = word.upper()
    

    
    

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
    caracter = input("Ingrese un caracter: ")
    secret_word = read_word()
    print(secret_word)
    print(word_to_list(secret_word))
   # print_result(secret_word, caracter)

if __name__ == '__main__':
    run()
