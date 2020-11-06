# 将两个文件夹的nii扫描和标签转换成paddleseg的数据集格式
"""
1. 所有的nii和标签转成png
2. 按照paddleseg的目录结构移动文件
# TODO:  3. 生成list文件
"""
import os
import argparse

import numpy as np
import cv2
import nibabel as nib
from tqdm import tqdm

import util.util as util

parser = argparse.ArgumentParser()
parser.add_argument("--scan_dir", type=str, default="/home/lin/Desktop/data/aorta/nii/scan")
parser.add_argument("--label_dir", type=str, default="/home/lin/Desktop/data/aorta/nii/label")
parser.add_argument("--scan_img_dir", type=str, default="/home/lin/Desktop/data/aorta/dataset/scan")
parser.add_argument("--label_img_dir", type=str, default="/home/lin/Desktop/data/aorta/dataset/label")

args = parser.parse_args()
# util.check_nii_match(args.scan_dir, args.label_dir)

# TODO: 这里改成scan和label一起处理,一个函数
# TODO: 这里用threadpool

for file in tqdm(os.listdir(args.scan_dir)):
    util.nii2png(os.path.join(args.scan_dir, file), scan_img_dir=args.scan_img_dir)

# util.nii2png_folder(
#     args.label_dir,
#     args.label_img_dir,
#     rot=3,
#     wwwl=(600, 0),
#     subfolder=False,
#     islabel=True,
#     thresh=0,
# )
# util.labels = os.listdir("/home/lin/Desktop/data/lits/dataset/label/")
# util.nii2png_folder(
#     args.scan_dir,
#     args.scan_img_dir,
#     rot=3,
#     wwwl=(600, 0),
#     subfolder=False,
# )
