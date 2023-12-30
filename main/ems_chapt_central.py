import os
from math import floor
from shutil import copytree
import re
from tqdm import tqdm
import pandas as pd
import numpy as np
from yaspin import yaspin
from ems_folder_pth import *
#from main.zp_configure import retrieve_file_paths

#--------------------
def rebaser(df):
    df = df.sort_values(by="num", ignore_index=True)
    df["floor_num"] = df["num"].apply(lambda x: floor(x))
    value_ct = dict(df["floor_num"].value_counts())
    #df["clean_chapt"] = ""                               # ? Sept.23 Depreciation warning `df.iloc[:, i] = newvals` will attempt to set the values inplace instead of always setting a new array.
    for el_ in list(value_ct.keys()):
        mask = (df["floor_num"]==el_)
        long = len(df.loc[mask])
        to_add = pd.Series(np.arange(1,long+1,1)/100).set_axis(df.loc[mask].index)
        df.loc[mask,"clean_chapt"] = df.loc[mask,"floor_num"]+to_add
    return df

#! CHAPT FIND
def chapt_search(chapt):
    try:
        #y = re.search(r'Chapter \d+',chapt).group(0)
        y = re.search(r'Chapter ((\d+(\.\d*)?))',chapt).group(0)
    except:
        try:
            y = re.search(r'Ch.((\d+(\.\d*)?))',chapt).group(0)
        except:
            # Format MangaSee ...
            iterr = True
            c = 0
            while iterr == True:
                x = hk_chapt_name[c]
                try:
                    var = x + ' ((\d+(\.\d*)?))'
                    y = re.search(var,chapt).group(0)
                    iterr = False
                except:
                    c+=1
                    pass
    num = float(re.findall(r'((\d+(\.\d*)?))',y)[0][0])
    return num

#! <MAIN>
def chapt_central(Name_path, dic):
        
    def cleaning(Name_path):
        try:
            os.remove(clean_path+".DS_Store")
        except:pass
        try:
            os.remove(base_path+".DS_Store")
        except:pass
        try:
            os.remove(base_path+"._DS_Store")
        except:
            pass
        try:
            os.remove(base_path+Name_path+"/'.DS_Store'")
        except:
            pass
        try:
            os.remove(base_path+"._"+Name_path)
        except:
            pass
        
    df = pd.DataFrame({'chapt':[], 'num':[], 'vol':[]})
    i = 0
    input_path = base_path+Name_path
    save_path = clean_path+Name_path+"*"
    cleaning(Name_path=Name_path)   #* try remove all ._(xxx) files
    
    if os.path.exists(save_path) == False:
        os.mkdir(save_path)
    
    if len(os.listdir(save_path)) == len(os.listdir(input_path)):
        return()
    
    else:
        save_list = []
        
        with yaspin(text="ems_chapt_central.py vol<->chapt").line as sp:
            sp.side = "right"  
            for chapt in os.listdir(input_path):
                if chapt not in [".DS_Store", "._.DS_Store"]:
                    try:
                        num = chapt_search(chapt)
                        try:
                            vol = dic[round(num)]
                            df.loc[i] = [chapt, num, vol]
                            i+=1
                        except:pass
                    except:pass
            #print(df)
            df = rebaser(df)
            sp.ok("✅ ")
        
        for chapt in os.listdir(save_path):
            if chapt not in [".DS_Store", "._.DS_Store"]:
                save_list.append(chapt_search(chapt))
        
        with tqdm(total=len(df), ascii=True) as pbar:
            for j in range(len(df)):
                if df.loc[j,"clean_chapt"] in save_list:
                    pass
                else:
                    pbar.set_description("Moving %s" % str(df.loc[j,"chapt"]))
                    copytree(base_path+Name_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+str(df.loc[j,"chapt"]))
                    os.rename(save_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+"Vol."+str(df.loc[j,"vol"])+" Chapter "+f'{df.loc[j,"clean_chapt"]:.2f}') #pour garder 1.10 par ex et pas passer en 1.1
                    for file in os.listdir(base_path+Name_path+"/"+str(df.loc[j,"chapt"])):
                        try:
                            os.remove(base_path+Name_path+"/"+str(df.loc[j,"chapt"])+"/"+file)
                        except:pass
                pbar.update(1)        

#--------------------


# * %%%%%% TEST %%%%%%%
'''
manga = 'CJX'
manga_pth = "Choujin X"

#-----------------------
def get_settings(Name, xlsx): 
    set = pd.read_excel(xlsx, sheet_name='SETTINGS', usecols='A:I')         # ! VERFIER usecols dans origin.xlsx
    set = set.set_index(keys='Manga',drop=True)
    set['TBD']=set['TBD'].apply(lambda x: x==True)
    #return list(set.loc[Name])
    return set.loc[Name].to_dict()

def get_dic(Name, Name_path, xlsx):  
    try:
        df = pd.read_excel(xlsx, sheet_name='UPDATE')
        sub = df[["Vol",Name]].copy()
        sub = sub.dropna()
        sub_dic = pd.Series(sub.Vol.values, index=sub[Name])
        sub_dic.index = sub_dic.index.astype("int")
        df_dic = {}
        l = list(sub_dic.index)
        l.reverse()
        
        #print(l)
        if l[0]<20:                             # * ex Berserk, Jojo4 ... ça doit marcher avec ce code là et pas l'autre
            for j in range(l[0]+1):
                df_dic[j] = sub_dic[l[0]]
            for k in range(1,len(l)):
                for j in range(l[k-1]+1,l[k]+1):
                    df_dic[j] = sub_dic[l[k]]
            return df_dic
        else:                                   # * CF Jojo1, Jojo2 etc...
            for j in range(l[0]+1,l[1]+1):
                df_dic[j] = sub_dic[l[0]]
            for k in range(1,len(l)):
                for j in range(l[k-1]+1,l[k]+1):
                    df_dic[j] = sub_dic[l[k]]
            return df_dic
    
    #except ValueError:
    except KeyError:
        chapt_list = os.listdir(base_path+Name_path)
        nul = [".DS_Store", "._.DS_Store"]
        for ele in nul:
            try:
                chapt_list.remove(ele)
            except:
                pass
        spe_dic={}
        for el in chapt_list:
            try:
                y = re.search(r'Chapter ((\d+(\.\d*)?))',el).group(0)
            except:
                try:
                    y = re.search(r'Ch.((\d+(\.\d*)?))',el).group(0)
                except:
                    # Format MangaSee ...
                    iterr = True
                    c = 0
                    while iterr == True:
                        x = hk_chapt_name[c]
                        try:
                            var = x + ' ((\d+(\.\d*)?))'
                            y = re.search(var,el).group(0)
                            iterr = False
                        except:
                            c+=1
                            pass
            chapt = float(re.findall(r'((\d+(\.\d*)?))',y)[0][0])
            try:
                vol = round(float(re.findall(r'\d+',re.search(r'Vol.\d+',el).group(0))[0]))
            except:
                raise ValueError("ERROR IN get_dic > verif. Vol.X (..) format OU inclusion dans 'SETTINGS'")
            spe_dic[chapt]=vol
        return spe_dic
#-----------------------

xlsx = pd.ExcelFile('origin.xlsx')
set = get_settings(manga, xlsx)
manga_dic = get_dic(manga, set['Manga_path'], xlsx)

if __name__ == "__main__":
    chapt_central(Name_path=manga_pth,dic=manga_dic)
'''