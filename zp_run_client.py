from zp_main import *
from zp_cover import *

def input_client():
    try:
        manga_name = input('Manga Code Name : ')

        #>> Scan_mode
        scan_mode = input('Scan mode : ')
        if str.isnumeric(scan_mode)==False:
            scan_mode='all'
        else:
            start_scan = input('Start scan : ')
            end_scan = input('End scan : ')
            scan_mode = [int(start_scan), int(end_scan)]

        #>> Couvertures
        cover_update = input('Update covers ? ')
        if str.lower(cover_update) in ['oui', 'y']:
            cover_update = True
        else:
            cover_update = False

        #>> Arc format
        arc = input('Format arc ? ')
        if str.lower(arc) in ['oui', 'y']:
            arc = True
        else:
            arc = False

        print('----------------------------')
        
        if cover_update == True:
            zp_cover_dl(manga = manga_name)
        zanpa(manga=manga_name, scan_mode=scan_mode, arc=arc)
    except KeyboardInterrupt:
        #Sortir du code avec ctrl+z ou ctrl+c
        quit()


if __name__ == "__main__":
    input_client()