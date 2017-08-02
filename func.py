import vk_api
import time

vk = vk_api.VkApi(token='5998b265c9a37305498547c92781806b617eb4fe01131cc738d877a5d29b45beb8600d4371980cb525910')
Vano = vk_api.VkApi(login="79193540345", password='1йфячыц2')
vk.auth()#заходит в группу
Vano.auth()


def send_stiker(id, nom):
    dict = {'user_id': id, 'sticker_id': nom}
    mess(id, "Пробуем отправить стикер")
    vk.method('messages.send', dict)

slovarni_zapas_oneword = {'Спасибо': 'Всегда пожалуйста, уважаемый',
        'сцук': 'Да уж, тяжела твоя доля',
        'Ход': 'Какой?',
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
                    '"Список Игроков На Озере" (название_озера)\n'
                    '"Захожу в озеро (название_озера)"\n'
                    '"Выйти Из Моего Озера"\n'
                    '"Какой Сейчас День?"\n'
                    '"Как сделать ход?"\n'
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
    lister = set('.,!-:?"ёЁ')#символы подлежащие удалению
    t = S.split() #список слов
    flag = 1 #из названия яхт и парков символы не удаляются
    for i in range(len(t)):
        if flag == 1:
            x = list(t[i])
            j = 0
            while j < len(x):
                if x[j] in lister:
                    if x[j] == 'ё' or x[j] == 'Ё':
                        if j == 0:
                            x[j] = 'Е'
                        else:
                            x[j] = 'е'
                    else:
                        x.pop(j)
                        j = j - 1
                j = j + 1
            t[i] = (str().join(x)).title() #собирает слово из списка и делает так, что первый символ каждого слова - большая буква, остальные маленькие
        else:
            if t[i] == "@" or t[i][-1:] == "@":
                flag = 1
        if t[i] in words_unite:
            flag = 0
    return t

musor_set = set(["М", "Мусорю", "Мусор", "Мусорим"])
claen_set = set(["Ч", "Чистим", "Чищу"])
pokupka_set = set(["П", "Покупка", "Покупаю", "Приобретаю"])

level_set = set(["У", "Уровень", "А", "Апгрейд"])
clean_set = set(["Ф", "Фильтр"])
lobster_set = set(["Л", "Лобстер", "Лобстера", "Лобстеров", "Лобстеры"])
yaxt_set = set(["Я", "Яхта", "Яхту"])
park_set = set(["П", "Парк"])
robot_set = set(["Р", "Робот", "Робота"])

attak_set = set(["А", "Атака", "Атакую", "Атакуем"])
diversion_set = set(["Д", "Диверсия"])
sponsor_set = set(["С", "Спонсирую", "Спонсорство"])
green_set = set(["Г", "Гринпис", "Голосую"])
pokupka_unite = set.union(yaxt_set, park_set, lobster_set, robot_set)
words_unite = set.union(yaxt_set, park_set)


def proverka(st, words):
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if not(list[i] == words[i]):
            return 0
    return 1

def p_list_of_lakes (id, list_of_lakes):
    if len(list_of_lakes) == 1:
        mess(id, "Озёр ещё нет")
    else:
        for i in range(1, len(list_of_lakes)):
            if list_of_lakes[i][0]: #Если название озера не пустое
                mess(id, list_of_lakes[i][0])
        mess(id, "Конец списка.")

def find_gemer(id, list_of_lakes):
    for i in range(1, len(list_of_lakes)):
        for j in range(1, len(list_of_lakes[i])):
            if id == list_of_lakes[i][j]:
                return i, j
    return -1, -1

mess=lambda id, t: vk.method('messages.send', {'user_id':int(id), 'message':"." + t})
