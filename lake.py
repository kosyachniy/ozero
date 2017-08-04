from func import *

def red_hod_to_state(id, h, s, reg_list, dict_of_dilogs, list_of_robots):
    h['musor'] = min(h['musor'], s['musor'])
    nom_of_our_lake = dict_of_dilogs[id]['lake']
    if len(reg_list[nom_of_our_lake]) > h['attak_name']:
        h['attak_name'] = 0
    if not(h['diversion_name'] and h['diversion_money']):
        h['diversion_name'] = 0
        h['diversion_money'] = 0
    else:
        if h['diversion_name'].isdigit():
            if h['diversion_name'] < len(list_of_robots) - 1:
                h['diversion_name'] = ""
        else:
            if list_of_robots.count(h['diversion_name']):
                h['diversion_name'] = list_of_robots.index(h['diversion_name'])
    return h




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
    if h['robot'][0]:
        st += "Покупаем робота " + h['robot'][0] + "\n"
        if h['robot']:
            st += "Вы покупаете робота за 180 и устонавиваете ему защиту на {}\n".format(h['robot'][1])
        else:
            st += "Если у вас есть робот, его броня будет увеличена на " + str(h['robot'][1])
    if h['yaxt']:
        st += "Купили яхту: {}".format(h['yaxt'])
    if h['park']:
        st += "Купили парк: {}".format(h['park'])
    if h['attak_name']:
        st += "Атакуем игрока на вашем озере под номером " + str(h['attak_name']) + "\n"
    if h['green']:
        st += "Голосуем против игрока на вашем озере под номером " + str(h['green']) + "\n"
    else:
        st += "Вы голосуете против себя, так как ни за кого не проголосовали"
    if h['diversion_name'] and h['diversion_money']:
        st += "Диверсия на робота под номером " + str(h['diversion_name']) + ", тратим " + str(
            h['diversion_money']) + '\n'
    if h['sponsor_money'] and h['sponsor_name']:
        st += "Спонсируем игрока под номером " + str(h['sponsor_name']) + " на " + str(
            h['sponsor_money']) + ' едениц\n'
    mess(id, st)
def make_hod_file(id, words): #создаёт файл "hod-
    h = hod()
    i = 0
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
                    return hod()
                else:
                    h['musor'] = float(tchk(words[i])) #сразу мусорим правильно
                    ch = ''
            elif ch == 'r':
                if words[i].isdigit():
                    h['robot'][1] = int(words[i])
                else:
                    h['robot'][0] = words[i]
                if i + 1 > len(words) and words[i+1].isdigit():
                    h['robot'][1] = int(words[i+1])
                ch = ''
            elif ch == 'y':
                h['yaxt'] = words[i]
            elif ch == 'p':
                h['park'] = words[i]
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
    'robot': ["", 0],
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
            'robot': ["", 0],#8
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
def lake(st, id):
    return {
        'name': st,
        'purity': 60,
        'gamers': [id,],
        'yaxt': [],
        'parks': [],
        'robots': []}

def make_list_of_robots(list_of_lakes):
    list = []
    for i in range(1,len(list_of_lakes)):
        for j in range(len(list_of_lakes[i]['robots'])):
            list.append(list_of_lakes[i]['robots'][j])
    return list