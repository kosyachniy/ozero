from lake import *
import os

list_of_lakes = get_obj('list_of_lakes')
dict_of_dilogs = get_obj('dict_of_dilogs')
reg_list = get_obj('reg_list')
list_of_robots = ['',]
game_dict, have_robot_list = make_game_dict(dict_of_dilogs, reg_list)
list_of_robots, list_of_lakes = make_list_of_robots(dict_of_dilogs, game_dict, have_robot_list, list_of_lakes, reg_list)
words = []

def proverka(st, remove = 1):
    global words
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if not(list[i] == words[i]):
            return st
    if remove:
        words = words[len(list):]
    return 1

def dil(id, dict, main_st):
    global words
    if not(proverka(main_st)):
        return 0
    keys = dict.keys()
    if words:
        st = ""
        for string in keys:
            st += '"'+main_st + ' ' + string + '"\n'
        mess(id, st)
        return 1
    for string in keys:
        if proverka(string):
            dict[string](id) #?wtf?
            return 1
    return 0

def put(st):
    set0 = set(st)
    if 'r' in set0:
        put_obj(reg_list, 'reg_list')
    if 'l' in set0:
        put_obj(list_of_lakes, 'day'+str(reg_list[0])+'list_of_lakes')
        put_obj(list_of_lakes, 'list_of_lakes')
    if 'd' in set0:
        put_obj(dict_of_dilogs, 'dict_of_dilogs')

def p_gamers_on_lake(id, lake):
    if len(lake) == 1:
        mess(id, "На озере " + lake[0] +" никого нет")
    else:
        for j in range(1, len(lake)):
            mess(id, '('+str(j)+')'+ get_name(lake[j]))
        mess(id, "Конец списка, "+dict_of_dilogs[id]['obr'])

def chek_list_of_dilogs():
    if not(id in dict_of_dilogs):  # если с этим человеком мы ещё не разговривали, добавляем его в словарь
        x = Vano.method("users.get", {"user_ids": id})[0]
        dict_of_dilogs[id] = {"obr": x["first_name"], "date": item['date'], "first_name": x["first_name"],
                                   "last_name": x["last_name"], "status": 'New', "lake": 0, "nom": 0, "admin":0, "cheat": ""}  # !!
        if int(id) == 144520879 or int(id) == 140420515:
            dict_of_dilogs[id]['admin'] = 1
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
        for i in range(1, 31):
            put_obj(state(), id+'-s'+str(i))
            put_obj(hod(), id+'-h'+str(i))
    elif (dict_of_dilogs[id]['date'] >= item['date']):  # отвечаем только на последние сообщения данного пользователя
        return 1
    else:
        dict_of_dilogs[id]['date'] = item['date']
        put('d')
    return 0

def get_name(id):
    return dict_of_dilogs[id]['first_name'] + ' ' + dict_of_dilogs[id]['last_name']

values = {'out': 0, 'count': 10, 'time_offset': 3600}

def answer_to_admin():
    global list_of_lakes, dict_of_dilogs, reg_list, words
    if proverka("Помощь", remove=0):
        mess(id, "В помощь админу:\nОбнулить\nДай словарь\nДай список\nДай регистрацию\nУстановить день\nСделать ход\n")
    if proverka("Обнулить"):
        reg_list = [1, ]
        dict_of_dilogs = {}
        list_of_lakes = [0, ]
        put('rld')
        return 1
    if proverka("Дай Словарь"):
        mess(id, str(dict_of_dilogs))
        return 1
    if proverka("Дай Регистрацию"):
        mess(id, str(reg_list))
        return 1
    if proverka("Дай Список"):
        mess(id, str(list_of_lakes))
        return 1
    if proverka("Установить День") and words and int(words[0]):
        put_obj(list_of_lakes, "day"+str(reg_list[0]))
        reg_list[0] = int(words[0])
        put_obj(reg_list, 'reg_list')
        mess(id, "Установлен день " + words[0])
        return 1
    if proverka("Сделать Ход"):
        global list_of_robots
        put_obj(list_of_lakes, "day"+str(reg_list[0]))
        game_dict, have_robot_list = make_game_dict(dict_of_dilogs, reg_list)
        list_of_robots, list_of_lakes = make_list_of_robots(dict_of_dilogs, game_dict, have_robot_list, list_of_lakes, reg_list)#роботы до диверсий
        do_game(game_dict, dict_of_dilogs, reg_list, list_of_lakes, list_of_robots, dict_of_dilogs)
        game_dict, have_robot_list = make_game_dict(dict_of_dilogs, reg_list)
        list_of_robots, list_of_lakes = make_list_of_robots(dict_of_dilogs, game_dict, have_robot_list, list_of_lakes, reg_list)#роботы после диверсий
        reg_list[0] += 1 #следующий день
        for i in range(1, len(list_of_lakes)):
            list_of_lakes[i]['k'] = k(list_of_lakes[i]['purity'])
        put('rl')
        return 1
    return 0

