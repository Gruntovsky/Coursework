import requests
import json
import os
# Чтение токена для ВК
with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()

class User:
    """Скачивание фото с профиля VK"""
    def __init__(self,owner_id,count):
        self.owner_id = owner_id
        self.photos = []
        self.likes = []
        self.info = {}
        self.count = count
        self.get_photo(owner_id)
        self.load()
        self.check()

    def get_photo(self,owner_id):
        """ функция для получения url фотографий профиля пользователя"""
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.owner_id,
            'album_id': 'profile',
            'access_token': token,
            'v': '5.131',
            'rev': '0',
            'extended': '1',
            'photo_sizes': '0',
            'count': self.count,
        }
        res = requests.get(URL, params=params)
        result = res.json()
        for i in range(0,int(params['count'])): # Получаем url изображения размера 'r'
            photo = result.get('response').get('items')[i].get('sizes')
            self.likes.append(result.get('response').get('items')[i].get('likes')['count'])
            # pprint(result.get('response').get('items')[i].get('sizes'))
            for url in photo:
                if 'r' in url['type']:
                    self.info[f'{i}-url'] = url['url']
                    self.info[f'{i}-size'] = url['type']
                    self.info[f'{i}-name'] = f"{i}likes{self.likes[i]}.jpg"
                    self.photos.append(url['url'])
        return self.photos,self.likes

    def load(self):
        """Скачивание файлов по url"""
        for i in range(0, len(self.photos)):
            p = requests.get(self.photos[i])
            out = open(f"images/{i}likes{self.likes[i]}.jpg", "wb")
            out.write(p.content)
            out.close()
        return self.info

    def check(self):
        """"Запись Чек-листа"""
        with open('images/Check_list.json','w',encoding='utf-8') as f:
            json.dump(self.info,f,indent=2)