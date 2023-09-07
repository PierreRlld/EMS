import os
import pandas as pd
import numpy as np
from math import floor
from shutil import copytree
from tqdm import tqdm
import re
from zp_folder_pth import *
#from main.zp_configure import retrieve_file_paths

#--------------------
def rebaser(df):
    df = df.sort_values(by="num", ignore_index=True)
    df["floor_num"] = df["num"].apply(lambda x: floor(x))
    value_ct = dict(df["floor_num"].value_counts())
    df["clean_chapt"] = ""
    for el_ in list(value_ct.keys()):
        mask = (df["floor_num"]==el_)
        long = len(df.loc[mask])/100
        to_add = pd.Series(np.arange(0.01,long+0.01, 0.01)).set_axis(df.loc[mask].index)
        df.loc[mask,"clean_chapt"] = df.loc[mask,"floor_num"]+to_add
    return df

def chapt_central(Name_path, dic):
    
    def chapt_search(chapt):
        try:
            #y = re.search(r'Chapter \d+',chapt).group(0)
            y = re.search(r'Chapter ((\d+(\.\d*)?)|(\.\d+))',chapt).group(0)
        except:
            try:
                y = re.search(r'Ch.((\d+(\.\d*)?)|(\.\d+))',chapt).group(0)
            except:
                # Format MangaSee ...
                iterr = True
                c = 0
                while iterr == True:
                    x = hk_chapt_name[c]
                    try:
                        var = x + ' ((\d+(\.\d*)?)|(\.\d+))'
                        y = re.search(var,chapt).group(0)
                        iterr = False
                    except:
                        c+=1
                        pass
        num = float(re.findall(r'((\d+(\.\d*)?)|(\.\d+))',y)[0][0])
        return num
    
    df = pd.DataFrame({'chapt':[], 'num':[], 'vol':[]})
    i = 0
    input_path = base_path+Name_path
    save_path = clean_path+Name_path+"*"
    
    if os.path.exists(save_path) == False:
        os.mkdir(save_path)
    
    if len(os.listdir(save_path)) == len(os.listdir(input_path)):
        return()
    
    else:
        save_list = []
        
        for chapt in os.listdir(input_path):
            if chapt not in [".DS_Store", "._.DS_Store"]:
                num = chapt_search(chapt)
                try:
                    vol = dic[round(num)]
                    df.loc[i] = [chapt, num, vol]
                    i+=1
                except:pass
        df = rebaser(df)
        
        for chapt in os.listdir(save_path):
            if chapt not in [".DS_Store", "._.DS_Store"]:
                save_list.append(chapt_search(chapt))
        
        with tqdm(total=len(df), ascii=True) as pbar:
            for j in range(len(df)):
                if df.loc[j,"clean_chapt"] in save_list:
                    pass
                else:
                    pbar.set_description("Processing %s" % str(df.loc[j,"chapt"]))
                    copytree(base_path+Name_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+str(df.loc[j,"chapt"]))
                    os.rename(save_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+"Vol."+str(df.loc[j,"vol"])+" Chapter "+f'{df.loc[j,"clean_chapt"]:.2f}') #pour garder 1.10 par ex et pas passer en 1.1
                    for file in os.listdir(base_path+Name_path+"/"+str(df.loc[j,"chapt"])):
                        try:
                            os.remove(base_path+Name_path+"/"+str(df.loc[j,"chapt"])+"/"+file)
                        except:pass
                pbar.update(1)


# * %%%%%% TEST %%%%%%%

manga = 'JJK'
manga_pth = "Jujutsu Kaisen"
from main.ems_main import get_settings, get_dic
xlsx = pd.ExcelFile('origin.xlsx')
set = get_settings(manga, xlsx)
manga_dic = get_dic(manga, set['Manga_path'], xlsx)

if __name__ == "__main__":
    chapt_central(Name_path=manga_pth,dic=manga_dic)
