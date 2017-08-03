import vk_api

Vano = vk_api.VkApi(login="79193540345", password='1йфячыц2')
Vano.auth()

values = {'out': 0, 'count': 10, 'time_offset': 180}

res = Vano.method('messages.get', values)
print(res)