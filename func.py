import vk_api

vk=vk_api.VkApi(token='5998b265c9a37305498547c92781806b617eb4fe01131cc738d877a5d29b45beb8600d4371980cb525910')
vk.auth()

mess=lambda id, t: vk.method('messages.send', {'user_id':id, 'message':t})