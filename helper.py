import vk_api
import time
chelovek = vk_api.VkApi(login = '79193540345', password = '1йфячыц2')
soobshestvo = vk_api.VkApi(token='5998b265c9a37305498547c92781806b617eb4fe01131cc738d877a5d29b45beb8600d4371980cb525910')
soobshestvo.auth()
chelovek.auth()


for i in range(0, 6):
    print(i, lx[i] == l2[i])

if st1 == st2:
    print("1 == 2")
if st2 == st3:
    print("2 == 3")
if st3 == st4:
    print("3 == 4")



values = {'out':0, 'count':10, 'time_offset':800}
#res = soobshestvo.method('messages.geыt', values)
#print(res)

for i in range(10000):
    res = chelovek.method('messages.get', values)
    for item in res['items']:
        id = item['user_id']
        if id == 58115079:
            chelovek.method("message.get", {'sticker_id': 48})
    time.sleep(0.5)
"""
id = 140420515
id_pol = 144532083
soobshestvo.method("messages.send", {"user_id": 144520879,
                                     'attachments': {
                                         'type': 'sticker',
                'sticker': {'id': 14, 'product_id': 1, 'photo_64': 'https://vk.com/images/stickers/14/64b.png',
                                                        'photo_128': 'https://vk.com/images/stickers/14/128b.png',
                                                        'photo_256': 'https://vk.com/images/stickers/14/256b.png',
                                                        'photo_352': 'https://vk.com/images/stickers/14/352b.png',
                                                        'photo_512': 'https://vk.com/images/stickers/14/512b.png',
                                                            'width': 232, 'height': 256}}})



id = 144520879
for i in range(1,100):
    dict = {'user_id': id, 'sticker_id': i}
    chelovek.method('messages.send', dict)
    time.sleep(1)
    soobshestvo.method('messages.send', dict)
    time.sleep(1)
"""