# Создайте программу для игры в "Крестики-нолики".

# игровое поле
field = [1,2,3,
         4,5,6,
         7,8,9]
 
# определяем победные комбинации
wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
 
# вывод игрового поля
def print_field():
    print(field[0], end=' ')
    print(field[1], end=' ')
    print(field[2])
    print(field[3], end=' ')
    print(field[4], end=' ')
    print(field[5])
    print(field[6], end=' ')
    print(field[7], end=' ')
    print(field[8])

# делаем ход в ячейку поля
def step_field(step, symbol):
    ind = field.index(step)
    field[ind] = symbol
 
# получить текущий результат игры
def checkwin():
    win = ''

    for i in wins:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            win = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            win = 'O'   
    return win
 
# поиск линии ИИ с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
 
    step = ''
    for line in wins:
        o = 0
        x = 0
 
        for j in range(0,3):
            if field[line[j]] == 'O':
                o = o + 1
            if field[line[j]] == 'X':
                x = x + 1
 
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if field[line[j]] != 'O' and field[line[j]] != 'X':
                    step = field[line[j]]
    return step
 
# выбор хода ИИ
def bot_move():        
 
    step = ''
 
    # ходит, если на какой либо из победных линий 2 свои фигуры и 0 чужих
    step = check_line(2, 0)
 
    # ходит, если на какой либо из победных линий 2 чужие фигуры и 0 своих
    if step == '':
        step = check_line(0, 2)        
 
    # ходит, если 1 фигура своя и 0 чужих
    if step == '':
        step = check_line(1, 0)           
 
    # центр пуст, занимаем центр
    if step == '':
        if field[4] != 'X' and field[4] != 'O':
            step = 5           
 
    # если центр занят, то занимает первую ячейку
    if step == '':
        if field[0] != 'X' and field[0] != 'O':
            step = 1           

    return step
 
def main():
    game_over = False
    player = True
    
    while game_over == False:
    
        # показываем поле
        print_field()
    
        # ход игрока
        if player == True:
            symbol = 'X'
            step = int(input('Ваш ход: '))
        else:
            # ход бота
            print('Компьютер делает ход: ')
            symbol = 'O'
            step = bot_move()
    
        # если бот нашел куда сделать ход, то играем, если нет, то конец игры
        if step != '':
            step_field(step, symbol)
            # определим, есть ли победитель
            win = checkwin()
            if win != '':
                game_over = True
            else:
                game_over = False
        else:
            game_over = True
            win = 'Ничья'
    
        player = not(player)        
    
    # игра окончена, вывод результатов
    print_field()
    if win == 'Ничья':
        print('Ничья!')
    else:
        print('Победил', 'Компьютер' if win=='O' else 'Человек')

if __name__ == '__main__':
    main()