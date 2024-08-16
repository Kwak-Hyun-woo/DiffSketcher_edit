import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision
import torchvision.transforms as transforms
import numpy as np
from torch.utils import data
from PIL import Image
import numpy as np
import os

from PIL import Image

IMG_EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def is_feature_file(filename):
    return filename == 'features.pt'

def is_angles_file(filename):
    return filename == 'camera_angle.pt'


def make_dataset(dir):
    images = []

    assert os.path.isdir(dir), '%s is not a valid directory' % dir
    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                images.append(path)
    return images


class Sketchdataset(data.Dataset):
    def __init__(self, root, opt, transform=None, mode='train', target = "ws"):   # target = z, ws or tri_plane
        sketch_root = os.path.join(root, "sketch")
        
        # input: sketch image, target: z, w or tri-plane of real image
        self.sketch_data = make_dataset(sketch_root)

        self.target_feature = target
        self.len_imgs = len(self.sketch_data)

        self.root = root

        self.mode = mode
        self.opt = opt
        self.transform = transform
    def __getitem__(self, index):
        img_path = self.sketch_data[index]
        img = Image.open(img_path).convert('RGB')

        # dir, file split
        seed_path, file_path = os.path.split(img_path) 
        file_name, file_extension = os.path.splitext(file_path)
        
        seed = os.path.basename(seed_path)
        seed = int(seed)
        stroke_root = os.path.join(self.root, "stroke")
        stroke_dir = os.path.join(stroke_root, f'{seed:05d}')
        os.makedirs(stroke_dir, exist_ok=True)
        
        img = self.transform(img)

        input_dict = {'img': img,  'path': img_path, 'name': file_name ,'seed': seed}
        return input_dict


    def __len__(self):
        return self.len_imgs

