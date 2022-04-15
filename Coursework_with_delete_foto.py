from ya_disk import YandexDisk
from Vk_download import User
from tqdm import tqdm
import os

#552934290,5

def inputs():
    """"Входные данные"""
    id = input('Введите ID: ')
    count_photo = input('Введите количество фото: ')
    user=User(id,count_photo)

inputs()

def load_photos():
    file_path = os.getcwd()
    """Загрузка файлов на Яндекс диск"""
    files = os.listdir('images')
    with open('tokenYA.txt', 'r') as file_object:
        token_ya = file_object.read().strip()
    TOKEN = token_ya
    print('Загрузка фото на Я.Диск:')
    for file in tqdm(files):
        ya = YandexDisk(token=TOKEN)
        ya.upload_file_to_disk(f'Vk_photo/{file}',f'{file_path}/images/{file}')
        os.remove(f'{file_path}/images/{file}')

load_photos()




