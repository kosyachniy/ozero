from func import *
from lake import *
values = {'out':0, 'count':10, 'time_offset':3600}
#mess(144520879, 'Привет, я робот-помошник Тетрис-4.' + '\n'
#                'Не хочешь зарегестрироваться на игру Озеро?' + '\n'
#                'Напиши "Помощь" и узнаешь о чём со мной можно поговорить')



dict_of_dilogs = {} #словарь списков взаиможействий с людьми "id": ["Способ обращения"(str), "Дата последнего сообщения"(int)]
list_of_lakes = [] #список списков озёр list_of_lakes[номер озера(int)] == [название озера, id1, id2, id3 ...]
put_obj(list_of_lakes, 'list_of_lakes') #!!
dict_of_dilogs = get_obj('dict_of_dilogs')
list_of_lakes = get_obj('list_of_lakes')


kol_lakes = len(list_of_lakes)
for i in range(100):
    res = vk.method('messages.get', values)
    #print(res)
    for item in res['items']:
        id = item['user_id']
        if not(str(id) in dict_of_dilogs): #если с этим человеком мы ещё не разговривали, добавляем его в словарь
            dict_of_dilogs[str(id)] = ('Человек', item['date'])
            put_obj(dict_of_dilogs, 'dict_of_dilogs')
        elif (dict_of_dilogs[str(id)][1] >= item['date']): #отвечаем только на последние сообщения данного пользователя
            continue
        else:
            dict_of_dilogs[str(id)][1] = item['date']
            put_obj(dict_of_dilogs, 'dict_of_dilogs')

        words = get_words(item['body'])
        print("Words:= ", words)
        while len(words) > 0 and (words[0] in privetstvie or words[0] in Obrashenie):
            if words[0] in privetstvie:
                mess(id, "И тебе привет, " + dict_of_dilogs[str(id)][0] + ' :-)')
            words.remove(words[0])

        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue

        if proverka("Называй Меня", words):
            #len(words) > 2 and (words[0] == 'Называй' and words[1] == 'Меня'):
            dict_of_dilogs[str(id)][0] = words[2]
            put_obj(dict_of_dilogs, 'dict_of_dilogs')
            mess(id, 'Хорошо, товарищ ' + words[2])
            continue

        if proverka("Зарегистрировать Новое Озеро", words):
            i, j  = find_gemer(id, list_of_lakes)
            if j:
                mess(id, 'Вы уже зарегистрированны в озеро под названием {}'.format(list_of_lakes[i][0]))
            else:
                lake, kol_lakes = lake_registation(id, kol_lakes)
                list_of_lakes.append(["Озеро" + str(kol_lakes), id])
                put_obj(list_of_lakes, "list_of_lakes")
                mess(id, 'Появилось новое озеро под номером {}.\n'
                         'Название: {}\n'
                         'Сейчас на нём только один игрок с id: {}(Вы)'.format(kol_lakes, "Озеро" + str(kol_lakes), str(id)))
            continue

        if proverka("Список Озёр", words):
            if len(list_of_lakes) == 0:
                mess(id, "Озёр ещё нет")
            for i in range(len(list_of_lakes)):
                mess(id, list_of_lakes[i][0])
            continue

        if len(words) > 4 and proverka("Cписок Игроков На Озере", words):
            flag = 1 #нужно упростить
            for i in range(len(list_of_lakes)):
                if words[4] == list_of_lakes[i][0]:
                    print_gamers_on_lake(i, id, list_of_lakes)
                    flag = 0
                    break
            if flag:
                mess(id, "Озера с таким названием нет")
            continue

        if len(words) > 3 and proverka("Захожу В Озеро", words):
            i, j = find_gemer(id, list_of_lakes)
            if j:
                mess(id, 'Вы уже зарегистрированны в озеро под названием {}.\n'
                         'Чтобы войти в другое озеро, сначала выйдите из этого\n'.format(list_of_lakes[i][0]))
            else:
                i1, j1 = find_gemer(words[0], list_of_lakes)
                list_of_lakes[i1].append(id)
                put_obj(list_of_lakes, "list_of_lakes")
                mess(id, 'Вы успешно вошёли в Озеро под номером {}.\n'
                         'Название: {}\n'
                         'Итого, список игроков на этом озере:'.format(i+1, list_of_lakes[i1][0]))
                print_gamers_on_lake(i+1, id, list_of_lakes[i1][0])
            continue
        if len(words) > 0:
            mess(id, 'непонятка:(')
    time.sleep(2)