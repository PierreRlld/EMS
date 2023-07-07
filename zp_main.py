from zp_configure import *
from zp_folder_pth import *

#-----------------------
def get_settings(Name, xlsx): 
    set = pd.read_excel(xlsx, sheet_name='SETTINGS', usecols='A:I')
    set = set.set_index(keys='Manga',drop=True)
    set['TBD']=set['TBD'].apply(lambda x: x==True)
    #return list(set.loc[Name])
    return set.loc[Name].to_dict()

#-----------------------
#def old_get_dic(Name, Name_path, xlsx):  
    try:
        df = pd.read_excel(xlsx, sheet_name=Name, usecols= 'A:B')
        df_dic = pd.Series(df.Vol.values, index=df.Chapt).to_dict()
        return df_dic
    except ValueError:
        chapt_list = os.listdir(base_path+Name_path)
        nul = [".DS_Store", "._.DS_Store"]
        for ele in nul:
            try:
                chapt_list.remove(ele)
            except:
                pass
        spe_dic={}
        for el in chapt_list:
            if Name_path=='Vagabond':
                chapt = round(float(el.split(' ')[2]))
            else:
                chapt = round(float(el.split(' ')[1].split('.')[1]))  #<Vol.XX Chapter.XX>
            try:
                vol = round(float(el.split(' ')[0].split('.')[1]))
            except:
                vol = 'TBD'
            spe_dic[chapt]=vol
        return spe_dic

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

        for j in range(l[0]+1):
            df_dic[j] = sub_dic[l[0]]
        for k in range(1,len(l)):
            for j in range(l[k-1],l[k]+1):
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
            if Name_path=='Vagabond':
                chapt = round(float(el.split(' ')[2]))
            else:
                chapt = round(float(el.split(' ')[1].split('.')[1]))  #<Vol.XX Chapter.XX>
            try:
                vol = round(float(el.split(' ')[0].split('.')[1]))
            except:
                vol = 'TBD'
            spe_dic[chapt]=vol
        return spe_dic

#-----------------------   
#def get_dic_arc(Name, arc, xlsx):
    if arc==True:
        df = pd.read_excel(xlsx, sheet_name=Name+"_Arc", usecols="A:E")
        df_dic = pd.Series(df.Arc.values, index=df.Vol).to_dict()
        return df_dic
    else:
        return None

#-----------------------
def meta_group_chapt(el_list, volumes, pth, dic, TBD, arc, dic_arc):
    long = len(pth) + 1

    def dic_arc_check(vol):
        #nonlocal dic_arc
        if arc==True:
            return dic_arc[vol]
        else:
            return vol
    
    if arc==True:
        group = {i:[] for i in list(np.unique(np.array(list(dic_arc.values())))) }
    else:
        group = {i:[] for i in range(1,volumes+1)}
        if TBD==True:
            group['TBD'] = []

    for el in el_list:
        vol = dic[round(float(el[long::].split(' ')[1].split('-')[1].split('/')[0]))]   #<Vol.XX Chapter-XX>
        group[dic_arc_check(vol)].append(el)
    '''
    if vol_format == 1:
        for el in el_list:
            vol = dic[round(float(el[long::].split(' ')[1].split('-')[1].split('/')[0]))]   #<Vol.XX Chapter-XX>
            group[dic_arc_check(vol)].append(el)
    else:   #2.1 ou 2.2
        for el in el_list:
            vol = dic[round(float(el[long::].split('-')[1].split('/')[0]))] #<Chapter-XX>
            group[dic_arc_check(vol)].append(el)
    '''
    return group    

#-----------------------
#-----------------------
def zanpa(manga: str, scan_mode, arc=False):
    '''
    @manga : name to be saved as = name in origin.xlsx
    @scan_mode : [scan_start, scan_end] / "all" / update
    @arc : pas utilisé
    '''
    xlsx = pd.ExcelFile('origin.xlsx')
    set = get_settings(manga, xlsx)
    manga_dic = get_dic(manga, set['Manga_path'], xlsx)
    #print(manga_dic, len(manga_dic))
    #manga_arc_dic = get_dic_arc(manga, arc, xlsx)
    manga_path = set['Manga_path']
    print('>>> Converting '+manga_path)
    dir_name = clean_path+manga_path+"*"

    chapt_renamer(Name_path=set['Manga_path'], mode=scan_mode, dic=manga_dic, 
                  volumes=int(set['Volumes']), arc=arc, manga=manga, xlsx=xlsx, TBD=set['TBD'])                                        #>>enregistrés dans dir_name
    filePaths = retrieve_file_paths(dir_name)
    
    grouped = meta_group_chapt(el_list=filePaths[1::], volumes=int(set['Volumes']), 
                                pth=dir_name, dic=manga_dic, TBD=set['TBD'], arc=False, dic_arc=None)   #.DS_Store à enlever

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
                            if "/._" in file[len(clean_path)::]:
                                pass
                            else:
                                zip_file.write(file, arcname=file[len(clean_path)::])
                pbar.update(1)
            else:pass
    print('Done ✅')
    rmtree(clean_path+manga_path+'*', ignore_errors=True)
    print('28ix®')