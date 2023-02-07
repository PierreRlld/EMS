from zp_main import *
from zp_cover import *

#==== RUN ====
if __name__ == "__main__":
    manga_name = "Jojo2"
    scan_mode = [616,626]
    arc = False
    cover_update = True

    zp_cover_dl(manga = manga_name)
    zanpa(manga=manga_name, scan_mode=scan_mode, arc=arc)