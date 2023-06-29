import os
import pandas as pd
import numpy as np
from math import floor
from shutil import copytree
from tqdm import tqdm
import re
from zp_folder_pth import *

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

#--------------------
#def start_end(mode, dic, volumes, arc, manga):
#    if arc==True:
#        vol_list = np.array(pd.read_excel('zanpa_file.xlsx', sheet_name=manga+'_Arc', usecols= 'D:E')['End vol'].dropna().to_list())
#        if dic[mode[0]] in vol_list:
#            start_vol = int(vol_list[vol_list<=dic[mode[0]]].max())
#        else:
#            start_vol = int(vol_list[vol_list<=dic[mode[0]]].max())+1
#        end_vol = int(vol_list[vol_list>=dic[mode[1]]].min())
#    else:
#        start_vol = dic[mode[0]]
#        end_vol = dic[mode[1]]
#    return [start_vol, end_vol]



#--------------------
def mode_RemoveVol(mode, dic, volumes, arc, manga, xlsx):
    '''
    @mode: [scan_start,scan_finish] OR 'all'
    '''
    if type(mode)==list:
        start_vol = dic[mode[0]]
        end_vol = mode[1]
        if end_vol == "max":
            end_vol = max(list(dic.keys()))
        else:
            end_vol = dic[int(mode[1])]
        to_del = []

        if arc==True:
            df = pd.read_excel(xlsx, sheet_name=manga+'_Arc', usecols= 'D:E')
            vol_list = np.array(df['End_Vol'].dropna().to_list())
            if start_vol==end_vol=='TBD':
                to_del.extend([i for i in range(1,np.setdiff1d(vol_list, [volumes]))])
                return to_del
            else:
                if start_vol not in vol_list:
                    start_vol = int(vol_list[vol_list<=start_vol].max())+1
                if end_vol not in vol_list:
                    if end_vol == 'TBD':
                        end_vol = volumes
                    else:
                        end_vol = int(vol_list[vol_list>=end_vol].min())-1
                to_del.extend([i for i in range(1,start_vol)])
                try:
                    to_del.extend([j for j in range(end_vol+1, volumes+1)])
                    if end_vol<volumes:
                        to_del.append('TBD')
                except:
                    pass
                return to_del

        else:
            if start_vol==end_vol=='TBD':
                to_del.extend([i for i in range(1,volumes)])
                return to_del  
            else:     
                to_del.extend([i for i in range(1,start_vol)])
                try:
                    to_del.extend([j for j in range(end_vol+1, volumes+1)])
                    if end_vol<volumes:
                        to_del.append('TBD')
                except:
                    pass
                return to_del
    else:
        return []


#--------------------
def chapt_renamer(Name_path, mode, dic, volumes, arc, manga, xlsx):
    save_path = clean_path+Name_path+"*"
    to_del = mode_RemoveVol(mode, dic, volumes, arc, manga, xlsx)
    df = pd.DataFrame({'chapt':[], 'num':[], 'vol':[]})
    i=0
    chapt_list = os.listdir(base_path+Name_path)
    nul = [".DS_Store", "._.DS_Store"]
    for ele in nul:
        try:
            chapt_list.remove(ele)
        except:
            pass

    try:
        pass
    except:
        print('<!> Error zanpa_file.xlsx not up to date!\n<!> Cannot handle {0} files until update.'.format(Name_path))
        quit()

    for chapt in chapt_list:
        """
        if vol_format==1:
            #_"Vol.XX Ch.XX"   >>OK
            if Name_path == 'Vagabond':
                num = chapt.split(' ')[2] #VAGABOND !
            else:
                num = chapt.split(' ')[1].split('.')[1]
            '''
            #Vol.01 Ch.003 - Watch Out! 
            Vol.1 Chapter 4  The Brigand Tsujikaze
            '''
        elif vol_format==2.1:
            #_"Ch.XX"          >>OK
            num = chapt.split(' ')[0].split('.')[1]
        else:
            #_"Chapter XX ..." >>OK
            num = chapt.split(' ')[1]
        """
        try:
            y = re.search(r'Chapter \d+',chapt).group(0)
        except:
            y = re.search(r'Ch.\d+',chapt).group(0)
        num = re.findall(r'\d+',y)[0]
        try:
            vol = dic[round(float(num))]
            if vol in to_del:
                pass
            else:
                df.loc[i] = [chapt, float(num), vol]
                i+=1
        except:
            pass

    df=rebaser(df)
    with tqdm(total=len(df)) as pbar:
        for j in range(len(df)):
            copytree(base_path+Name_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+str(df.loc[j,"chapt"]))
            os.rename(save_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+"Vol."+str(df.loc[j,"vol"])+" Chapter-"+f'{df.loc[j,"clean_chapt"]:.2f}') #pour garder 1.10 par ex et pas passer en 1.1
            pbar.update(1)

