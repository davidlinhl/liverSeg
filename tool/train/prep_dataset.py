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

import util

parser = argparse.ArgumentParser()
parser.add_argument("--scan_dir", type=str, default="/home/lin/Desktop/data/aorta/nii/scan")
parser.add_argument("--scan_img_dir", type=str, default="/home/lin/Desktop/data/aorta/dataset/scan")
parser.add_argument("--label_dir", type=str, default="/home/lin/Desktop/data/aorta/nii/label")
parser.add_argument("--label_img_dir", type=str, default="/home/lin/Desktop/data/aorta/dataset/label")
parser.add_argument("--scan_only", type=bool, default=True)

args = parser.parse_args()
# util.check_nii_match(args.scan_dir, args.label_dir)
# TODO: 添加logging
pbar = tqdm(os.listdir(args.scan_dir))
for file in pbar:
    pbar.set_description("Processing {}".format(file))
    if args.scan_only:
        util.nii2png(
            os.path.join(args.scan_dir, file),
            args.scan_img_dir,
            rot=1,
            wwwc=(400, 0),
        )
    else:
        util.nii2png(
            os.path.join(args.scan_dir, file),
            args.scan_img_dir,
            os.path.join(args.label_dir, file),
            args.label_img_dir,
            rot=1,
            wwwc=(400, 0),
        )
