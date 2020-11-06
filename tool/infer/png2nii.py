import os
import nibabel as nib
import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import argparse
from tqdm import tqdm


from util.util import to_pinyin
import util.util as util


parser = argparse.ArgumentParser()
# /home/lin/Desktop/data/aorta/nii/scan
# /home/lin/Desktop/data/aorta/external/nii_512/
parser.add_argument("--scan_dir", type=str, default="/home/lin/Desktop/data/aorta/nii/scan")
parser.add_argument("--seg_dir", type=str, default="./seg")
parser.add_argument("--png_dir", type=str, default="./img")
args = parser.parse_args()

png_dir = args.png_dir
img_names = os.listdir(png_dir)
patient_names = []
for n in img_names:
    if not n.endswith("mask.png"):
        continue
    n = n.split("-")
    if n[0] not in patient_names:
        # print(n[0], n)
        patient_names.append(n[0])
print(patient_names)
input("here")

all_imgs = os.listdir(png_dir)
for patient in tqdm(patient_names):
    # if os.path.exists(os.path.join(args.seg_dir, to_pinyin(patient) + ".nii.gz")):
    #     continue
    print("----------------")
    print(patient)
    img_names = [n for n in all_imgs if n.split("-")[0] == patient and n.endswith("mask.png")]
    img_names.sort(key=lambda n: int(n.split("-")[1].split("_")[0]))
    print(img_names)
    print(len(img_names))

    img_data = np.zeros([512, 512, len(img_names) + 2])
    print(img_data.shape)

    # with ThreadPoolExecutor(max_workers=16) as exe_pool:
    #     tasks = [
    #         exe_pool.submit(self.process_worker, imgs, idx, use_pr)
    #         for idx in range(len(imgs))
    #     ]

    for img_name in img_names:
        img = cv2.imread(os.path.join(args.png_dir, img_name))
        ind = int(img_name.split("-")[1].split("_")[0])
        img = img.swapaxes(0, 1)
        if "\u4e00" <= patient[0] <= "\u9fff":
            img = img[:, ::-1, 0]
        elif len(patient) > 5:
            img = img[:, ::-1, 0]
        else:
            img = img[::-1, ::, 0]
        img_data[:, :, ind] = img
    try:
        print(os.path.join(args.scan_dir, patient + ".nii.gz"))
        scanf = nib.load(os.path.join(args.scan_dir, patient + ".nii"))
        scan_header = scanf.header
    except:
        print(patient, "error")
        scanf = nib.load(os.path.join(args.scan_dir, "张金华_20201024213424575a.nii"))
        scan_header = scanf.header

    img_data[:, :, -1] = img_data[:, :, -2]
    img_data[:, :, 0] = img_data[:, :, 1]

    # img_data = util.filter_largest_volume(img_data, mode="hard")
    newf = nib.Nifti1Image(img_data.astype(np.float64), scanf.affine, scan_header)
    nib.save(newf, os.path.join(args.seg_dir, patient + ".nii.gz"))
    # input("here")
