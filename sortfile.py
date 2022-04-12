from importlib.resources import path
import shutil
from numpy import where
import pandas as pd
import os.path
from os import *

defectlist= [' creamout', ' node', ' burnt', ' broken', ' crack', 'tailing', 'pale','Oval']

df = pd.read_csv("/home/amit/senquire_work/csvfileoperations/prac1.csv")
parent_dir = "/home/amit/senquire_work/csvfileoperations/parentdir"

for index, row in df.iterrows():
    
    for defect in defectlist:
        if not os.path.exists(os.path.join(parent_dir, defect)):
            os.makedirs(os.path.join(parent_dir, defect))
        if row['defect1'].find(defect) != -1: 
            shutil.copy(os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', row['name']), os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', defect, row['name']))

for index, row in df.iterrows():

    for defect1 in defectlist:
        if not os.path.exists(os.path.join(parent_dir, defect1)):
            os.makedirs(os.path.join(parent_dir, defect1))
        if row['defect2'].find(defect1) != -1: 
            shutil.copy(os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', row['name']), os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', defect1, row['name']))

for index, row in df.iterrows():

    for defect2 in defectlist:
        if not os.path.exists(os.path.join(parent_dir, defect2)):
            os.makedirs(os.path.join(parent_dir, defect2))
        if row['defect3'].find(defect2) != -1: 
            shutil.copy(os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', row['name']), os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', defect2, row['name']))

# for _file in os.listdir('/home/amit/senquire_work/csvfileoperations/parentdir'):
#     if not os.path.isdir(os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', _file)):
#         os.remove(os.path.join('/home/amit/senquire_work/csvfileoperations/parentdir', _file))
    
