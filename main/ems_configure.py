#__REQUIRED MODULES 
import os
import time
from math import *
from os.path import basename
import zipfile
import re
from shutil import copytree, rmtree, move
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
import inquirer
from inquirer.themes import Default
from blessed import Terminal
from ems_chapt_central import chapt_central, rebaser, chapt_search
today = str(datetime.today().strftime('%Y-%m-%d'))
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