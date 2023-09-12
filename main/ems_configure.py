#__REQUIRED MODULES 
import os
import time
from math import *
from os.path import basename
import zipfile
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
from shutil import copytree, rmtree, move
today = str(datetime.today().strftime('%Y-%m-%d'))
from main.ems_chapt_central import chapt_central, rebaser
import re
import inquirer
from inquirer.themes import Default
from blessed import Terminal
from main.repo_check_size import *


#------------------------
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
        if '/._' in filePath:
          pass
        else:
          filePaths.append(filePath)
  return filePaths