def answer_to_gamer():
    global dict_of_dilogs, list_of_lakes, list_of_robots
    if proverka("Ход"):
        day = reg_list[0]
        if len(words) > 0 and int(words[0]):
            day = max(day, int(words[0]))
            words.remove(words[0])
        h = make_hod_file(id, words, dict_of_dilogs, reg_list) #+
        s = get_obj(id+'-s'+str(reg_list[0]))
        h = red_hod_to_state(id, h, s, reg_list, dict_of_dilogs, list_of_lakes, list_of_robots) #have not diversion
        answer_for_hod(day, id, h, s)
        put_obj(h, id+'-h'+str(reg_list[0]))
        return 1

    if proverka("Помощь", remove=0):
        mess(id, 'В помощь игроку:\n"Дай"\n"Выйти Из Моего Озера"\n"Список"\n"Как сделать ход"\n')
    if proverka("Как Сделать Ход"):
        mess(id, как_сделать_ход)
        return 1
    if proverka("Sv_Cheats 1") and not(dict_of_dilogs[id]['cheat']): #len(words) > 1 and words[0] == "Sv_Cheats" and words[1] == '1':
        dict_of_dilogs[id]['cheat'] = '1'
        mess(id, "Читы включены")
        return 1

    if dil(id, словарь_подробнее, "Подробнее"):
        return 1

    if dict_of_dilogs[id]['cheat']:
        if proverka("Impuls 101"):
            string = id+'-s'+str(reg_list[0])
            s = get_obj(string)
            s['money'] += 1010
            s['level'] += 2
            put_obj(s, string)
            return 1

    if proverka("Дай"):
        if proverka("Озеро"):
            L = dict_of_dilogs[id]['lake']
            day = reg_list[0]
            proverka("№")
            if words:
                L = int_lake(id, words[0], reg_list)
            if not(L):
                return 1
            words.pop(0)
            if proverka("День") and words and int(words[0]) and int(words[0]) <= day:
                day = int(words[0])
            p_lake_day(id, list_of_lakes[L], day)
        if proverka("Состояние"):
            if words:
                if len(words[0]) > 1 and (words[0][0] == '-' or words[0][0] == '+') and words[0][1:].isdigit():
                    day = str(reg_list[0] + int(words[0]))
                elif words[0].isdigit():
                    day = words[0]
                else:
                    day = str(10000)
            else:
                day = str(reg_list[0])
            st = id + '-s' + day
            if os.path.exists('data/' + st + ".txt"):
                daiy_s(day, id)
                mess(id, "Состояние за день "+str(int(day))+' '+str(get_obj(st)))
            else:
                mess(id, "Файл не найден")
            return 1
        if proverka("Ход"):
            if words:
                if len(words[0]) > 1 and (words[0][0] == '-' or words[0][0] == '+') and words[0][1:].isdigit():
                    day = str(reg_list[0] + int(words[0]))
                elif words[0].isdigit():
                    day = words[0]
                else:
                    day = 10000
            else:
                day = str(reg_list[0])
            st = id + '-h' + day
            if os.path.exists('data/' + st + ".txt"):
                mess(id, "Ход за день "+day+' '+str(get_obj(st)))
            else:
                mess(id, "Файл не найден")
            return 1
        ster = 'Напишите\n "Дай ход", "Дай состояние" или "Дай озеро №[номер озера]", чтобы узнать свой ход или состояние за текущий день.\n"'
        ster += 'Дай ход 4" чтобы узнать ход за день 4\n"Дай состояние -1" чтобы узнать состояние за вчерашний день'
        mess(id, )
    return 0

def answer():
    while words and words[0] in privetstvie:
        if words[0] in privetstvie:
            mess(id, "И тебе привет, " + dict_of_dilogs[id]['obr'] + ' :-)')
            words.pop(0)
    if dict_of_dilogs[id]['admin']:
        if answer_to_admin():
            return 1
    if dict_of_dilogs[id]['status'] == 'Gamer':
        if answer_to_gamer():
            return 1
    return 0

mess(str(144520879), str(dict_of_dilogs))
#dict_of_dilogs['144520879']['date'] -= 1  # !!""""


