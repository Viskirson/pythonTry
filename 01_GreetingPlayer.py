from typing import Union

# == Имя файла: 01_GreetingPlayer.py ==
# == Список переменных: ==
player_name : str = ''  # Имя игрока
player_class : str = ''  # Класс игрока
class_choices : list[str] = ["Маг","Воин","Разбойник"]  # Список классов игрока
class_explained : dict[str, str] = {class_choices[0]:"Этот класс силён в магических схватках. Но слаб в физическом плане.",
                                     class_choices[1]: "Этот класс силён в физических схватках. Но не ожидай от него великого волшебства.",
                                     class_choices[2]: '''Этот класс ловок и смышлён. Не так силён как воин, 
                                     но может увернуться от атаки и использовать хитрости.'''}  # Словарь с описанием классов

itemForChose : dict[str, dict[str, Union[str, int, float]]] = {# Словарь с предметами для выбора
    "banana": {
        "описание": '''
Самый обычный фрукт. Может немного помочь подлечиться. А если кинуть во врага, при определённом везении, нанесён урон''', 
        "количество": 4,
        "стоимость": 0.4,
        "именование": "Банан"
        },
    "luck_potion": {
        "описавние": '''
Из зназвания понятно, что это зелье принесёт тебе невиданную удачу. 
К примеру ты сможешь нанести двойной урон, увернуться от удара или повысить шанс в случайном собитии.
Полезная штука, да?''',
        "количество": 2,
        "стоимость": 2.0,
        "именование": "Зелье удачи"
        },
    "rock": {
        "описание": '''
Просто камень. Может пригодиться в будущем. А может и нет. Он даже лучше подходит для бросания во врага чем банан!
Но может отскочить и нанести урон тебе. Опасная штука.''',
        "количество": 3,
        "стоимость": 0.1,
        "именование": "Камень"
    },
    "golf_cap": {
        "описание": '''
С виду простая кепка, но не зря же она лежит тут среди прочих предметов?''',
        "количество": 1,
        "стоимость": 4.0,
        "именование": "Кепка"
    }
}

itemSelector: list[str] = [ # Список для выбора предметов
    f'''
    {itemForChose["banana"]["именование"]} - Кол-во: {itemForChose["banana"]["количество"]}
    {itemForChose["banana"]["описание"]}.''',
    f'''
    {itemForChose["luck_potion"]["именование"]} - Кол-во: {itemForChose["luck_potion"]["количество"]}
    {itemForChose["luck_potion"]["описавние"]}.''',
    f'''
    {itemForChose["rock"]["именование"]} - Кол-во: {itemForChose["rock"]["количество"]}
    {itemForChose["rock"]["описание"]}.''',
    f'''
    {itemForChose["golf_cap"]["именование"]} - Кол-во: {itemForChose["golf_cap"]["количество"]}
    {itemForChose["golf_cap"]["описание"]}.''']


# == Квест №1 "Имя игрока" ==
# == Автор: Алексей Т. (OneRun) ==
print('Приветствую тебя! Назови своё имя.')
player_name = input('Моё имя: ')
print(f'Приветствую тебя странник {player_name}! Добро пожаловать в земли Гаргантюа!')
# == Конец квеста №1 "Имя игрока" ==

# == Квест №2 "Путь героя" ==
# == Автор: Алексей Т. (OneRun) ==
print(f'''Чтож, {player_name}, настало время выбрать свой путь. Какой класс тебе ближе?
      Классы:
      1. Маг
      2. Воин
      3. Разбойник''')

while True:
    playerChoice = input('Выбери класс (1,2,3): ')
    if playerChoice not in ['1', '2', '3']:
        print('Неверный выбор. Пожалуйста, выбери 1, 2 или 3.')
        continue
    classListIndex = int(playerChoice) - 1  # Преобразуем выбор игрока в индекс списка классов
    if classListIndex in [0, 1, 2]:
        player_class = class_choices[classListIndex]
        print(f'''Ты выбрал класс {player_class}. {class_explained[player_class]}
        Ты уверен в своём выборе? (да/нет)''')
        playerConfirmation = input('Мой ответ: ...')
        if playerConfirmation.lower() in ['да', 'yes', 'y', 'д', 'давай', '1']:
            print(f'''Отлично, {player_name}! Ты выбрал класс {player_class}. Твой путь только начинается!''')
            break
        else:
            print('Хорошо, давай попробуем ещё раз.')

input('Нажми Enter, чтобы продолжить...')
# == Конец квеста №2 "Путь героя" ==

# == Квест №3 "Инвентарь героя" ==
# == Автор: Алексей Т. (OneRun) ==

inventory : list[str] = []  # Инвентарь игрока, изначально пустой
print(f'''
Чтож герой, пора снарядить тебя в путешествие!
Вот твой походный мешок. В этом инвентаре ты будешь хранить свои вещи.
В нём есть 3 ячейки для предметов.
Ты взял походный мешок и заглянул внутрь.''')
print('''---Твой инвентарь---''')
for i in range(len(inventory)):
    inventory[i] if inventory[i] else print("Пусто")

if len(inventory) == 0: print("Пусто")
print("Мда... не густо")


itemChoice = 99
choiceCount = 0
while len(itemSelector) != 2:
    
    print(f'''
    Вот список предметов, которые ты можешь взять с собой в путешествие: ''')
    for i in range(len(itemSelector)):
        print(f'{i + 1}. {itemSelector[i]}')

    itemChoice = input('Выбери предмет (введи номер предмета): ')
    
    if itemChoice not in ['1', '2', '3', '4']:
        print('Неверный выбор. Пожалуйста, выбери 1, 2, 3 или 4.')
        continue
    
    if itemChoice == '1': key = "banana"
    elif itemChoice == '2': key = "luck_potion" 
    elif itemChoice == '3': key = "rock"
    elif itemChoice == '4': key = "golf_cap"

    inventory.insert(0,itemForChose[key]["именование"])
    del itemSelector[int(itemChoice) - 1]  # Удаляем выбранный предмет из списка доступных предметов


    print(inventory)
    print(len(itemSelector))
    choiceCount += 1
    
print('''Чтож, ты сделал свой выбор.''')
print(list(itemForChose.keys()))