import json
import yaml
import os

annotations_path = '../Coco_Segmentation/data/coco/annotations/annotations/instances_train2017.json'

with open(annotations_path, 'r') as f:
    data = json.load(f)

categories = data['categories']
class_names = {cat['id']: cat['name'] for cat in categories}

yaml_data = {
    "path": "coco_project/data/coco",
    "train": "images/train2017",
    "val": "images/val2017",
    "test": "images/test2017",
    "names": class_names,
}

yaml_path = '../Coco_Segmentation/data/coco.yaml'
with open(yaml_path, 'w') as f:
    yaml.dump(yaml_data, f, default_flow_style=False)

print(f'Файл {yaml_path} создан')