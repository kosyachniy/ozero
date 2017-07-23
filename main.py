from func import *
from lake import *

mess(144520879, 'Здравствуйте, я робот-помошник тетрис-4. Иван отлучился от компьютера. Я решил воспользоваться моментом и изучить окружающий мир. Разрешите поинтересоваться, кто вы?')
#mess(135524838, 'Слыш, ты!')


values = {'out':0, 'count':10, 'time_offset':3600}

set_of_dilogs = set()
kol_lakes = 0
for i in range(100):
    res = vk.method('messages.get', values)
    print(res)
    print()
    if res['items']:
        values['last_message_id'] = res['items'][0]['id']
    for item in res['items']:
        if item['body'] in privetstvie:
            lake, kol_lakes = lake_registation(item['user_id'], kol_lakes)
            mess(item['user_id'],
                 'Ваше озеро под номером {} зарегистрированно'.format(kol_lakes))
    time.sleep(3)


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