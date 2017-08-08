from lake import *


words = []

def proverka(st):
    list = st.split()
    if len(list) > len(words):
        return 0
    for i in range(len(list)):
        if not(list[i] == words[i]):
            return 0
    return 1