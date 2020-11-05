import glob
import json
from pprint import pprint

import yaml
from pathlib import Path
from vojtovo import *


class Project:

    """ Default Psi Truncation """
    psi = 0.75

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.image_seeds = self.get_image_seeds()
        self.style_seeds = self.get_style_seeds()
        self.pkl = self.get_pkl_filename()

    def get_pkl_filename(self):
        pkls = glob.glob(self.data_dir + '/*.pkl')
        pprint(pkls)
        return pkls[0]

    def get_seed_url(self, seed):
        return "{}/{}.jpg".format(self.data_dir, seed)

    def get_image_seeds(self):
        seeds = []
        files = glob.glob(self.data_dir + '/images/*.jpg')
        for file in files:
            seeds.append(os.path.splitext(os.path.basename(file))[0])  # Append filename without extension
        return seeds

    def get_style_seeds(self):
        seeds = []
        files = glob.glob(self.data_dir + '/styles/*.jpg')
        for file in files:
            seeds.append(os.path.splitext(os.path.basename(file))[0])  # Append filename without extension
        return seeds
