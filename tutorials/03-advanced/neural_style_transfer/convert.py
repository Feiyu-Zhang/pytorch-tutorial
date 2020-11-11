# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

import sys
import shutil

imgpath='/home/zjh/zfy/pytorch-tutorial/tutorials/03-advanced/neural_style_transfer/png/style-shufa.jpg'
newpath='/home/zjh/zfy/pytorch-tutorial/tutorials/03-advanced/neural_style_transfer/png/style-shufa-new.png'
def turnto24(path):
    img=Image.open(imgpath).convert('RGB')
    img.save(newpath)

turnto24(imgpath)


