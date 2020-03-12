x = 1

def run(x):
    while x != 3:
        for i in range(8):
            print(i)
            if i == 6:
                x += 1
                break
        if x == 3:
            print(x)

run(x)