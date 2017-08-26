

def proverka(st):
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if not (list[i] == words[i]):
            return 0
    return 1

def dil(id, dict, main_st, words):
    print('in dill')
    print(proverka(main_st))
    if not(proverka(main_st)):
        print(words)
        print(main_st)
        print('not')
        return 0
    words.remove(words[0])
    keys = game.keys()
    print('go')
    if not(len(words)):
        st = ""
        for string in keys:
            st += main_st + ' ' + string + '\n'
            mess(id, st)
            return 1
    for string in keys:
        if proverka(string):
            dict[string](id)
            return 1
    return 0
