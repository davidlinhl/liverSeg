# 将mhd的扫描转换为nii格式
import os
import argparse

import SimpleITK as sitk
import nibabel as nib
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--mhd_dir", type=str, required=True)
parser.add_argument("--nii_dir", type=str, required=True)
args = parser.parse_args()


for fname in tqdm(os.listdir(args.mhd_dir)):
    if not fname.endswith(".mhd"):
        continue
    scan = sitk.GetArrayFromImage(sitk.ReadImage(os.path.join(args.mhd_dir, fname)))
    scan = scan.swapaxes(0, 1).swapaxes(1, 2)

    # TODO: 研究mhd/raw格式是否带有更多头文件信息
    new_scan = nib.Nifti1Image(scan, np.eye(4))
    nib.save(new_scan, os.path.join(args.nii_dir, fname.replace("mhd", "nii")))
