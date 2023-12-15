def victory_game():
    import random

    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                    'Сергей Александрович Есенин': '03.10.1895'}

    rounds = int(input('Сколько раз вы хотите играть?:'))
    for i in range (rounds):
        name,date = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился {name}')
        if answer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')