def run():
    # dict = {}
    
    # for key in range (1,101):
    #     if i %3 != 0:
    #         dict[key] = key**3

#Reemplazo el códifo anterior con dict comprenhension
    dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print (dict)

    
if __name__ == '__main__':
    run()