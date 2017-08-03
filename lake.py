from func import *

musor_set = set(["М", "Мусорю", "Мусор", "Мусорим"])
purity_set = set(["Ч", "Чистим", "Чищу"])
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

def red_hod_to_state(id, h, s):
        h['musor'] = min(h['musor'], s['musor'])
        if h['robot']:
            if s['robot'][0]:
                h['robot'] = [1, h['robot']]
            else:
                h['robot'] = [0, h['robot']]
        return h
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
def state():
    return {'musor': 2,
    'money': 100,
    'level': 1,
    'clean_level': 0,
    'grean': 0,
    'lobsters': 0,
    'yaxts': [],
    'parks': [],
    'robot': [0, 0],
    'money_minus': 0,
    'money_plus': 0}

def hod():
    return {'musor': 0,#1+
            'purity': 0,#2
            'level': 0,#3
            'clean_level': 0,#4
            'lobster': 0,#5
            'yaxt': "",#6
            'park': "",#7
            'robot': 0,#8
            'attak_name': 0,#9
            'diversion_name': 0,#10
            'diversion_money': 0, #11
            'sponsor_name': 0,#12
            'sponsor_money': 0,#13
            'green': 0}#14
def do_game(day, dict, list, list_robots):
    get_k = 1
    set = day.keys()
    for i in set: #i == id
        h = day[i]['h']
        s = day[i]['s']
        s['money_plus'] += 60*get_k*s['level']
        s['musor'] += s['level'] - h['musor']#1
        s['money_minus'] += 20*h['musor']
        if h['purity']:#2
            s['money_minus'] += 60
        if h['level']:
            s['money_minus'] += 100 + s['level']*20
            s['level'] += 1
        if h['clean_level']:
            s['money_minus'] += 100 + s['clean_level']*40
            s['clean_level'] += 1
        if h['lobster']:
            s['lobster'] += 1
        if h['yaxt']:
            s['yaxt'].append(h['yaxt'])
        if h['park']:
            s['park'].append(h['park'])
        #if s['']
        day[i]['s']['money_minus'] = s['money_minus']
        day[i]['s']['money_plus'] = s['money_plus']
        day[i]['s_new'] = s
    for i in set:
        put_obj(day[i]['s_new'], i+'-s'+str(list[0]))

def k(x):
    return 1

def lake(st):
    return {
        'name': st,
        'purity': 60,
        'gamers': [],
        'yaxt': [],
        'parks': [],
        'robots': []}