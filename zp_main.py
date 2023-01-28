from zp_configure import *
from folder_pth import *

#-----------------------
def get_settings(Name): 
    set = pd.read_excel('zanpa_file.xlsx', sheet_name='SETTINGS')
    set = set.set_index(keys='Manga',drop=True)
    set['TBD']=set['TBD'].apply(lambda x: x==True)
    #return list(set.loc[Name])
    return set.loc[Name].to_dict()

#-----------------------
def get_dic(Name, Name_path):  
    try:
        df = pd.read_excel('zanpa_file.xlsx', sheet_name=Name, usecols= 'A:B')
        df_dic = pd.Series(df.Vol.values, index=df.Chapt).to_dict()
        return df_dic
    except:
        chapt_list = os.listdir(base_path+Name_path)
        spe_dic={}
        for el in chapt_list:
            chapt = round(float(el.split(' ')[1].split('.')[1]))  #<Vol.XX Chapter-XX>
            try:
                vol = round(float(el.split(' ')[0].split('.')[1]))
            except:
                vol = 'TBD'
            spe_dic[chapt]=vol
        return spe_dic

#-----------------------   
def get_dic_arc(Name, arc):
    if arc==True:
        df = pd.read_excel('zanpa_file.xlsx', sheet_name=Name+"_Arc", usecols="A:E")
        df_dic = pd.Series(df.Arc.values, index=df.Vol).to_dict()
        return df_dic
    else:
        return None

#-----------------------
def meta_group_chapt(arc, manga, vol_format, el_list, volumes, pth, dic, TBD):
    long = len(pth) + 1

    def dic_arc_check(vol):
        nonlocal dic_arc
        if arc==True:
            return dic_arc[vol]
        else:
            return vol
    
    if arc==True:
        dic_arc = get_dic_arc(manga, arc)   # {vol:'arc'}
        group = {i:[] for i in list(np.unique(np.array(list(dic_arc.values())))) }
    else:
        dic_arc=None
        group = {i:[] for i in range(1,volumes+1)}
        if TBD==True:
            group['TBD'] = []

    if vol_format == 1:
        for el in el_list:
            vol = dic[round(float(el[long::].split(' ')[1].split('-')[1].split('/')[0]))]   #<Vol.XX Chapter-XX>
            group[dic_arc_check(vol)].append(el)
    else:   #2.1 ou 2.2
        for el in el_list:
            vol = dic[round(float(el[long::].split('-')[1].split('/')[0]))] #<Chapter-XX>
            group[dic_arc_check(vol)].append(el)
    return group    


#-----------------------
#-----------------------
def zanpa(manga: str, scan_mode, arc=False):
    '''
    @manga : name to be saved as = name in zanpa_file.xlsx
    @manga_path : download name from Hakuneko
    @mode : [scan_start, scan_end] or "all"
    '''
    set = get_settings(manga)
    manga_dic = get_dic(manga, set['Manga_path'])
    manga_path = set['Manga_path']
    print('Converting '+manga_path)
    dir_name = clean_path+manga_path+"*"

    chapt_renamer(Name_path=set['Manga_path'], vol_format=set['Vol_format'], mode=scan_mode, dic=manga_dic, volumes=int(set['Volumes']))    #>>enregistrés dans dir_name
    filePaths = retrieve_file_paths(dir_name)
    
    grouped = meta_group_chapt(arc=arc, manga=manga, vol_format=set['Vol_format'], el_list=filePaths[1::], volumes=int(set['Volumes']), 
                                pth=dir_name, dic=manga_dic, TBD=set['TBD'])   #.DS_Store à enlever

    fold_id = "_"+str(len(next(os.walk(output_dir))[1]))
    os.mkdir(os.path.join(output_dir, " ".join([today+fold_id, manga])))
    nb_converted_vol = len([k for k in list(grouped.keys()) if grouped[k]!=[]]) 
    with tqdm(total=nb_converted_vol) as pbar:
        for vol in list(grouped.values()) : 
            if vol!=[]:
                num = list(grouped.keys())[ list(grouped.values()).index(vol) ]     #key dans le dic à partir élément = bon num volume
                if arc==True:
                    zip_file = zipfile.ZipFile(output_dir+today+fold_id+' '+manga+'/'+manga+' Arc '+str(num)+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
                else:
                    zip_file = zipfile.ZipFile(output_dir+today+fold_id+' '+manga+'/'+manga+' Vol'+str(num)+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
                with zip_file:
                    try:
                        cover = cover_dir+manga+'/'+str(num)+'.jpg'
                        zip_file.write(cover, arcname="/0.cover/"+basename(cover))
                    except:
                        pass
                    finally:
                        for file in vol:
                            zip_file.write(file, arcname=file[len(clean_path)::])
                pbar.update(1)
            else:pass
    rmtree(clean_path+manga_path+'*')