for i in range(2000):
    res = vk.method('messages.get', values)
    for item in res['items']:
        id = str(item['user_id'])

        if item['body'][0] == 'Л':
            id = '140420515'
            item['body'] = item['body'][1:]
        if item['body'] and item['body'][0] == '/' and item['body'][1] == '/':
            continue
        if chek_list_of_dilogs():
            continue

        words = get_words(item['body'])
        print("Words:= ", words)

        #words = red_words(id, reg_list, dict_of_dilogs[id], words)
        #print("Words:= ", words)
        if len(words) > 0 and answer():
            continue


        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue


        if proverka("Какой Сейчас День"):
            mess(id, "Сегодня " + sPM(reg_list[0])+" день")
            continue

        if proverka("Называй Меня") and words:
            dict_of_dilogs[id]['obr'] = words[0]
            put("d")
            mess(id, 'Хорошо, товарищ ' + words[0])
            continue

        if proverka("Зарегистрировать Новое Озеро"):
            i, j = find_gemer(id, reg_list)
            dict = dict_of_dilogs[id]
            if dict['status'] == 'Gamer':
                mess(id, 'Вы уже зарегистрированны в озеро под названием {}'.format(reg_list[dict['lake']][0]))
            else:
                x, reg_list = lake_registation(id, reg_list)
                list_of_lakes.append(lake(reg_list[x][0], id))
                dict_of_dilogs[id]['status'] = "Gamer"
                dict_of_dilogs[id]['lake'] = x
                dict_of_dilogs[id]['nom'] = 1
                put("rld")
                mess(id, 'Появилось новое озеро под номером {}.\n'
                         'Название: {}\n'
                         'Сейчас на нём только один игрок: {}(Вы)'.format(x, "Озеро" + str(x), get_name(id)))
            continue

        if proverka("Список"):
            if not(words):
                mess(id, 'Возможные вариванты: "Список озёр"\n"Список роботов"\n"Список игрков на озере %название озера%"\n')
            if proverka("Озер"):
                pr_list(id, map(lambda x: x[0], reg_list[1:]))
                continue
            if proverka("Игроков На Озере"):
                if int_lake(id, words, reg_list):
                    p_gamers_on_lake(id, int_lake(words[0]))
                else:
                    mess(id, "Озера с таким названием нет")
                continue
            if proverka("Роботов"):
                list_of_robots = ['',]
                game_dict, have_robot_list = make_game_dict(dict_of_dilogs, reg_list)
                list_of_robots, list_of_lakes = make_list_of_robots(dict_of_dilogs, game_dict, have_robot_list, list_of_lakes, reg_list)
                pr_list(id, map(lambda x: x[0], list_of_robots[1:]))
                continue

        if proverka("Захожу В Озеро"):
            if dict_of_dilogs[id]['status'] == "Gamer":
                mess(id, 'Вы уже зарегистрированы в озеро под названием {}.\n'
                         'Чтобы войти в другое озеро, сначала выйдите из этого\n'.format(reg_list[dict_of_dilogs[id]['lake']][0]))
            else:
                for i in range(1,len(reg_list)):
                    if reg_list[i][0] == words[0]:
                        break
                if reg_list[i][0] != words[0]:
                    mess(id, "Озера с таким названием нет. Выберете озеро из списка озёр или создавайте своё.")
                    p_reg_list(id, reg_list)
                else:
                    reg_list[i].append(id)
                    mess(id, 'Вы успешно вошли в Озеро №{}.\n'
                             'Название: {}\n'
                             'Итого, список игроков на вашем озере:'.format(i, reg_list[i][0]))
                    p_gamers_on_lake(id, reg_list[i])
                    dict_of_dilogs[id]['status'] = 'Gamer'
                    dict_of_dilogs[id]['lake'] = i
                    dict_of_dilogs[id]['nom'] = len(reg_list[i]) - 1
                    put("rdl")
            continue


        if proverka("Выйти Из Моего Озера"):
            if dict_of_dilogs[id]['status'] != "Gamer":
                mess(id, "Вы и так не состоите ни в одном озере")
                continue
            elif dict_of_dilogs[id]['lake'] > 0:
                L = dict_of_dilogs[id]['lake']
                reg_list[L].remove(id)
                for i in range(dict_of_dilogs[id]['nom'], len(reg_list[L])): #если из списка 1 2 3 удалить втророй элемент, то должно остаться 1 2
                    dict_of_dilogs[reg_list[L][i]]['nom'] = i
                mess(id, "Вы вышли из озера и сейчас не зарегистрированы на игру")
                if len(reg_list[dict_of_dilogs[id]['lake']]) == 1:
                    reg_list[dict_of_dilogs[id]['lake']][0] = ''
                dict_of_dilogs[id]['status'] = 'New'
                dict_of_dilogs[id]['lake'] = 0
                dict_of_dilogs[id]['nom'] = 0
                put("rdl")
            continue

        if not(words):  # !!
            mess(id, 'непонятка:(')
            if not(dict_of_dilogs[id]['admin']):
                time.sleep(2)
                mess(id, dict_of_dilogs[id]['obr'] + ', может, напишешь:\n"Помощь"?')
    time.sleep(1)
