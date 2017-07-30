from lake import *

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
                                   "last_name": x["last_name"], "status": 'New', "lake": 0, "nom": 0}  # !!
        if id == 144520879 or id == 140420515:
            dict_of_dilogs[id]["status"] = 'Admin'
        print("Добавляем ", dict_of_dilogs[id])
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
    elif (dict_of_dilogs[id]['date'] >= item['date']):  # отвечаем только на последние сообщения данного пользователя
        return 1
    else:
        dict_of_dilogs[id]['date'] = item['date']
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
    return 0

def get_name(id):
    return dict_of_dilogs[id]['first_name'] + ' ' + dict_of_dilogs[id]['last_name']

values = {'out': 0, 'count': 10, 'time_offset': 3600}

#dict_of_dilogs = {}  # словарь списков взаиможействий с людьми
list_of_lakes = [0,]  # список списков озёр list_of_lakes[номер озера(int)] == [название озера, id1, id2, id3 ...]
"""
list_of_lakes - список списков
[(int)сегондяшний день, ["название озера1", ["название озера2", [...], [...], ...] 
                        id11,            id21,         
                        id12,            id22,    
                        id13,            id23         
                        ...                 ...
                         ]                  ]               

"""
#put_obj(list_of_lakes, 'list_of_lakes')  # !!
#put_obj(dict_of_dilogs, 'dict_of_dilogs')
dict_of_dilogs = get_obj('dict_of_dilogs')
list_of_lakes = get_obj('list_of_lakes')

dict_of_dilogs['144520879']['date'] -= 1  # !!
dict_of_dilogs['144520879']['lake'] = 0
dict_of_dilogs['144520879']['nom'] = 0
dict_of_dilogs['144520879']["status"] = 'Admin'


today = 8  # !!
list_of_lakes[0] = today

for i in range(200):
    res = vk.method('messages.get', values)
    # print(res)
    for item in res['items']:
        id = str(item['user_id'])

        if chek_list_of_dilogs():
            continue

        if item['body'][0] == '/' and item['body'][1] == '/':
            continue
        words = get_words(item['body'])
        print("Words:= ", words)
        while len(words) > 0 and (words[0] in privetstvie or words[0] in Obrashenie):
            if words[0] in privetstvie:
                mess(id, "И тебе привет, " + dict_of_dilogs[id]['obr'] + ' :-)')
            words.remove(words[0])

        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue

        if proverka("Смайлик", words):
            mess(id, "Да, смайлик) И не такое умею")

        if proverka("Как Сделать Ход", words):
            mess(id,
                 'Ваше сообщение должно начинаться со слова "Ход". Далее через пробел необязательное целое число - дата, за какой день делается ход.\n'
                 'Далее неважно где вы можете добавить в сообщение некоторые из необязательных слов или просто первую букву слова:\n'
                 'x, y - целые числа\n'
                 'z - действительное число\n'
                 '("Мусорю" или "М") z\n'
                 '("Чищу" или "Ч")\n'
                 '("Атакую" или "А") x\n'
                 '("Диверсия" или "Д") x y\n'
                 '("Спонсирую" или "С") x y\n')
            continue

        if proverka("Называй Меня", words):
            dict_of_dilogs[id]['obr'] = words[2]
            put_obj(dict_of_dilogs, 'dict_of_dilogs')
            mess(id, 'Хорошо, товарищ ' + words[2])
            print(dict_of_dilogs[id]['obr'])
            continue

        if proverka("Зарегистрировать Новое Озеро", words):
            i, j = find_gemer(id, list_of_lakes)
            if j != -1:
                mess(id, 'Вы уже зарегистрированны в озеро под названием {}'.format(list_of_lakes[i][0]))
            else:
                x, list_of_lakes = lake_registation(id, list_of_lakes)
                put_obj(list_of_lakes, "list_of_lakes")
                dict_of_dilogs[id]['status'] = "Gamer"
                dict_of_dilogs[id]['lake'] = x
                dict_of_dilogs[id]['nom'] = 1
                mess(id, 'Появилось новое озеро под номером {}.\n'
                         'Название: {}\n'
                         'Сейчас на нём только один игрок: {}(Вы)'.format(x, "Озеро" + str(x),
                                                                               dict_of_dilogs[id]['first_name'] + ' ' + dict_of_dilogs[id]['last_name']))
            continue

        if proverka("Список Озер", words):
            p_list_of_lakes(id, list_of_lakes)
            continue

        if len(words) > 4 and proverka("Список Игроков На Озере", words):
            flag = 1  # нужно упростить
            for i in range(1, len(list_of_lakes)):
                if words[4] == list_of_lakes[i][0]:
                    p_gamers_on_lake(id, list_of_lakes[i])
                    flag = 0
                    break
            if flag:
                mess(id, "Озера с таким названием нет")
            continue


        if len(words) > 3 and proverka("Захожу В Озеро", words):
            if dict_of_dilogs[id]['status'] == "Gamer":
                mess(id, 'Вы уже зарегистрированны в озеро под названием {}.\n'
                         'Чтобы войти в другое озеро, сначала выйдите из этого\n'.format(list_of_lakes[dict_of_dilogs[id]['lake']][0]))
            else:
                flag = 1
                for i in range(1,len(list_of_lakes)):
                    print(list_of_lakes)
                    print(list_of_lakes[i])
                    if list_of_lakes[i][0] == words[3]:
                        flag = 0
                        break
                if flag:
                    mess(id, "Озера с таким названием нет. Выберете озеро из списка озёр или создавайте своё.")
                    p_list_of_lakes(id, list_of_lakes)
                else:
                    list_of_lakes[i].append(id)
                    put_obj(list_of_lakes, "list_of_lakes")
                    mess(id, 'Вы успешно вошёли в Озеро под номером {}.\n'
                             'Название: {}\n'
                             'Итого, список игроков на вашем озере:'.format(i, list_of_lakes[i][0]))
                    dict_of_dilogs[id]['status'] == 'Gamer'
                    dict_of_dilogs[id]['lake'] == i
                    dict_of_dilogs[id]['nom'] == len(list_of_lakes[i]) - 1
                    p_gamers_on_lake(i, id, list_of_lakes[i])
            continue

        if proverka("Ход", words):
            words.remove(words[0])
            day = list_of_lakes[0]
            if words[0].isdigit():
                day = max(today, int(words[0]))
                words.remove(words[0])
            anser_for_hod(day, id, make_hod_file(day, id, words))
            continue

        if proverka("Выйти Из Моего Озера", words):
            if dict_of_dilogs[id]['status'] != "Gamer":
                mess(id, "Вы и так не состоите ни в одном озере")
                continue
            else:
                x = dict_of_dilogs[id]
                list_of_lakes[x['lake']].pop(x['nom'])
                for i in range(x['nom'], len(list_of_lakes[x['lake']])):
                    dict_of_dilogs[list_of_lakes[x['lake']][i]]['nom'] = i
                mess(id, "Вы вышли из озера и сейчас не зарегистрированны на игру")
                dict_of_dilogs[id]['status'] = 'New'
                put_obj(dict_of_dilogs, "dict_of_dilogs")
                put_obj(list_of_lakes, "list_of_lakes")
            continue


        if len(words) > 0:  # !!
            mess(id, 'непонятка:(')
            if dict_of_dilogs[id]['status'] != 'Admin':
                time.sleep(2)
                mess(id, dict_of_dilogs[id]['obr'] + ', может, напишешь:\n"Помощь"?')
    time.sleep(3)