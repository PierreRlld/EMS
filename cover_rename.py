#%%
from zp_configure import (os, cover_dir)

def cover_renamer(manga):
    base_pth = cover_dir+manga+"/"
    for filename in os.listdir(cover_dir+manga):
        try:
            text = str(int(filename.split('-')[1][:-4]))+'.jpg' 
            #str(int()) à cause des ...-011.jpg par exp
            os.rename(os.path.join(base_pth, filename), os.path.join(base_pth, text))
        except:pass

#%%
if __name__ == "__main__":
    cover_renamer(manga="SKR")