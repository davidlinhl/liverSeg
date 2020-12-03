# 将两个文件夹的nii扫描和标签转换成paddleseg的数据集格式
"""
1. 所有的nii和标签转成png
2. 按照paddleseg的目录结构移动文件
# TODO:  3. 生成list文件
"""
import os
import argparse

from tqdm import tqdm

import util

parser = argparse.ArgumentParser()
parser.add_argument("--scan_dir", type=str, required=True)
parser.add_argument("--scan_img_dir", type=str, required=True)
parser.add_argument("--label_dir", type=str, default=None)
parser.add_argument("--label_img_dir", type=str, default=None)
parser.add_argument("--thresh", type=int, default=None)
parser.add_argument("--ww", type=int, default=1000)
parser.add_argument("--wc", type=int, default=0)
parser.add_argument("--rot", type=int, default=0)


args = parser.parse_args()

# TODO: 完善对扫描和标签的检查
# util.check_nii_match(args.scan_dir, args.label_dir)

# TODO: 添加logging
scans = util.listdir(args.scan_dir)
labels = util.listdir(args.label_dir)
for s, l in zip(scans, labels):
    print(s, "\t", l)
cmd = input("Input Y/y to continue: ")
if cmd.lower() != "y":
    exit("exit on user cmd")
scans = tqdm(scans)
for scan, label in zip(scans, labels):
    scans.set_description("Processing {}".format(scan.rstrip(".gz").rstrip(".nii")))

    util.nii2png(
        os.path.join(args.scan_dir, scan),
        args.scan_img_dir,
        os.path.join(args.label_dir, label) if args.label_dir else None,
        args.label_img_dir,
        rot=args.rot,
        wwwc=[args.ww, args.wc],
        thresh=args.thresh,
    )