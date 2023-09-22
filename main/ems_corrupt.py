import os

def corrupt_remove(folder_path):
    for root,directories,files in os.walk(str(folder_path)):
        for file in files:
            if "._" in file:
                os.remove(folder_path+"/"+file)


if __name__ == "__main__":
    fold_pth = input('Path du dossier corrompu: ')
    corrupt_remove(folder_path=fold_pth)