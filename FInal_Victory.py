def game():

from Victory import victory_game

print('Добро пожаловатьт в игру Викторина')
name = input('Как тебя зовут?:')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    victory_game()
elif answer == 'Нет':
    print(('Ну давай готовься тогда)'))
else:
    print('Не могу понять, что ты хочешь от меня)')