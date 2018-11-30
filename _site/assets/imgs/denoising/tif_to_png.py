#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert .tif images into .png

Created on Wed Oct  3 14:41:13 2018

@author: remussn
"""
import os
from PIL import Image

folders = ['l2_3C_motion_masked_gradient_masked_reg_no_drop_0.75_FULL_SEG',
	   'l2_3C_motion_masked_gradient_masked_reg_no_drop_0.75_FULL_data_w2']


raw_train_folder = '/raw_train'
raw_valid_folder = '/raw_valid'
train_folder = '/train'
valid_folder = '/valid'

#raw_train_path = raw_train_folder+
raw_train_paths = [folders[i]+raw_train_folder for i in range(len(folders))]
raw_valid_paths = [folders[i]+raw_valid_folder for i in range(len(folders))]
train_paths = [folders[i]+train_folder for i in range(len(folders))]
valid_paths = [folders[i]+valid_folder for i in range(len(folders))]

# Image.open('./epoch_140_train_inputs_img.tif').save('./epoch_140_train_inputs_img.png')

for expIdx in range(len(folders)):
    raw_train_path = raw_train_paths[expIdx]
    raw_valid_path = raw_valid_paths[expIdx]
    train_path = train_paths[expIdx]
    valid_path = valid_paths[expIdx]
    
    for root, dirs, files in os.walk(raw_train_path):  
        for filename in files:
            Image.open(raw_train_path+'/'+filename).save(train_path+'/'+filename.split('.')[0]+'.png')

    for root, dirs, files in os.walk(raw_valid_path):  
        for filename in files:
            Image.open(raw_valid_path+'/'+filename).save(valid_path+'/'+filename.split('.')[0]+'.png')
    
