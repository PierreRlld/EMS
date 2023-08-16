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
def mode_RemoveVol(mode, dic, volumes, TBD):
    '''
    @mode: [scan_start,scan_finish] OR 'TBD update' OR 'all'
    '''
    if type(mode)==list or mode=='TBD update':
        if mode == 'TBD update':
            if TBD==False:
                print('ERROR MODE DANS REMOVE_VOL')
                return 'ERROR MODE DANS REMOVE_VOL'
            else:
                start_vol, end_vol = 'TBD', 'TBD'
        else:
            start_vol = dic[mode[0]]
            end_vol = mode[1]
            if end_vol == "max":    # !!!! max qu'il faut rentrer dans cmd poru que ça marche
                end_vol = dic[int(max(list(dic.keys())))]
            else:
                end_vol = dic[int(mode[1])]
        to_del = []
        '''
        #rajouter manga, xlsx
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
        '''
        if start_vol==end_vol=='TBD':
            to_del.extend([i for i in range(1,volumes+1)])
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
def chapt_renamer(Name_path, mode, dic, volumes, TBD):
    save_path = clean_path+Name_path+"*"
    to_del = mode_RemoveVol(mode, dic, volumes, TBD)
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
        print('<!> Error origin.xlsx not up to date!\n<!> Cannot handle {0} files until update.'.format(Name_path))
        quit()
    
    for chapt in chapt_list:
        # !! Même code que get_dic !!
        try:
            y = re.search(r'Chapter \d+',chapt).group(0)
        except:
            try:
                y = re.search(r'Ch.\d+',chapt).group(0)
            except:
                # Format MangaSee ...
                iterr = True
                c = 0
                while iterr == True:
                    x = hk_chapt_name[c]
                    try:
                        var = x + ' \d+'
                        y = re.search(var,chapt).group(0)
                        iterr = False
                    except:
                        c+=1
                        pass
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

