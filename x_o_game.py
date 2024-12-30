# Размеры игрового поля
field_size = 3
# Игровое поле, пока что в виде пустого словаря
field = {}
# Заполнение словаря парами координаты-содержимое поля
for vertical in range(field_size):
    for horizontal in range(field_size):
         field[(vertical, horizontal)] = '-'
def output_of_the_field():
    '''Функция, которая будет отображать текущее состояние игрового поля в консоли'''
    print(' ', *range(field_size))
    for i in range(field_size):
        print(f'{i} {list(field.values())[i*3]} {list(field.values())[i*3+1]} {list(field.values())[i*3+2]}')

def check_end_game():
    '''Функция, которая будет проверять текущее состояние игрового поля и определять, завершилась ли игра'''
    # Поля вертикалей, горизонталей, диагоналей, в каждой из них по 3 поля
    vertical1 = list(filter(lambda x: x[0] == 0, list(field.keys())))
    vertical2 = list(filter(lambda x: x[0] == 1, list(field.keys())))
    vertical3 = list(filter(lambda x: x[0] == 2, list(field.keys())))
    horizontal1 = list(filter(lambda x: x[1] == 0, list(field.keys())))
    horizontal2 = list(filter(lambda x: x[1] == 1, list(field.keys())))
    horizontal3 = list(filter(lambda x: x[1] == 2, list(field.keys())))
    # Координаты полей первой диагонали равны
    diagonal1 = list(filter(lambda x: x[0] == x[1], list(field.keys())))
    # Сумма координат полей второй диагонали равна 2
    diagonal2 = list(filter(lambda x: x[0] + x[1] == 2, list(field.keys())))
    # Проверка на заполнение только крестиками или только ноликами
    for i in ("x", "o"):
        if any([field[vertical1[0]] == i and field[vertical1[1]] == i and field[vertical1[2]] == i,
                field[vertical2[0]] == i and field[vertical2[1]] == i and field[vertical2[2]] == i,
                field[vertical3[0]] == i and field[vertical3[1]] == i and field[vertical3[2]] == i,
                field[horizontal1[0]] == i and field[horizontal1[1]] == i and field[horizontal1[2]] == i,
                field[horizontal2[0]] == i and field[horizontal2[1]] == i and field[horizontal2[2]] == i,
                field[horizontal3[0]] == i and field[horizontal3[1]] == i and field[horizontal3[2]] == i,
                field[diagonal1[0]] == i and field[diagonal1[1]] == i and field[diagonal1[2]] == i,
                field[diagonal2[0]] == i and field[diagonal2[1]] == i and field[diagonal2[2]] == i]):
            return f'Игра завершилась победой игрока {i}.'
    if not '-' in field.values():
        return 'Игра завершилась вничью.'
    else:
        return False

# После завершения одной игры будет начинаться другая
while True:
    print("Добро пожаловать в Крестики-нолики!")
    # Вывод пустого игрового поля
    output_of_the_field()
    # Игроки
    players = ("x", "o")
    # Выполнение цикла действий до завершения игры
    while check_end_game() == False:
        # Реализация перехода хода от игрока и игроку
        for turning_player in players:
            # Выход из цикла при завершении игры
            if check_end_game() != False:
                break
            # Цикл для игрока, чтобы из него выйти, нужно ввести верные координаты
            while True:
                # Ввод координат игроком
                vertical = int(input(f"Ход игрока {turning_player}. Введите номер вертикали поля: "))
                horizontal = int(input("Введите номер горизонтали поля: "))
                # Проверка на корректность ввода координат
                if (vertical, horizontal) in field.keys() and field[(vertical, horizontal)] == '-':
                    # Обработка хода
                    field[(vertical, horizontal)] = turning_player
                    # Вывод поля в его новом состоянии
                    output_of_the_field()
                    break
                else:
                    print("Введены неверные координаты.")
    # Вывод итога игры
    print(check_end_game())
    # Создание нового игрового поля
    field_size = 3
    field = {}
    for i in range(field_size):
        for j in range(field_size):
            field[(j, i)] = '-'
