# MedSeg
English | [简体中文](./README_cn.md)

Medical image segmentation toolkit based on PaddlePaddle framework. Our target is to implement various 2D and 3D model architectures, various loss function and data augmentation methods. This is still a work in progress but has achieved promising results on liver segmentation and aorta segmentation. The development plans can be seen in the [Project](https://github.com/davidlinhl/medSeg/projects/1)

## Project Structure
Currently this project contains only 2D segmentation models. The structure is as follows.

- medseg: Promary code
-- train.py: Training pipeline
-- aug.py: Data augmentation
-- loss.py: Various model loss
-- eval.py: Various metrics to evaluate segmentation result
-- vis.py: Visualize results
-- models: Currently only 2D models
