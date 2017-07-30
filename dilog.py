from lake import *

def chek_list_of_dilogs():
    if not (str(id) in dict_of_dilogs):  # если с этим человеком мы ещё не разговривали, добавляем его в словарь
        print(id)
        x = Vano.method("users.get", {"user_ids": id})[0]
        dict_of_dilogs[str(id)] = {"obr": x["first_name"], "date": item['date'], "first_name": x["first_name"],
                                   "last_name": x["last_name"], "status": 'New'}  # !!
        if id == 144520879 or id == 140420515:
            dict_of_dilogs[str(id)]["status"] = 'Admin'
        print("Добавляем ", dict_of_dilogs[str(id)])
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
    elif (dict_of_dilogs[str(id)]['date'] >= item['date']):  # отвечаем только на последние сообщения данного пользователя
        return 1
    else:
        dict_of_dilogs[str(id)]['date'] = item['date']
        put_obj(dict_of_dilogs, 'dict_of_dilogs')
    return 0

values = {'out': 0, 'count': 10, 'time_offset': 20}

dict_of_dilogs = get_obj('dict_of_dilogs')


dict_of_dilogs['144520879']['date'] -= 1  # !!



while True:
    res = Vano.method('messages.get', values)
    #print(res)
    for item in res['items']:
        id = item['user_id']
        print(item)
        if id > 0 and chek_list_of_dilogs():
            continue
        if id == 58115079:
            Vano.method("messages.send", {'user_id':id, 'sticker_id': 48})
    time.sleep(1)