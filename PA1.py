from flask import Flask, request, json
import vk_api
import random
app = Flask(__name__)
TOKEN = 
CONFIRMATION_TOKEN = 
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
@app.route('/', methods=['POST'])
def bot_handler():
    data = request.get_json()
    if data.get('type') == 'confirmation':
        return 'd4c85a7e'
    elif data.get('type') == 'message_new':
          msg_object = data['object']['message']
          user_id = msg_object['from_id']
          vk.messages.send(
             user_id=user_id,
             message="Привет, я начинающий разработчик Арктический Пингвин, это тестовый бот!",
             random_id=random.getrandbits(64))
          return 'ok'
