from json import *

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
    level = 0
    clean_level = 0
    lobster = 0
    yaxt = ""
    park = ""
    pobot = 0
    attak = 0
    diversion_name = 0
    diversion_money = 0
    peredacha_name = 0
    peredacha_money = 0
    grean = 0

class humans_day:
    inform = gamers_information()
    s = station()
    h = hod()
    money_minus = 0
    money_plus = 0


