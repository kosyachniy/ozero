from json import *
from func import *

def put_obj(obj, s):
    with open(s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open(s + '.txt', 'r') as f:
        return loads(f.read())

def lake_registation(id, kol):
    kol = kol + 1
    s = 'L(' + str(kol) + ')' + '-day' + '00'
    lake =  {'name': 'Озеро(' + str(kol) + ')', 'day': 0,
            'kol_gamers': 1, 'gamers': [id],
            'yaxts': [],    'robots': [],
            'purity': 60,   'delata_purity': 0}
    put_obj(lake, s)
    return lake, kol

class gamers_information:
    id = 0
    name = ""
    lake = 0
    gamer_nomber = 0
    day = 0

class station:
    musor = 2
    money = 100
    level = 1
    clean_level = 0
    grean = 0
    lobsters = 0
    yaxts = []
    parks = []
    robot = 0

class hod:
    musor = 0
    purity = 0
    level = 0; clean_level = 0; lobster = 0; yaxt = ""; park = ""; pobot = 0

    attak_name = 0
    diversion_name = 0
    diversion_money = 0
    sponsor_name = 0
    sponsor_money = 0
    grean = 0

class humans_day:
    inform = gamers_information()
    s = station()
    h = hod()
    money_minus = 0
    money_plus = 0

musor_set = set(["М", "Мусорю", "Мусор", "Мусорим"])
pokupka_set = set(["П", "Покупка", "Покупаю", "Приобретаю"])
yaxt_set = set(["Я", "Яхта", "Яхту"])
park_set = set(["П", "Парк"])
lobster_set = set(["Л", "Лобстер", "Лобстера", "Лобстеров", "Лобстеры"])
robot_set = set(["Р", "Робот", "Робота"])
attak_set = set(["А", "Атака", "Атакую"])
diversion_set = set(["Д", "Диверсия"])
peredacha_set = set(["С", "Спонсирую", "Спонсорство"])
green_set = set(["Г", "Гринпис", "Голосую"])
unite = set.union(musor_set, pokupka_set, yaxt_set, park_set, lobster_set,
                   robot_set, attak_set, diversion_set, peredacha_set, green_set)
def one(i, words, set):
    if len(words) > i and words[i] in set and words[i+1].isdigit():
        return 1
    return 0

def tchk(s):
    if s[0] == '0':
        return s[0] + '.' + s[1:]
    return s

def make_hod(person, words):
    day = person.inform.day
    if words[0].isdigit():
        day = max(person.inform.day, int(words[0]))
        words.remove(words[0])
    st = "Вы назначили ход за день " + str(day)+".\n"
    for i in range(len(words)):
        if one(i, words, musor_set):
            person.h.musor = min(float(tchk(words[i+1])), float(person.s.musor))
    st = st + "Мусорим на " + str(person.h.musor)
    return person, st