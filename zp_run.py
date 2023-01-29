from zp_main import *
from zp_cover import *

#==== CHAPTERS ====
if __name__ == "__main__":
    manga_name = "OP"
    scan_mode = [1000,1040]
    arc = False

    zp_cover_dl(manga = manga_name)
    zanpa(manga=manga_name, scan_mode=scan_mode, arc=arc)