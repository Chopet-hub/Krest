print("Приветсвую в игре 'Крестики-нолики'!")

box = [1, 2, 3, 4, 5, 6, 7, 8, 9] # поле для игры
box_size = 3 # количество игровых клеток по вертикали/горизонтали

def play_box(): # Игровое поле
    print("-" * 6 * box_size)
    for i in range(box_size):
        print("|", end="")
        print((" " * 5 + "|")*3)
        print("|", box[i*3]," ", "|", box[1 +i*3], " ", "|", box[2 +i*3], " " * 2 + "|")
        print(("|" + 5 * "_")*3 + "|")

def victory_condition(): #Условие победы
    win = False

    combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # Комбинации победы

    for position in combination:
        if (box[position[0]] == box[position[1]] and box[position[1]] == box[position[2]]):
            win = box[position[0]]



    return win

def game_step(manager, char): #Ход игрока
    if (manager > 9 or manager < 1 or box[manager - 1] in ("X", "O")):
        return False

    box[manager - 1] = char
    return True
def game():
    player = "X" # Игрок
    step = 1 # Шаг поле
    play_box()

    while (step<10) and (victory_condition() == False):
        manager = input("Ходит игрок " + player + ". Введите номер поля:")

        if game_step(int(manager), player):  # Если ход прошел успешно
            print("Ход выполнен")

            if (player == "X"): # Подмена игроков
                player = "O"
            else:
                player = "X"

            play_box()

            step += 1 # Номер хода

        else:
            print("Неправильный номер")
    if (step == 10):
        print("Ничья!")

    print("Победил " + victory_condition() + "!")




game()