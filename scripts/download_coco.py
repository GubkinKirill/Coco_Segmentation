import os
import requests
from tqdm import tqdm
import zipfile


base_dir = 'data/coco'
image_dir = os.path.join(base_dir, 'images')
annotations_dir = os.path.join(base_dir, 'annotations')

os.makedirs(image_dir, exist_ok=True)
os.makedirs(annotations_dir, exist_ok=True)

urls = {
    'train2017': 'http://images.cocodataset.org/zips/train2017.zip',
    'val2017': 'http://images.cocodataset.org/zips/val2017.zip',
    'test2017': 'http://images.cocodataset.org/zips/test2017.zip',
    'annotations_trainval2017': 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
}

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(destination, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar

    if total_size != 0 and progress_bar.n != total_size:
        print('Ошибка: Загрузка не удалась')

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

for name, url in urls.items():
    print(f'Загрузка {name}...')
    zip_path = os.path.join(base_dir, f'{name}.zip')

    download_file(url, zip_path)

    print(f'Распаковка {name}...')
    if 'annotations' in name:
        extract_zip(zip_path, annotations_dir)
    else:
        extract_zip(zip_path, image_dir)
    
    os.remove(zip_path)
    print(f'{name} загружен и распакован')

print('Все файлы загружены и распакованы')   


     