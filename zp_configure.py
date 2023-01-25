
#__REQUIRED MODULES 
import os
from math import *
from os.path import basename
import zipfile
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
from shutil import copytree, rmtree
from file_manip import chapt_renamer, mode_RemoveVol, rebaser
global today, base_path, clean_path, output_dir, cover_dir
today = datetime.today().strftime('%Y-%m-%d %S')


#====================================================
#======== TO_EDIT ===================================
#====================================================
base_path = "/Users/prld/Documents/222Mangas/"
clean_path = "/Users/prld/Documents/222Mangas_clean/"
output_dir = '/Users/prld/Documents/222upl_output/'
cover_dir = '/Users/prld/Desktop/git_proj/EMS/covers'


#----------------------------------------------------
#Source: https://linuxhint.com/python_zip_file_directory/
def retrieve_file_paths(dirName):
  # dirName = "/Users/prld/Documents/Mangas/Bleach"
  # setup file paths variable
  filePaths = []
   
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
  # return all paths
  return filePaths