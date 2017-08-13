from lake import *
import os
time.clock()
list_of_lakes = get_obj('list_of_lakes')
dict_of_dilogs = get_obj('dict_of_dilogs')
reg_list = get_obj('reg_list')
list_of_robots = make_list_of_robots(list_of_lakes)
words = []

def proverka(st):
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if not (list[i] == words[i]):
            return 0
    return 1

def put(st):
    set0 = set(st)
    if 'r' in set0:
        put_obj(reg_list, 'reg_list')
    if 'l' in set0:
        put_obj(list_of_lakes, 'list_of_lakes')
    if 'd' in set0:
        put_obj(dict_of_dilogs, 'dict_of_dilogs')

def p_gamers_on_lake(id, lake):
    if len(lake) == 1:
        mess(id, "На озере " + lake[0] +" никого нет")
    else:
        for j in range(1, len(lake)):
            mess(id, '('+str(j)+')'+ get_name(lake[j]))
            mess(id, "Конец списка")

def chek_list_of_dilogs():
    if not(id in dict_of_dilogs):  # если с этим человеком мы ещё не разговривали, добавляем его в словарь
        x = Vano.method("users.get", {"user_ids": id})[0]
        dict_of_dilogs[id] = {"obr": x["first_name"], "date": item['date'], "first_name": x["first_name"],
                                   "last_name": x["last_name"], "status": 'New', "lake": 0, "nom": 0, "admin":0, "cheat": ""}  # !!
        if int(id) == 144520879 or int(id) == 140420515:
            dict_of_dilogs[id]['admin'] = 1
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
        for i in range(1, 20):
            put_obj(state(), id+'-s'+str(i))
            put_obj(hod(), id+'-h'+str(i))
    elif (dict_of_dilogs[id]['date'] >= item['date']):  # отвечаем только на последние сообщения данного пользователя
        return 1
    else:
        dict_of_dilogs[id]['date'] = item['date']
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
    return 0

def get_name(id):
    return dict_of_dilogs[id]['first_name'] + ' ' + dict_of_dilogs[id]['last_name']

values = {'out': 0, 'count': 10, 'time_offset': 3600}

def answer_to_admin():
    global list_of_lakes, dict_of_dilogs, reg_list, words
    if proverka("Помощь"):
        mess(id, "В помощь админу:\nОбнулить\nДай словарь\nДай список\nДай регистрацию\nУстановить день\nСделать ход\n")
    if proverka("Обнулить"):
        reg_list = [8, ]
        dict_of_dilogs = {}
        list_of_lakes = [0, ]
        put('rld')
        return 1
    if proverka("Дай Словарь"):
        mess(id, str(dict_of_dilogs))
        return 1
    if proverka("Дай Список"):
        mess(id, str(list_of_lakes))
        return 1
    if proverka("Дай Регистрацию"):
        mess(id, str(reg_list))
        return 1
    if proverka("Установить День") and words[2].isdigit():
        reg_list[0] = int(words[2])
        put_obj(reg_list, 'reg_list')
        mess(id, "Установлен день " + words[2])
        words = words[3:]
    if proverka("Сделать Ход"):
        global list_of_robots
        game_dict = {}
        for i in range(1, len(reg_list)):
            for j in range(1, len(reg_list[i])):
                g_id = reg_list[i][j]
                mess(id, "Закидываем игрока " + str(i) + str(j))
                if dict_of_dilogs[g_id]['lake'] != i or dict_of_dilogs[g_id]['nom'] != j: #на всякий случай. Защита от неправильной проги
                    mess(id, "Информация об игроке " + g_id + " некорректная")
                game_dict[g_id] = {}
                game_dict[g_id]['s'] = get_obj(id + '-s' + str(reg_list[0]))
                game_dict[g_id]['h'] = get_obj(id + '-h' + str(reg_list[0]))
        do_game(game_dict, dict_of_dilogs, reg_list, list_of_lakes, list_of_robots, dict_of_dilogs)
        list_of_robots = make_list_of_robots(list_of_lakes)
        reg_list[0] += 1
        for i in range(1, len(list_of_lakes)):
            list_of_lakes[i]['k'] = k(list_of_lakes[i]['purity'])
        put('rl')
        return 1
    return 0

def answer_to_gamer():
    global dict_of_dilogs
    if proverka("Помощь"):
        mess(id, 'В помощь игроку:\n"Дай"\n"Выйти Из Моего Озера"\n"Список"\n"Как сделать ход"\n')

    if proverka("Sv_Cheats 1"): #len(words) > 1 and words[0] == "Sv_Cheats" and words[1] == '1':
        dict_of_dilogs[id]['cheat'] = '1'
        mess(id, "Читы включены")
        return 1
    if dict_of_dilogs[id]['cheat'] and proverka("Impuls 101"):
        string = id+'-s'+str(reg_list[0])
        s = get_obj(string)
        s['money'] += 1010
        put_obj(s, string)
        return 1
    print(words)
    print(words[0])
    print(words[0] == 'Дай')
    if words[0] == "Дай":
        print("daiy")
        if len(words) == 1:
            mess(id, 'Напишите\n "Дай ход" или "Дай состояние", чтобы узнать свой ход или состояние за текущий день.\n"Дай ход 4" чтобы узнать ход за день 4\n"Дай состояние -1" чтобы узнать состояние за вчерашний день')
            print('len == 0')
            return 1
        if words[1] == 'Озеро':
            L = dict_of_dilogs[id]['lake']
            mess(id, str(list_of_lakes[L]))
            return 1
        if words[1] == "Состояние":
            if len(words) > 2:
                if len(words[2]) > 1 and (words[2][0] == '-' or words[2][0] == '+') and words[2][1:].isdigit():
                    day = str(reg_list[0] + int(words[2]))
                elif words[2].isdigit():
                    day = words[2]
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
        if words[1] == "Ход":
            if len(words) > 2:
                if len(words[2]) > 1 and (words[2][0] == '-' or words[2][0] == '+') and words[2][1:].isdigit():
                    day = str(reg_list[0] + int(words[2]))
                elif words[2].isdigit():
                    day = words[2]
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
    return 0

