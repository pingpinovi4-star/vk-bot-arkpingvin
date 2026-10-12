import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
vk_session = vk_api.VkApi(token=")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print("Ура! Бот открыт!")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
       vk.messages.send(
           user_id=event.user_id,
           message="Привет, я начинающий разработчик Арктический Пингвин, это тестовый бот!",
           random_id=0)
