from func import *
from lake import *

mess(144520879, 'Привет, я робот-помошник Тетрис-4.' + '\n'
                'Не хочешь зарегестрироваться на игру Озеро?' + '\n'
                'Напиши "Помощь" и узнаешь о чём со мной можно поговорить')
#mess(135524838, 'Слыш, ты!')

d = {'t': 100}
print(d)
print(d['t'])

values = {'out':0, 'count':10, 'time_offset':3600}

dict_of_dilogs = {'144520879': ('Вано', 1500828375)} #словарь кортежей. id: ("Способ обращения"(str), "Дата последнего сообщения"(int))
put_obj(dict_of_dilogs, 'dict_of_dilogs')
dict_of_dilogs = loads(get_obj('dict_of_dilogs'))


print(dict_of_dilogs)
print(type(dict_of_dilogs))
dict_of_dilogs['t'] = 1
print(dict_of_dilogs['t'])
kol_lakes = 0
for i in range(100):
    res = vk.method('messages.get', values)
    #print(res)
    if res['items']:
        values['last_message_id'] = res['items'][0]['id']
    for item in res['items']:
        id = item['user_id']
        print(str(id))
        print(dict_of_dilogs[str(id)])
        if not(str(id) in dict_of_dilogs):
            dict_of_dilogs[str(id)] = ('Человек', item['date'])
        elif (dict_of_dilogs[str(id)][1] > item['date']): #отвечаем только на последние сообщения данного пользователя
            continue
        else:
            dict_of_dilogs[id][1] = item['date']
        words = get_words(item['body'])
        if words[0] in privetstvie:
            mess(id, "И тебе привет " + dict_of_dilogs[id] + ' :-)')
            words.remove(words[0])

        if len(words) == 1 and words[0] in slovarni_zapas_oneword:
            mess(id, slovarni_zapas_oneword[words[0]])
            continue
            """
            lake, kol_lakes = lake_registation(item['user_id'], kol_lakes)
            mess(item['user_id'],
                 'Ваше озеро под номером {} зарегистрированно'.format(kol_lakes))
                 """
        if len(words) > 0:
            mess(id, 'непонятка(')
    time.sleep(8)


#t=s.split()

for i in range(100):
    res = vk.method('messages.get', values)
    print(res)
    print()
    if res['items']:
        values['last_message_id'] = res['items'][0]['id']
    #print(res['items'])
    for item in res['items']:
        t = item['body'].split()
        for word in t:
            if word in Oskorbleniye:
                oskorbi(word, item)
                continue
        answer(item)

    time.sleep(1)

#for i in range(10)
#    res = vk.method('messages.get', value1)
#    if res['items']:
#        value1['last_message_id'] = res['items'][0]['id']