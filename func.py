import vk_api
import time
#import vk
vk = vk_api.VkApi(token='5998b265c9a37305498547c92781806b617eb4fe01131cc738d877a5d29b45beb8600d4371980cb525910')
#vk = vk_api.VkApi(login='79193540345', password='')
vk.auth()
"""
vk.users.get(user_id=144520879)

x = vk.users(user_id=144520879)
x = vk.status.get()
x = vk_api.Session()




vk.users.get()
print(vk_api)

session = vk_api.Session()
vk_api = vk.API(session)
print(vk_api.users.get(user_id=144520879))
"""
slovarni_zapas_oneword = {'Спасибо': 'Всегда пожалуйста, уважаемый',
        'сцук': 'Да уж, тяжела твоя доля',
         '1': 'Единичка',
         '2': 'Двойка',
         '3': 'Тройка',
         '4': 'Четвёрка',
         '5': 'Пятёрка',
         '6': 'Шестёрка',
         '7': 'Семёрка',
         '8': 'Восьмёрка',
         '9': 'Девятка',
         '0': 'Ноль',
         'Предел': 'Число А называется пределом последовательности, если для любого положительного ε существует такой номер N0, начиная с которого все элементы последовательности лежат в ε-окрестности числа А',
         '123': '456',
         '456': '123',
          'Помощь': 'Список доступных фраз:\n'
                    '"Называй меня (имя_в_одно_слово)"\n'
                    '"Хочу зарегистрировать новое озеро"\n'
                    '"Список озёр"\n'
                    '"Захожу в озеро (название озера)"\n'
                          } #словарный запас
privetstvie = ['Привет', 'Здарова', 'Здравствуй', 'Ghbdtn']
Oskorbleniye = ['Пидор', 'Козёл', 'Падла',
                'Гнида', 'Лох', 'Тупой',
                'Глупый', 'Хуй', 'Урод',
                'Козёл', 'Падла','Гнида']

Obrashenie = ['Ты', 'Тетрис', 'Бот', 'Озеро', 'Робот', 'Компьютер', 'Калькулятор', 'Ozero', 'Хочу']

def oskorbi(word, item):
    mess(item['user_id'], "Всё правильно: ты " + word)

def answer(item):
    print('item:=', item)
    if item['body'] in zapas:
        mess(item['user_id'], zapas[item['body']])
    else:
        mess(item['user_id'],'Непонимание')
             #'Тысяча извинений, Иван-ВеликийСоздатель не научил меня оперировать такими сложными материями. не могли бы вы говорить понятнее?')

def get_words(S):
    lister = set('.,!-:"?')#символы подлежащие удалению
    t = S.split() #список слов
    for i in range(len(t)):
        x = list(t[i])
        j = 0
        while j < len(x):
            if x[j] in lister:
                x.pop(j)
                j = j - 1
            j = j + 1
        t[i] = (str().join(x)).title() #собирает слово из списка и делает так, что первый символ каждого слова - большая буква, остальные маленькие
    return t

def proverka(st, words):
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if list[i] != words[i]:
            return 0
    return 1

def p_list_of_lakes (id, list_of_lakes):
    if len(list_of_lakes) == 0:
        mess(id, "Озёр ещё нет")
    else:
        for i in range(len(list_of_lakes)):
            mess(id, list_of_lakes[i][0])
        mess(id, "Конец списка.")

def find_gemer(id, list_of_lakes):
    for i in range(len(list_of_lakes)):
        for j in range(len(list_of_lakes[i])):
            if id == list_of_lakes[i][j]:
                return i, j
    return -1, -1

def print_gamers_on_lake(i, id, list_of_lakes):
    if len(list_of_lakes) == 0:
        mess(id, "На озере "+list_of_lakes[0]+" никого нет")
    else:
        for j in range(1, len(list_of_lakes[i])):
            mess(id, "Игрок " + str(list_of_lakes[i][j]))
        mess(id, "Конец списка")

mess=lambda id, t: vk.method('messages.send', {'user_id':id, 'message':"." + t})


#users.get(144520879)