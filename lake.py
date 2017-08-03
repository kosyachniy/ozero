from json import *
from func import *

def put_obj(obj, s):
    with open('data/' + s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open('data/' + s + '.txt', 'r') as f:
        return loads(f.read())

def red_hod_to_state(id, h, s):
        h['musor'] = max(h['musor'], s['musor'])
        if h['robot']:
            if s['robot'][0]:
                h['robot'] = [1, h['robot']]
            else:
                h['robot'] = [0, h['robot']]
        return h

def lake_registation(id, list_of_lakes):
    i = 1
    L = len(list_of_lakes)
    while i < L and len(list_of_lakes[i]) != 1:
        i += 1
    if i == L:
        list_of_lakes.append(["Озеро" + str(i), id])
    else:
        list_of_lakes[i] = ["Озеро" + str(i), id]
    return i, list_of_lakes

def gamers_information(id):
    return {'id': id,
    'name': "",
    'lake': 0,
    'gamer_nomber': 0,
    'day': 0}

def state():
    return {'musor': 2,
    'money': 100,
    'level': 1,
    'clean_level': 0,
    'grean': 0,
    'lobsters': 0,
    'yaxts': [],
    'parks': [],
    'robot': [0, 0]}



def do_game(d, dict, list):
    set = d.keys()
    for i in set:
        d[i]



def hod():
    return {'musor': 0,
            'purity': 0,
            'level': 0,
            'clean_level': 0,
            'lobster': 0, 'yaxt': "", 'park': "", 'robot': 0,
    'attak_name': 0,
    'diversion_name': 0,'diversion_money': 0,
    'sponsor_name': 0, 'sponsor_money': 0,
    'green': 0}

def humans_day(id):
    return {
    'i': gamers_information(id),
    's': station(),
    'h': hod(),
    'money_minus': 0,
    'money_plus': 0}

def one(i, words, set):
    if len(words) > i and words[i] in set and words[i+1].isdigit():
        return 1
    return 0

def two(i, words, set):
   if len(words) > i + 1 and words[i] in set and words[i+1].isdigit() and words[i+2].isdigit():
       return 1
   return 0

def tchk(s):
    if s[0] == '0':
        return s[0] + '.' + s[1:]
    return s

def anser_for_hod(day, id, h):
    st = "Ход за день " + str(day) + ":\n"
    st += "Мусорим на " + str(h['musor']) + '\n'
    if h['purity']:
        st += "Чистим своими силами за 60 ед\n"
    if h['level']:
        st += "Улучшаем производство на заводе\n"
    if h['clean_level']:
        st += "Покупаем фильтры\n"
    if h['lobster']:
        st += "Сегодня у вас на ужин аристократические лобстеры\n"
    if h['robot']:
        if h['robot'][0]:
            if h['robot'] >= 180:
                st += "Вы покупаете робота за 180 и устонавиваете ему защиту за {}\n".format(h['robot']-180)
            else:
                st += "На покупку робота нужно 180, а вы меньше поставили("
        else:
            st += "Повышение защиты робота на {}".format(h['robot'][1])
    if h['yaxt']:
        st += "Купили яхту: {}".format(h['yaxt'])
    if h['park']:
        st += "Купили парк: {}".format(h['park'])
    if h['attak_name']:
        st += "Атакуем игрока под номером " + str(h['attak_name']) + "\n"
    if h['green']:
        st += "Голосуем против игрока под номером " + str(h['green']) + "\n"
    if h['diversion_name'] and h['diversion_money']:
        st += "Диверсия на робота под номером " + str(h['diversion_name']) + ", тратим " + str(
            h['diversion_money']) + '\n'
    if h['sponsor_money'] and h['sponsor_name']:
        st += "Спонсируем игрока под номером " + str(h['sponsor_name']) + " на " + str(
            h['sponsor_money']) + ' едениц\n'
    mess(id, st)






musor_set = set(["М", "Мусорю", "Мусор", "Мусорим"])
purity_set = set(["Ч", "Чистим", "Чищу"])
pokupka_set = set(["П", "Покупка", "Покупаю", "Приобретаю"])

level_set = set(["У", "Уровень", "Up"])
clean_set = set(["Ф", "Фильтр"])
lobster_set = set(["Л", "Лобстер", "Лобстера", "Лобстеров", "Лобстеры"])
yaxt_set = set(["Я", "Яхта", "Яхту"])
park_set = set(["П", "Парк"])
robot_set = set(["Р", "Робот", "Робота"])

attak_set = set(["А", "Атака", "Атакую", "Атакуем"])
diversion_set = set(["Д", "Диверсия"])
sponsor_set = set(["С", "Спонсирую", "Спонсорство"])
green_set = set(["Г", "Гринпис", "Голосую"])

def make_hod_file(day, id, words): #создаёт файл "hod-
    h = hod()
    i = 0
    print(words)
    ch = '' #счётчик
    st = ""
    while i < len(words):
        s = words[i]
        if ch == '':
            if s in level_set:
                h['level'] = 1
            elif s in purity_set:
                h['purity'] = 1
            elif s in clean_set:
                h['clean_level'] = 1
            elif s in lobster_set:
                h['lobster'] = 1
            elif s in musor_set:
                ch = 'm'
            elif s in robot_set:
                ch = 'r'
            elif s in yaxt_set:
                ch = 'y'
            elif s in park_set:
                ch = 'p'
            elif s in attak_set:
                ch = 'a'
            elif s in diversion_set:
                ch = 'd0'
            elif s in sponsor_set:
                ch = 's0'
            elif s in green_set:
                ch = 'g'
        else:
            if ch == 'm':
                if len(words[i]) > 2 or not(words[i].isdigit()):
                    mess(id, "Неккоректное колличество мусора")
                    ch = ''
                    break
                else:
                    h['musor'] = float(tchk(words[i]))
                    ch = ''
            elif ch == 'r' and words[i].isdigit():
                h['robot'] = int(words[i])
                ch = ''
            elif ch == 'y':
                if words[i] == "@":
                    ch = ''
                    h['yaxt'] = st
                    st = ""
                else:
                    st += words[i] + ' '
            elif ch == 'p':
                if words[i] == "@":
                    ch = ''
                    h['park'] = st
                    st = ""
                else:
                    st += words[i] + ' '
            elif ch == 'a':
                if s.isdigit():
                    h['attak_name'] = int(s)
                ch = ''
            elif ch == 'g':
                if s.isdigit():
                    h['green'] = int(s)
                ch = ''
            elif ch == 'd0':
                if s.isdigit():
                    h['diversion_name'] = int(s)
                else:
                    ch = ''
                ch = 'd1'
            elif ch == 'd1':
                if s.isdigit():
                    h['diversion_money'] = int(s)
                ch = ''
            elif ch == 's0':
                if s.isdigit():
                    h['sponsor_name'] = int(s)
                else:
                    ch = ''
                ch = 's1'
            elif ch == 's1':
                if s.isdigit():
                    h['sponsor_money'] = int(s)
                ch = ''

        i += 1
    if ch == 'y':
        h['yaxt'] = st
    if ch == 'p':
        h['park'] = st
    put_obj(h, "hod" + str(id) + "_day" + str(day))
    return h