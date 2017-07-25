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
    print(res)
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

        if len(words) > 2 and (words[0] == 'Называй' and words[1] == 'Меня'):
            dict_of_dilogs[str(id)][0] = words[2]
            put_obj(dict_of_dilogs, 'dict_of_dilogs')
            mess(id, 'Хорошо, товарищ ' + words[2])
            continue
        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue
        if len(words) > 2 and (words[0] == 'Зарегистрировать' and words[1] == 'Новое' and words[2] == 'Озеро'):
            lake, kol_lakes = lake_registation(id, kol_lakes)
            list_of_lakes.append(["Озеро" + str(kol_lakes), id])
            put_obj(list_of_lakes, "list_of_lakes")
            #put_obj(dict_of_dilogs, 'L(' + str(kol_lakes) + '):Lake' + str(kol_lakes) + '-day00')
            mess(id,
                 'Ваше озеро под номером {} зарегистрированно на пользователя с id: {}'.format(kol_lakes, str(id)))
            continue
        if len(words) > 0:
            mess(id, 'непонятка(')
    time.sleep(7)