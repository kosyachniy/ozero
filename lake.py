from json import *
from func import *

def put_obj(obj, s):
    with open(s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open(s + '.txt', 'r') as f:
        return loads(f.read())

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

class class_for_lake:
    nomber = 0
    name = ''

def gamers_information(id):
    return {'id': id,
    'name': "",
    'lake': 0,
    'gamer_nomber': 0,
    'day': 0}

def station():
    return {'musor': 2,
    'money': 100,
    'level': 1,
    'clean_level': 0,
    'grean': 0,
    'lobsters': 0,
    'yaxts': [],
    'parks': [],
    'robot': 0}

def hod():
    return {'musor': 0,
            'purity': 0,
            'level': 0,
            'clean_level': 0,
            'lobster': 0, 'yaxt': "", 'park': "", 'robot': 0,
    'attak_name': 0,
    'diversion_name': 0,'diversion_money': 0,
    'sponsor_name': 0, 'sponsor_money': 0,
    'grean': 0}

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
    if h['attak_name']:
        st += "Атакуем игрока под номером " + str(h['attak_name']) + "\n"
    if h['diversion_name'] and h['diversion_money']:
        st += "Диверсия на робота под номером " + str(h['diversion_name']) + ", тратим " + str(
            h['diversion_money']) + '\n'
    if h['sponsor_money'] and h['sponsor_name']:
        st += "Спонсируем игрока под номером " + str(h['sponsor_name']) + " на " + str(
            h['sponsor_money']) + ' едениц\n'
    mess(id, st)


def make_hod_file(day, id, words): #создаёт файл "hod-
    h = hod()
    for i in range(len(words)):
        if words[i] in pokupka_set:
            while len(words) >= i and words[i] in pokupka_unite:
                if words[i] in lobster_set:
                    h.lobster = 1
                if len(words) > i + 1:
                    if words[i] in yaxt_set:
                        h['yaxt'] = words
        if one(i, words, musor_set):
            h['musor'] = float(tchk(words[i+1]))
            continue
        if words[i] in claen_set:
            h['purity'] = 1
            continue
        if one(i, words, attak_set):
            h['attak_name'] = words[i+1]
            continue
        if one(i, words, green_set):
            h['green'] = words[i+1]
            continue
        if two(i, words, diversion_set):
            h['diversion_name'] = int(words[i + 1])
            h['diversion_money'] = int(words[i + 2])
            continue
        if two(i, words, sponsor_set):
            h['sponsor_name'] = int(words[i + 1])
            h['sponsor_money'] = int(words[i + 2])
            continue
    put_obj(h, "hod" + str(id) + "_day" + str(day))
    return h