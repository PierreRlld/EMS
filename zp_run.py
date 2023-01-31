from zp_main import *
from zp_cover import *

#==== CHAPTERS ====
if __name__ == "__main__":
    manga_name = "Bleach"
    scan_mode = [120,130]
    arc = False
    cover_update = True

    zp_cover_dl(manga = manga_name)
    zanpa(manga=manga_name, scan_mode=scan_mode, arc=arc)