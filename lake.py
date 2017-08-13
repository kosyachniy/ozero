from func import *

def red_hod_to_state(id, h, s, reg_list, dict_of_dilogs, list_of_lakes, list_of_robots):
    h['musor'] = min(h['musor'], s['musor'])
    L = dict_of_dilogs[id]['lake']
    money_plus = 30*list_of_lakes[L]['k']*s['level']
    money_minus = (s['musor']-h['musor'])*10
    h['inf'] = "Производство продукции принесёт вам " + str(money_plus) + " ед\n"
    h['inf'] += "Утилизация мусора заберёт " + str(money_minus) + " ед\n"
    if h['level']:
        money_minus += 90 + 30*s['level']
    if h['lobster']:
        money_minus += 60
    if h['clean_level']:
        money_minus += 120
    if h['purity']:
        money_minus += 30
    if h['yaxt']:
        money_minus += 180
    if h['park']:
        money_minus += 600
    print("money_plus:= ", money_plus, ". money_minus:= ", money_minus)
    h['inf'] += "Предпологаемая прибыль: " + str(money_plus-money_minus) + " ед\n"
    if s['money'] < money_minus:
        mess(id, "Внимание! Attention! Aufmerksamkeit!\n"
        + str(money_minus) +' > '+ str(s['money']) + "\nЕсли не измените ход, то уёдёте в минус по деньгам и потеряете уровень!!!")
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

def anser_for_hod(day, id, h, s):
    st = "Принят ход за день " + str(day) + ":\n"
    st += "Мусорим на " + str(h['musor']) + ' из '+str(s['musor'])+'\n'
    if h['purity']:
        st += "Чистим своими силами за 30 ед\n"
    if h['level']:
        st += "Улучшаем производство на заводе за "+ str(90 + 30*s['level']) +" ед\n"
    if h['clean_level']:
        st += "Покупаем фильтры за 120 ед\n"
    if h['lobster']:
        st += "На ужин сегодня роскошные лобстеры за 60 ед\n"
    if h['yaxt']:
        st += "Ваша новая яхта будет называться " + h['yaxt']+'\n'
    if h['park']:
        st += "Завтра досторят новый парк аттракционов: " + h['park']+'\n'
    mess(id, st)
    mess(id, h['inf'])

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
                ch = 'r0'
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
                print(words[i].isdigit())
                if len(words[i]) > 2 or not(words[i].isdigit()):
                    mess(id, "Неккоректное колличество мусора")
                    ch = ''
                    return hod()
                else:
                    h['musor'] = float(tchk(words[i])) #сразу мусорим правильно
                    ch = ''
            elif ch == 'r0':
                if words[i].isdigit():
                    h['robot'][1] = int(words[i])
                else:
                    h['robot'][0] = words[i]
                if i + 1 > len(words) and words[i+1].isdigit():
                    h['robot'][1] = int(words[i+1])
                ch = ''
            elif ch == 'y':
                h['yaxt'] = words[i]
                ch = ''
            elif ch == 'p':
                h['park'] = words[i]
                ch = ''
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
    'lobster': 0,
    'yaxt': [],
    'park': [],
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
            'green': 0,
            'inf': ""}#14
#musor level lake-purity
#purity claen_level
#lobster yaxt park
#robot
#attak_name
#diversion
#sponsor
#green


def do_game(game, dict, reg_list, list_of_lakes, list_of_robots, dict_of_dilogs):
    set = game.keys()
    for i in set: #i == id
        L = dict_of_dilogs[i]['lake'] #номер озера
        h = game[i]['h']
        s = game[i]['s']
        h['inf'] = ''
        vuruchka = 30*list_of_lakes[L]['k']*s['level'] #(+)ежедневная прибыль
        if h['clean_level']:
            s['clean_level'] += 1 #(!) не больше 10того уровня
            s['money_minus'] += 120
            h['inf'] += 'Установили новые фильтры за 120 ед. \n'
        util_prise = (s['musor'] - h['musor'])*10 #(+)тратим деньги на утилизацию
        s['money_plus'] += vuruchka
        s['money_minus'] += util_prise
        list_of_lakes[L]['purity'] -= h['musor'] #(+)у озера уходят намусоренные проценты
        s['musor'] = s['level']*(1 - 0.1*s['clean_level']) #(не хватает фильтрв) появляются новые еденицы мусора

        if h['lobster']:
            s['money_minus'] += 60
            s['lobster'] += 1
            h['inf'] += 'Купили лобстеров за 60 ед\n'
        if h['yaxt']:
            print('yaxt:',h['yaxt'])
            s['money_minus'] += 180
            h['inf'] += '"'+h['yaxt'] + '" завтра выйдет в озеро\n'
            s['yaxt'].append(h['yaxt'])
            list_of_lakes[L]['yaxt'].append(h['yaxt'])
        if h['park']:
            print('park:',h['park'])
            s['money_minus'] += 600
            h['inf'] += '"'+h['park'] + '" ваш новый парк аттаркционов\n'
            s['park'].append(h['park'])
            list_of_lakes[L]['park'].append(h['park'])
        if h['level']:
            s['money_minus'] += 120
            h['inf'] += 'Купили новый уровень за 120 ед\n'
            s['level'] += 1  # покупаем уровень
        h['inf'] += 'Фабрика принесла выручку: ' + str(vuruchka) + '\n'
        h['inf'] += 'На утилизацию вы потратили ' + str(util_prise) + '\n'

        if h['purity']:
            list_of_lakes[L]['purity'] += 1
            h['inf'] += 'Почистили совими силами за 30 ед\n'
            s['money_minus'] += 30
        game[i]['h']['inf'] = h['inf']
        game[i]['s']['money_minus'] = s['money_minus']
        game[i]['s']['money_plus'] = s['money_plus']
        game[i]['s_new'] = s
    for i in set:
        put_obj(game[i]['s'], i+'-s'+str(reg_list[0]))
        put_obj(game[i]['h'], i+'-h'+str(reg_list[0]))
        game[i]['s_new']['money'] -= game[i]['s_new']['money_minus']
        while game[i]['s_new']['money'] < 0:
            game[i]['s_new']['level'] -= 1
            game[i]['s_new']['money'] += 100
        game[i]['s_new']['money'] += game[i]['s_new']['money_plus']
        game[i]['s_new']['money_minus'] = 0
        game[i]['s_new']['money_plus'] = 0
        mess(i, "Доброе утро! Новый день "+str(reg_list[0]+1)+"\n Вчера вы \n" + game[i]['h']['inf'] +"\nВ кармане "+str(game[i]['s_new']['money']))
        put_obj(h, i+'-h'+str(reg_list[0]))
        put_obj(game[i]['s_new'], i+'-s'+str(reg_list[0] + 1))
    put_obj(list_of_lakes, 'list_of_lakes')
    return game

def k(x):
    if x > 80:
        return 2
    elif x > 60:
        return 1.5
    elif x > 40:
        return 1
    elif x > 20:
        return 0.5
    elif x > 0:
        return 1/3
    else:
        return -100

def lake(st, id):
    return {
        'name': st,
        'purity': 60,
        'k': k(60),
        'gamers': [id,],
        'yaxt': [],
        'park': [],
        'robot': []}

def make_list_of_robots(list_of_lakes):
    list = []
    for i in range(1,len(list_of_lakes)):
        for j in range(len(list_of_lakes[i]['robot'])):
            list.append(list_of_lakes[i]['robot'][j])
    return list
