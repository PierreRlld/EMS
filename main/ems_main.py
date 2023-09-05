from main.zp_configure import *
from zp_folder_pth import *

#-----------------------
def get_settings(Name, xlsx): 
    set = pd.read_excel(xlsx, sheet_name='SETTINGS', usecols='A:I')         #VERFIER usecols dans origin.xlsx
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
            chapt = round(float(re.findall(r'\d+',y)[0]))
            vol = round(float(re.findall(r'\d+',re.search(r'Vol.\d+',el).group(0))[0]))
            spe_dic[chapt]=vol
        return spe_dic

#-----------------------
def meta_group_chapt(el_list, volumes, pth, dic, TBD):
    long = len(pth) + 1

    group = {i:[] for i in range(1,volumes+1)}
    if TBD==True:
        group['TBD'] = []

    for el in el_list:
        vol = dic[round(float(el[long::].split(' ')[1].split('-')[1].split('/')[0]))]   #<Vol.XX Chapter-XX>
        group[vol].append(el)

    return group    

#-----------------------
#-----------------------
def zanpa(manga: str, scan_mode):
    '''
    @manga : name to be saved as = name in origin.xlsx
    @scan_mode : [scan_start, scan_end] / "all" / update > scan_end (int) or "max"
    '''
    xlsx = pd.ExcelFile('origin.xlsx')
    set = get_settings(manga, xlsx)
    manga_dic = get_dic(manga, set['Manga_path'], xlsx)
    #print(manga_dic, len(manga_dic))
    manga_path = set['Manga_path']
    print('>>> Converting '+manga_path)
    
    # TODO : à changer
    dir_name = clean_path+manga_path+"*"
    # TODO : vérif + changement surement
    chapt_renamer(Name_path=set['Manga_path'], mode=scan_mode, dic=manga_dic, 
                  volumes=int(set['Volumes']), TBD=set['TBD'])                                        #>>enregistrés dans dir_name
    filePaths = retrieve_file_paths(dir_name)
    
    grouped = meta_group_chapt(el_list=filePaths[1::], volumes=int(set['Volumes']), 
                                pth=dir_name, dic=manga_dic, TBD=set['TBD'])   #.DS_Store à enlever

    fold_id = "_"+str(len(next(os.walk(output_dir))[1]))
    os.mkdir(os.path.join(output_dir, " ".join([today+fold_id, manga])))
    nb_converted_vol = len([k for k in list(grouped.keys()) if grouped[k]!=[]]) 
    with tqdm(total=nb_converted_vol) as pbar:
        for vol in list(grouped.values()) : 
            if vol!=[]:
                num = list(grouped.keys())[ list(grouped.values()).index(vol) ]     #key dans le dic à partir élément = bon num volume
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
    return output_dir+today+fold_id+' '+manga
