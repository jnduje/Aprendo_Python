import matplotlib.pyplot as plt

x= ['aa','bb', 'cc']
y= [100, 200, 30]


def generate_char (labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values, width=0.4, color="orange")
   # plt.show
    plt.savefig('grafico2.png')
    plt.close()

if __name__ == "__main__":
    generate_char(x, y)