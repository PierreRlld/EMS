from main.zp_main import *
from main.zp_cover import *

term = Terminal()

class CustomTheme(Default):
    def __init__(self):
        super().__init__() 
        self.List.selection_cursor = "➤"
        self.Checkbox.selection_icon = "➤"
        self.List.selection_color = term.green
        self.Checkbox.selection_color = term.green
        self.Checkbox.selected_color = term.green
        self.Checkbox.unselected_icon = "*"


def manga_select():

    def name_code(name):
        f = pd.read_excel("/Users/prld/git/EMS/origin.xlsx", sheet_name="SETTINGS",usecols="A,P")
        df = dict(zip(f.edit_name, f.Manga))
        return df[name]

    f = pd.read_excel("/Users/prld/git/EMS/origin.xlsx", sheet_name="SETTINGS",usecols="P,O")
    df = f[f['up.py']==True]['edit_name']
    manga_list = df.to_list()
    q_manga = [
    inquirer.List(name='manga_choice',
                    message="Quel manga à update",
                    choices=manga_list+['↪ Quit'],
                    carousel=True,
                )
    ]
    q_param = [
    inquirer.List(name='cover_update',
                     message="Update covers",
                     choices=['Yes','No'],
                     carousel=True),
    inquirer.List(name='scan_mode',
                     message="Scan update mode",
                     choices=['all','TBD update','select'],
                     carousel=True)
    ]

    a_manga = inquirer.prompt(q_manga, theme=CustomTheme(), raise_keyboard_interrupt=True)['manga_choice']
    if a_manga == "↪ Quit":
        quit()
    p_param = inquirer.prompt(q_param, theme=CustomTheme(), raise_keyboard_interrupt=True)
    a_cover, a_mode = p_param['cover_update'],p_param['scan_mode']
    a_manga = name_code(a_manga)
    a_cover = (a_cover=='Yes')
    if a_mode == 'select':
        q_scan = [
            inquirer.Text("start_scan", message="Start scan"),
            inquirer.Text("end_scan", message="End scan")
        ]
        p_scan = inquirer.prompt(q_scan, theme=CustomTheme(), raise_keyboard_interrupt=True)
        if p_scan['end_scan'].isnumeric() == False:
            a_scan = [int(p_scan['start_scan']),'max']
        else:
            a_scan = [int(p_scan['start_scan']),int(p_scan['end_scan'])]
        return (a_manga, a_cover, a_scan)
    else:
        return(a_manga,a_cover, a_mode)


if __name__ == "__main__":
    print('-------------------------------------------------')
    size = check_repo_size(git_pth)
    print(">(info) Repo. Git plein à",str(round(100*(size/1000/1000),1))+"%\n")
    main = manga_select()
    print(term.gold3("➜ Update {} - Cover update {} - Scan {} ?".format(*main)))
    conf = [
    inquirer.List(name='conf',
                  message="Confirm",
                  choices=['Yes','No'],
                  carousel=True)
    ]
    conf = inquirer.prompt(conf, theme=CustomTheme(), raise_keyboard_interrupt=True)['conf']
    if conf == "No":
        quit()
    print('-------------------------------------------------')
    if main[1]==True:
        zp_cover_dl(manga = main[0])
    zanpa(manga=main[0], scan_mode=main[2], arc=False)