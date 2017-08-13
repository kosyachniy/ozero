import vk_api
import time
from json import *

vk = vk_api.VkApi(token='5998b265c9a37305498547c92781806b617eb4fe01131cc738d877a5d29b45beb8600d4371980cb525910')
Vano = vk_api.VkApi(login="79193540345", password='1йфячыц2')
vk.auth()#заходит в группу
Vano.auth()

def put_obj(obj, s):
    with open('data/' + s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open('data/' + s + '.txt', 'r') as f:
        return loads(f.read())

musor_set = set(["М", "Мусорю", "Мусор", "Мусорим"])
putity_set = set(["Ч", "Чистим", "Чищу"])
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
          'Помощь': 'Вот на что я умею отвечать:\n'
                    '"Привет"\n'
                    '"Называй меня (имя_в_одно_слово)"\n'
                    '"Хочу зарегистрировать новое озеро"\n'
                    '"Список озёр"\n'
                    '"Список Игроков На Озере (название_озера)"\n'
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

def get_words(S):
    S = S + '%'
    lister = set(',! :?%"ёЁ')  # символы подлежащие удалению и изменению
    words = []
    flag = 1
    L = len(S)
    i = 0
    st = ""
    while i < L:
        if flag:
            if S[i] in lister:
                if S[i] == ' ' or S[i] == '%':
                    if st:
                        words.append(st.title())
                        st = ""
                elif S[i] == 'Ё' or S[i] == 'ё':
                    st += 'е'
            else:
                st += S[i]
        else:
            if S[i] != '%':
                st += S[i]
        if S[i] == '%':
            if st:
                if flag:
                    words.append(st.title())
                else:
                    words.append(st)
                st = ''
            flag = not(flag)
        i += 1
    return words


def p_reg_list (id, reg_list):
    if len(reg_list) == 1:
        mess(id, "Озёр ещё нет")
    else:
        for i in range(1, len(reg_list)):
            if reg_list[i][0]: #Если название озера не пустое
                mess(id, reg_list[i][0])
        mess(id, "Конец списка.")

def find_gemer(id, reg_list):
    for i in range(1, len(reg_list)):
        for j in range(1, len(reg_list[i])):
            if id == reg_list[i][j]:
                return i, j
    return -1, -1

def lake_registation(id, reg_list):
    i = 1
    L = len(reg_list)
    while i < L and len(reg_list[i]) != 1:
        i += 1
    if i == L:
        reg_list.append(["Озеро" + str(i), id])
    else:
        reg_list[i] = ["Озеро" + str(i), id]
    return i, reg_list

def sPM(x): #строчку в порядковое числительное муржского рода
    st = ''
    if x == 1:
        st = 'первый'
    elif x == 2:
        st = 'второй'
    elif x == 3:
        st = 'третий'
    elif x == 4:
        st = 'четвётрый'
    elif x == 5:
        st = 'пятый'
    elif x == 6:
        st = 'шестой'
    elif x == 7:
        st = 'седьмой'
    elif x == 8:
        st = 'восьмой'
    elif x == 9:
        st = 'девятый'
    elif x == 10:
        st = 'десятый'
    elif x == 11:
        st = 'одиннадцатый'
    elif x == 12:
        st = 'двенадцатый'
    elif x == 13:
        st = 'тринадцатый'
    elif x == 14:
        st = 'четырнадцатый'
    elif x == 15:
        st = 'пятнадцатый'
    elif x == 16:
        st = 'шестнадцатый'
    elif x == 17:
        st = 'семнадцатый'
    else:
        st = str(x)
    return st

def sKM(x): #строчку в числительно
    st = ''
    if x == 0:
        st == 'ноль'
    elif x == 1:
        st = 'один'
    elif x == 2:
        st = 'два'
    elif x == 3:
        st = 'три'
    elif x == 4:
        st = 'четыре'
    elif x == 5:
        st = 'пять'
    elif x == 6:
        st = 'шесть'
    elif x == 7:
        st = 'семь'
    elif x == 8:
        st = 'восемь'
    elif x == 9:
        st = 'девять'
    elif x == 10:
        st = 'десять'
    elif x == 11:
        st = 'одиннадцать'
    elif x == 12:
        st = 'двенадцать'
    elif x == 13:
        st = 'тринадцать'
    elif x == 14:
        st = 'четырнадцать'
    elif x == 15:
        st = 'пятнадцать'
    elif x == 16:
        st = 'шестнадцать'
    elif x == 17:
        st = 'семнадцать'
    else:
        st = str(x)
    return st


def daiy_s(day, id):
    s = get_obj(id+'-s'+str(day))
    st = "Ваше состояние за день " + str(day)
    st += "\nВ кармане "+str(s['money'])+" ед\nНа складе "+str(s['musor'])+" едениц отходов\nУровень производства "+str(s['level'])+"\n"
    if s['clean_level']:
        st += "Уровень фильтра "+str(s['clean_level']) + "/10\n"
    if s['lobster']:
        st += "Вы ужинали лобстерами "+sKM(s['lobster'])+" раз\n"
    if s['yaxt']:
        st += sKM(len(s['yaxt'])).title()+" ваши гордые яхты плавают в озере\n"
    if s['park']:
        st += "Вы посторили "+sKM(len(s['park']))+" парк аттракционов\n"
    if s['robot'][0]:
        st += "Робот " + s['robot'][0] + " с защитой "+sKM(s['robot'][1]) + " работает без перебоев\n"
    mess(id, st)


mess=lambda id, t: vk.method('messages.send', {'user_id':int(id), 'message':"." + t})
