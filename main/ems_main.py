from ems_configure import *
from ems_folder_pth import *

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
        if l[0]<15:                             # * fonctionnement "normal"
            for j in range(l[0]+1):
                df_dic[j] = sub_dic[l[0]]
            for k in range(1,len(l)):
                for j in range(l[k-1]+1,l[k]+1):
                    df_dic[j] = sub_dic[l[k]]
            return df_dic
        else:                                   # * CF Berserk, Jojo2, Jojo3, GoldenBoy etc...
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
            chapt = chapt_search(chapt=el)
            try:
                vol = round(float(re.findall(r'\d+',re.search(r'Vol.\d+',el).group(0))[0]))
            except:
                raise ValueError("<Erreur> dans 'get_dic' > verif. Vol.X (..) format OU inclusion dans 'SETTINGS'")
            spe_dic[chapt]=vol
        return spe_dic

#-----------------------
def meta_group_chapt(el_list, mode, volumes, pth, dic, TBD):
    
    def chapt_select(mode, dic, volumes, TBD):
        '''
        @mode: [scan_start,scan_finish] OR 'TBD update' OR 'all'
        '''
        if type(mode)==list or mode=='TBD update':
            if mode == 'TBD update':
                if TBD==False:
                    return "<Erreur> TBD=False dans 'chapt_select'"
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
            #ARC
            #rajouter param: manga, xlsx
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
    
    long = len(pth) + 1
    group = {i:[] for i in range(1,volumes+1)}
    
    to_omit = chapt_select(mode=mode,dic=dic,volumes=volumes,TBD=TBD)
    
    if to_omit=="<Erreur> TBD=False dans 'chapt_select'":
        print("<Erreur> TBD=False dans 'chapt_select'")
        quit()
    
    else:
        if TBD==True:
            group['TBD'] = []

        for el in el_list:
            try:
                #vol = dic[round(float(el[long::].split(' ')[1].split(' ')[1].split('/')[0]))]   #<Vol.XX Chapter-XX> <old>
                vol = dic[round(float(el[long::].split(' ')[2].split('/')[0]))]                  #<Vol.XX Chapter XX> 
                if vol not in to_omit:
                    group[vol].append(el)
            except:
                pass

        return group    

#-----------------------
#-----------------------
def EMS_central(manga: str, scan_mode):
    '''
    @manga : name to be saved as = name in origin.xlsx
    @mode: [scan_start,scan_finish]:scan_finish (int) ou "max" /OR/ 'TBD update' /OR/ 'all'
    '''
    xlsx = pd.ExcelFile('origin.xlsx')
    set = get_settings(manga, xlsx)
    try:
        manga_dic = get_dic(manga, set['Manga_path'], xlsx)
    except:
        return()
    try:
        df_cover = pd.read_excel(xlsx, sheet_name='SETTINGS', usecols='A,S')
        df_cover.set_index('Manga',drop=True,inplace=True)
        df_cover = df_cover.to_dict()['cover_folder']
        manga_cover = df_cover[manga]
    except:
        pass
    #print(manga_dic, len(manga_dic))
    manga_path = set['Manga_path']
    print('>>> Converting '+manga_path)
    
    dir_name = clean_path+manga_path+"*"
    
    chapt_central(Name_path=manga_path,dic=manga_dic)   #! (1)
    filePaths = retrieve_file_paths(dir_name)           #! (2)
    
    grouped = meta_group_chapt(el_list=filePaths, mode=scan_mode, volumes=int(set['Volumes']), 
                                pth=dir_name, dic=manga_dic, TBD=set['TBD'])   

    fold_id = "_"+str(len(next(os.walk(output_dir))[1]))
    os.mkdir(os.path.join(output_dir, " ".join([today+fold_id, manga])))
    nb_converted_vol = len([k for k in list(grouped.keys()) if grouped[k]!=[]]) 
    with tqdm(total=nb_converted_vol, ascii=True) as pbar:
        for vol in list(grouped.values()) : 
            if vol!=[]:
                num = list(grouped.keys())[ list(grouped.values()).index(vol) ]     #key dans le dic à partir élément = bon num volume
                if num == "TBD":
                    max_chapt = -np.inf
                    for x in vol:
                        max_chapt = max(max_chapt,chapt_search(x))
                    zip_file = zipfile.ZipFile(output_dir+today+fold_id+' '+manga+'/'+manga+' Vol'+str(num)+" at="+str(max_chapt)+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
                else:zip_file = zipfile.ZipFile(output_dir+today+fold_id+' '+manga+'/'+manga+' Vol'+str(num)+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
                pbar.set_description("Processing Vol.%s" % num)
                with zip_file:
                    try:
                        cover = cover_dir+manga_cover+'/'+str(num)+'.jpg'
                        zip_file.write(cover, arcname="/0.cover/"+basename(cover))
                    except:
                        pass
                    finally:
                        for file in vol:
                            if "/._" in file[len(clean_path)::]:
                                pass
                            else:
                                zip_file.write(file, arcname=file[len(clean_path)::])
                pbar.update(1)
            else:pass
    print('Done ✅')
    return output_dir+today+fold_id+' '+manga
