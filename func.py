from strings import *

def put_obj(obj, s):
    with open('data/' + s + '.txt', 'w') as f:
        print(dumps(obj), file = f)

def get_obj(s):
    with open('data/' + s + '.txt', 'r') as f:
        return loads(f.read())

INT = int
def integer(st):
    if not(st):
        return 0
    if type(st) == list_type:
        if st:
            st = st[0]
        else:
            return 0
    if st.isdigit():
        return INT(st)
    return 0
int = integer


def get_words(S):
    S = S + '%'
    lister = set(',! :?%"ёЁ№#')  # символы подлежащие удалению и изменению
    words = []
    flag = 1
    L = len(S)
    i = 0
    st = ""
    while i < L:
        if flag:
            if S[i] in lister:
                if S[i] == ' ' or S[i] == '%' or S[i] == '№' or S[i] == '#':
                    if st:
                        words.append(st.title())
                        st = ""
                    if S[i] == '№' or S[i] == '#':
                        words.append('№')
                elif S[i] == 'Ё' or S[i] == 'ё':
                    st += 'е'
            else:
                st += S[i]
        else:
            if S[i] != '%':
                st += S[i]
        if S[i] == '%':
            if st:
                if flag:
                    words.append(st.title())
                else:
                    words.append(st)
                st = ''
            flag = not(flag)
        i += 1
    return words

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

def p_reg_list (id, reg_list):
    if len(reg_list) == 1:
        mess(id, "Озёр ещё нет")
    else:
        for i in range(1, len(reg_list)):
            if reg_list[i][0]: #Если название озера не пустое
                mess(id, reg_list[i][0])
        mess(id, "Конец списка.")

def find_gemer(id, reg_list):
    for i in range(1, len(reg_list)):
        for j in range(1, len(reg_list[i])):
            if id == reg_list[i][j]:
                return i, j
    return -1, -1

def make_game_dict(dict_of_dilogs, reg_list):
    game_dict = {}
    have_robot_list = []
    for i in range(1, len(reg_list)):
        for j in range(1, len(reg_list[i])):
            g_id = reg_list[i][j]
            #mess(id, "Закидываем игрока " + str(i) + str(j))
            if dict_of_dilogs[g_id]['lake'] != i or dict_of_dilogs[g_id]['nom'] != j: #на всякий случай. Защита от неправильной проги
                mess(144520879, "Информация об игроке " + g_id + " некорректная")
            game_dict[g_id] = {}
            game_dict[g_id]['s'] = get_obj(g_id + '-s' + str(reg_list[0]))
            game_dict[g_id]['h'] = get_obj(g_id + '-h' + str(reg_list[0]))
            if game_dict[g_id]['s']['robot'][0]:
                have_robot_list.append(g_id)
    return game_dict, have_robot_list

def lake_registation(id, reg_list):
    i = 1
    L = len(reg_list)
    while i < L and len(reg_list[i]) != 1:
        i += 1
    if i == L:
        reg_list.append(["Озеро" + str(i), id])
    else:
        reg_list[i] = ["Озеро" + str(i), id]
    return i, reg_list

def get_id(st):
    if st.isdigit():
        return st
    x = Vano.method('utils.resolveScreenName', {'screen_name': st})
    if x['type'] == 'user':
        return x['object_id']
    return ''


def Приглашаю(id, words, dict_of_dilogs):
    get_name = lambda id: dict_of_dilogs[id]['first_name'] + ' ' + dict_of_dilogs[id]['last_name']
    dilogs_keys = dict_of_dilogs.keys()
    for i in range(len(words)):
        st = words[i]
        if st[:15] == 'https://vk.com/':
            st = st[15:]
        elif st[:7] == 'vk.com/':
            st = st[7:]
        chel_id = get_id(st)
        if chel_id:
            if chel_id in dilogs_keys:
                x = dict_of_dilogs[chel_id]
                if x['status'] == 'Gamer':
                    mess(id, "Игрок "+get_name(chel_id)+" уже сам зарегистрировался на озеро №"+int(x['lake']))
                elif x['status'] == 'Invited':
                    mess(id, "Игрока "+get_name(chel_id)+" уже кто-то пригласил в озеро №"+int(x['lake']))
            if is_they_friends(id, chel_id):
                x = get_user(chel_id)
                dict_of_dilogs[chel_id] = {"obr": x["first_name"], "date": 0, "first_name": x["first_name"],
                                       "last_name": x["last_name"], "status": 'invited', "lake": 0, "nom": 0, "admin":0, "cheat": ""}
                mess(id, "Пользователь "+get_name(chel_id)+" получит приглашение и инструкцию, как вступить в озеро под номером "+str(dict_of_dilogs[id]['lake']))
            else:
                chel = get_user(chel_id)
                mess(id, "Пользователь "+chel['first_name']+' '+chel['last_name']+" не является вашим другом")
        else:
            mess(id, "Простите, "+dict_of_dilogs[id]['obr']+', я не смог найти пользователя ВК по ссылке "'+words[i]+'" Возможно, вы не окружили ссылку процентиками\n Пример: "%https://vk.com/id144520879%"')
    return dict_of_dilogs
