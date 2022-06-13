def run():
    N = int(input())
    list = []

    for i in range(N):
        index, value = input().split()

        list.insert(int(index), int(value))
    print(list)

if __name__ == '__main__':
    run()