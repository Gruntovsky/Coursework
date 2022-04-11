import os
from ya_disk import YandexDisk
from Vk_download import User
from tqdm import tqdm

#552934290,5

def inputs():
    """"Входные данные"""
    id = input('Введите ID: ')
    count_photo = input('Введите количество фото: ')
    user=User(id,5)

inputs()

def load_photos():
    """Загрузка файлов на Яндекс диск"""
    files = os.listdir('images')
    with open('tokenYA.txt', 'r') as file_object:
        token_ya = file_object.read().strip()
    TOKEN = token_ya
    for file in tqdm(files):
        ya = YandexDisk(token=TOKEN)
        ya.upload_file_to_disk(f'Vk_photo/{file}',f'C:/Users/Gregory/Desktop/py/Coursework/images/{file}')

load_photos()