def sPM(x): #строчку в порядковое числительное муржского рода
    st = ''
    if x == 1:
        st = 'первый'
    elif x == 2:
        st = 'второй'
    elif x == 3:
        st = 'третий'
    elif x == 4:
        st = 'четвётрый'
    elif x == 5:
        st = 'пятый'
    elif x == 6:
        st = 'шестой'
    elif x == 7:
        st = 'с ₽ьмой'
    elif x == 8:
        st = 'восьмой'
    elif x == 9:
        st = 'девятый'
    elif x == 10:
        st = 'десятый'
    elif x == 11:
        st = 'одиннадцатый'
    elif x == 12:
        st = 'двенадцатый'
    elif x == 13:
        st = 'тринадцатый'
    elif x == 14:
        st = 'четырнадцатый'
    elif x == 15:
        st = 'пятнадцатый'
    elif x == 16:
        st = 'шестнадцатый'
    elif x == 17:
        st = 'семнадцатый'
    else:
        st = str(x)
    return st

def sKM(x): #строчку в числительно
    st = ''
    if x == 0:
        st == 'ноль'
    elif x == 1:
        st = 'один'
    elif x == 2:
        st = 'два'
    elif x == 3:
        st = 'три'
    elif x == 4:
        st = 'четыре'
    elif x == 5:
        st = 'пять'
    elif x == 6:
        st = 'шесть'
    elif x == 7:
        st = 'семь'
    elif x == 8:
        st = 'восемь'
    elif x == 9:
        st = 'девять'
    elif x == 10:
        st = 'десять'
    elif x == 11:
        st = 'одиннадцать'
    elif x == 12:
        st = 'двенадцать'
    elif x == 13:
        st = 'тринадцать'
    elif x == 14:
        st = 'четырнадцать'
    elif x == 15:
        st = 'пятнадцать'
    elif x == 16:
        st = 'шестнадцать'
    elif x == 17:
        st = 'семнадцать'
    else:
        st = str(x)
    return st

def дай_озеро(id, Lake):
    st = Lake['name']
    st += '\nЧистота '+str(Lake['purity'])+', k:='+str(Lake['k'])
    st += '\n '+str(len(Lake['yaxt']))+' яхт\n'+str(len(Lake['park']))+' парков\n'
    st += str(len(Lake['robot'])) + ' роботов\n'
    mess(id, st)

def daiy_s(day, id):
    s = get_obj(id+'-s'+str(day))
    st = "Cостояние за день " + str(day)
    st += "\nВ кармане "+str(s['money'])+"  ₽\nНа складе "+str(s['musor'])+"  едениц отходов\nУровень производства "+str(s['level'])+"\n"
    if s['clean_level']:
        st += "Уровень фильтра "+str(s['clean_level']) + "/10\n"
    if s['lobster']:
        st += "Вы ужинали лобстерами "+sKM(s['lobster'])+" раз\n"
    if s['yaxt']:
        st += sKM(len(s['yaxt'])).title()+" ваши гордые яхты плавают в озере\n"
    if s['park']:
        st += "Вы посторили "+sKM(len(s['park']))+" парк аттракционов\n"
    if s['robot'][0]:
        st += "Робот " + s['robot'][0] + " с защитой "+sKM(s['robot'][1]) + " работает без перебоев\n"
    mess(id, st)

def p_lake_day(id, lake, day):
    st = lake['name']+", день "+str(day)+":"#+str(lake)
    st += "\n Чистота "+str(lake['purity'])+"(k="+str(lake['k'])+")\n"
    if lake['yaxt'] or lake['robot'][1:] or lake['park']:
        if lake['yaxt']:
            st += str(len(lake['yaxt']))+" яхт\n"
        if lake['robot'][1:]:
            st += str(len(lake['robot']) - 1)+" роботов\n"#-1 есть!
        if lake['park']:
            st += str(len(lake['park']))+" парков\n"
    else:
        st += "Нет ни яхт, ни роботов-чистильщиков, ни парков"
    mess(id, st)

def pr_list(id, list):
    k = 0
    for i in list:
        k += 1
        mess(id, '('+str(k)+')'+i)
    if k:
        mess(id, "Конец списка")
    else:
        mess(id, "Пусто")

def int_lake(id, st, reg_list): #Поиск номера озера по номеру или названию
    if type(st) == list_type: #Если вдруг это список, то обрабатываем первый элемент списка и неадеемся на строчку
        if st:
            st = st[0]
        else:
            return 0
    if type(st) == int_type: #если строчка не номер, пишем сообщение
        return st
    if st.isdigit(): #если строчка переводится в число,
        st = int(st) #тогда полоучаем число
        if st < len(reg_list):
            return st
        return 0
    for i in range(1, len(reg_list)): #если строчка не переводится в число, проверяем, вдруг это назввание озера
        if st == reg_list[i][0]: #коль нашли такое название, заменяем строчку на номер
            st = i
            break
    if type(st) == int_type:
        return st
    else:
        mess(id, 'Такого озера нет\nСверьтесь с разделом "Список озёр"')