def answer():
    while len(words) > 0 and (words[0] in privetstvie or words[0] in Obrashenie):
        if words[0] in privetstvie:
            mess(id, "И тебе привет, " + dict_of_dilogs[id]['obr'] + ' :-)')
            words.remove(words[0])
    if len(words) == 0:
        return 1
    if dict_of_dilogs[id]['admin']:
        if answer_to_admin():
            return 1
    if dict_of_dilogs[id]['status'] == 'Gamer':
        if answer_to_gamer():
            return 1
    return 0


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
        if len(words) > 0 and answer():
            continue




        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue


        if len(words) > 2 and proverka("Дай Озеро") and words[2].isdigit():
            if len(list_of_lakes) > words[2]:
                mess(id, str(list_of_lakes[int(words[2])]))
            else:
                mess(id, "Озёр меньше, чем вы назвали")
            continue

        if proverka("Дай Роботов"):
            list_of_robots = make_list_of_robots(list_of_lakes)
            mess(id, str(list_of_robots))
            continue

        if proverka("Какой Сейчас День"):
            mess(id, "Сегодня " + sPM(reg_list[0])+" день")
            continue

        if proverka("Как Сделать Ход"):
            mess(id, "Раздел в разработке, уточните у Ивана")
            continue
        if len(words) > 2 and proverka("Называй Меня"):
            dict_of_dilogs[id]['obr'] = words[2]
            put("d")
            mess(id, 'Хорошо, товарищ ' + words[2])
            continue

        if proverka("Зарегистрировать Новое Озеро"):
            print('регистрируем')
            i, j = find_gemer(id, reg_list)
            dict = dict_of_dilogs[id]
            print(dict['status'])
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


        if proverka("Список Озер"):
            p_reg_list(id, reg_list)
            continue

        if len(words) > 4 and proverka("Список Игроков На Озере"):
            flag = 1  # нужно упростить
            for i in range(1, len(reg_list)):
                if words[4] == reg_list[i][0]:
                    p_gamers_on_lake(id, reg_list[i])
                    flag = 0
                    break
            if flag:
                mess(id, "Озера с таким названием нет")
            continue

        if len(words) > 3 and proverka("Захожу В Озеро"):
            if dict_of_dilogs[id]['status'] == "Gamer":
                mess(id, 'Вы уже зарегистрированы в озеро под названием {}.\n'
                         'Чтобы войти в другое озеро, сначала выйдите из этого\n'.format(reg_list[dict_of_dilogs[id]['lake']][0]))
            else:
                flag = 1
                for i in range(1,len(reg_list)):
                    if reg_list[i][0] == words[3]:
                        flag = 0
                        break
                if flag:
                    mess(id, "Озера с таким названием нет. Выберете озеро из списка озёр или создавайте своё.")
                    p_reg_list(id, reg_list)
                else:
                    reg_list[i].append(id)
                    list_of_lakes[i]['gamers'].append(id)
                    mess(id, 'Вы успешно вошёли в Озеро под номером {}.\n'
                             'Название: {}\n'
                             'Итого, список игроков на вашем озере:'.format(i, reg_list[i][0]))
                    p_gamers_on_lake(id, reg_list[i])
                    dict_of_dilogs[id]['status'] = 'Gamer'
                    dict_of_dilogs[id]['lake'] = i
                    dict_of_dilogs[id]['nom'] = len(reg_list[i]) - 1
                    put("rdl")
            continue

        if proverka("Ход"):
            words.remove(words[0])
            day = reg_list[0]
            if words[0].isdigit():
                day = max(day, int(words[0]))
                words.remove(words[0])
            h = make_hod_file(id, words) #+
            list_of_robots = make_list_of_robots(list_of_lakes) #+
            s = get_obj(id+'-s'+str(reg_list[0]))
            h = red_hod_to_state(id, h, s, reg_list, dict_of_dilogs, list_of_lakes, list_of_robots) #have not diversion
            anser_for_hod(day, id, h, s)
            put_obj(h, id+'-h'+str(reg_list[0]))
            continue

        if proverka("Выйти Из Моего Озера"):
            if dict_of_dilogs[id]['status'] != "Gamer" and dict_of_dilogs[id]['lake'] != 0:
                mess(id, "Вы и так не состоите ни в одном озере")
                continue
            elif dict_of_dilogs[id]['lake'] > 0 and dict_of_dilogs[id]['nom'] > 0:
                x = dict_of_dilogs[id]
                reg_list[x['lake']].pop(x['nom'])
                for i in range(x['nom'], len(reg_list[x['lake']])):
                    dict_of_dilogs[reg_list[x['lake']][i]]['nom'] = i
                mess(id, "Вы вышли из озера и сейчас не зарегистрированы на игру")
                if len(reg_list[x['lake']]) == 1:
                    reg_list[x['lake']][0] = ''
                dict_of_dilogs[id]['status'] = 'New'
                dict_of_dilogs[id]['lake'] = 0
                dict_of_dilogs[id]['nom'] = 0
                put("rdl")
            else:
                mess(id, "Вы и сейчас не в озере. Откуда выходить то?")
            continue

        if len(words) > 0:  # !!
            mess(id, 'непонятка:(')
            if not(dict_of_dilogs[id]['admin']):
                time.sleep(2)
                mess(id, dict_of_dilogs[id]['obr'] + ', может, напишешь:\n"Помощь"?')
    time.sleep(1)
