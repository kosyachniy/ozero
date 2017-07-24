from json import *

def put_obj(obj, s):
    with open(s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open(s + '.txt', 'r') as f:
        return loads(f.read())

def lake_registation(id, kol):
    kol = kol + 1
    s = 'L(' + '5' + ')' + '-day' + '00'
    lake =  {'name': 'Озеро(' + chr(kol) + ')', 'day': 0,
            'kol_gamers': 1, 'gamers': [id],
            'yaxts': [],    'robots': [],
            'purity': 60,   'delata_purity': 0}
    put_obj(lake, s)
    return lake, kol
