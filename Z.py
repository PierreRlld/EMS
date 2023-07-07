# cd /Users/prld/Desktop/git_proj/EMS
from zp_main import *
from zp_cover import *

def input_client():
    try:
        manga_name = input('Manga Code Name : ')

        #>> Scan_mode
        scan_mode = input('Scan mode : ')
        if scan_mode in ['all','f','full','t','a']:
            scan_mode='all'
        elif scan_mode in ['update','up','u']:  # == on veut TBD !!
            scan_mode='update'
        else:
            start_scan = input('Start scan : ')
            end_scan = input('End scan : ')
            scan_mode = [int(start_scan), end_scan]

        #>> Couvertures
        cover_update = input('Update covers ? ')
        if str.lower(cover_update) in ['oui', 'y']:
            cover_update = True
        else:
            cover_update = False

        #>> Arc format
        #arc = input('Format arc ? ')
        #if str.lower(arc) in ['oui', 'y']:
        #    arc = True
        #else:
        #    arc = False

        print('----------------------------')
        
        if cover_update == True:
            zp_cover_dl(manga = manga_name)
        zanpa(manga=manga_name, scan_mode=scan_mode, arc=False)
    except KeyboardInterrupt:
        #Sortir du code avec ctrl+z ou ctrl+c
        quit()


if __name__ == "__main__":
    input_client()