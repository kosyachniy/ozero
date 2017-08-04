import vk_api

Vano = vk_api.VkApi(login="79193540345", password='1йфячыц2')
Vano.auth()

#Vano.method('photos.createAlbum', {'title': "Проверка роботоспособности"})

server, photos_list, aid, hash,

x = Vano.method("photos.getUploadServer", {'album_id':246676489})
Vano.method("photos.save", {'album_id':246676489})
print(x)