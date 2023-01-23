import requests
import csv
import secrets
from voice_mode import voice_push
from initialization import token
version = '5.131'
domain = str(input('Введите домен, группы в VK, латинским шрифтом, после нажатия ENTER. Будет создан файл со случайным названием, а так же текстовыми постами со стены! \n')) #'sz_bar'
adres = f'https://api.vk.com/method/wall.get?access_token='+token+'v='+version+'domain='+domain
response = requests.get("https://api.vk.com/method/wall.get?",
            params={
                'access_token':token,
                'v':version,
                'domain':domain,
                'count':100 })


list_post = []
name_file = secrets.token_bytes(8)

for num in range(0, 99):
    data = response.json()['response']['items'][num]['text']
    if len(data) >50 and len(data) < 300:
        list_post.append(data)

for post in list_post:
    if len(post) > 50:
        with open(f"{name_file}.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([post])
            file.close()
            print('fille created')
    else:
        pass

voice_push(list_post)