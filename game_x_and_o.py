field = [[" "]*3 for i in range(3)]

def show():
    print(f"   | 0 | 1 | 2 |")
    print(f" ---------------")
    for i in range(3):
        row_info = f" {i} | {' | '.join(field[i])} | "
        print(row_info)
        print(f" ---------------")

def ask():
    while True:
        cords = input("       Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты!")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клета занята! ")
            continue

        return x, y
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print(" Ходят крестик ")
    else:
        print(" Ходят нолик ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if num == 9:
        print(" Ничья! ")
        break