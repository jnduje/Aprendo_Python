import matplotlib.pyplot as plt

def generate_char (labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
   # plt.show

    plt.savefig('grafico2.png')
    plt.close()
