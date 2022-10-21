# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:00:05 2022

@author: emilo
"""

import os
import glob
from pycasso import Canvas

os.chdir("C:/Users/emilo/OneDrive - Lund University/Experiment paradigms/ExperimentParadigms_Lund-Oxford/fMRI_gallerymemory/GalleryGame_block_fMRI")

readpath = "Images/*.jpg"

#Scramble and export images.
for img in glob.glob(readpath): 
    Canvas(img, 1, 'seed').export('scramble', os.path.splitext(img)[0] +'_scrambled.jpg')

