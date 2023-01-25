import os
import pandas as pd
import numpy as np
from math import floor
from shutil import copytree
from zp_configure import base_path, clean_path

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
def mode_RemoveVol(mode, dic, volumes):
    '''
    @mode: [scan_start,scan_finish] OR 'all'
    '''
    if type(mode)==list:
        start_vol = dic[mode[0]]
        end_vol = dic[mode[1]]
        to_del = []
        if start_vol==end_vol=='TBD':
            to_del.extend([i for i in range(1,volumes)])
            return to_del  
        else:     
            to_del.extend([i for i in range(1,start_vol)])
            try:
                to_del.extend([j for j in range(min(end_vol+1,volumes), volumes+1)])
                if end_vol<volumes:
                    to_del.append('TBD')
            except:
                pass
            return to_del
    else:
        return []


#--------------------
def chapt_renamer(Name_path, vol_format, mode, dic, volumes):
    save_path = clean_path+Name_path+"*"
    to_del = mode_RemoveVol(mode, dic, volumes)
    df = pd.DataFrame({'chapt':[], 'num':[], 'vol':[]})
    i=0
    chapt_list = os.listdir(base_path+Name_path)
    try:
        chapt_list.remove(".DS_Store")
    except:pass

    for chapt in chapt_list:
        if vol_format==1:
            #_"Vol.XX Ch.XX"   >>OK
            vol = chapt.split(' ')[0]
            num = chapt.split(' ')[1].split('.')[1]
            #num = chapt.split(' ')[2] #VAGABOND !
            '''
            #Vol.01 Ch.003 - Watch Out! 
            Vol.1 Chapter 4  The Brigand Tsujikaze
            '''
        elif vol_format==2.1:
            #_"Ch.XX"          >>OK
            vol = ""
            num = chapt.split(' ')[0].split('.')[1]
        else:
            #_"Chapter XX ..." >>OK
            vol = ""
            num = chapt.split(' ')[1]
        
        if dic[round(float(num))] in to_del:
            pass
        else:
            df.loc[i] = [chapt, float(num), vol]
            i+=1

    df=rebaser(df)
    for j in range(len(df)):
        copytree(base_path+Name_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+str(df.loc[j,"chapt"]))
        os.rename(save_path+"/"+str(df.loc[j,"chapt"]), save_path+"/"+df.loc[j,"vol"]+" Chapter-"+f'{df.loc[j,"clean_chapt"]:.2f}') #pour garder 1.10 par ex

