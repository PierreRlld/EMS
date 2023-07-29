from zp_main import *
from zp_cover import *
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
        f = pd.read_excel("/Users/prld/git/EMS/origin.xlsx", sheet_name="SETTINGS",usecols="A:B")
        df = dict(zip(f.Manga_path, f.Manga))
        return df[name]

    f = pd.read_excel("/Users/prld/git/EMS/origin.xlsx", sheet_name="SETTINGS",usecols="B,O")
    df = f[f['up.py']==True]['Manga_path']
    manga_list = df.to_list()
    q1 = [
    inquirer.List(name='manga_choice',
                    message="Quel manga à update",
                    choices=manga_list,
                    carousel=True,
                ),
    inquirer.List(name='cover_update',
                     message="Update covers",
                     choices=['Yes','No'],
                     carousel=True),
    inquirer.List(name='scan_mode',
                     message="Scan update mode",
                     choices=['all','TBD update','select'],
                     carousel=True)
    ]
    p1 = inquirer.prompt(q1, theme=CustomTheme(), raise_keyboard_interrupt=True)
    a1, a2, a3 = p1['manga_choice'],p1['cover_update'],p1['scan_mode']
    a1 = name_code(a1)
    a2 = (a2=='Yes')
    if a3 == 'select':
        q2 = [
            inquirer.Text("start_scan", message="Start scan"),
            inquirer.Text("end_scan", message="End scan")
        ]
        p2 = inquirer.prompt(q2, theme=CustomTheme(), raise_keyboard_interrupt=True)
        if p2['end_scan'].isnumeric() == False:
            a4 = [int(p2['start_scan']),'max']
        else:
            a4 = [int(p2['start_scan']),int(p2['end_scan'])]
        return (a1, a2, a4)
    else:
        return(a1,a2, a3)

if __name__ == "__main__":
    try:
        print('-------------------------------------------------')
        size = check_repo_size("https://github.com/PierreRlld/EMS")
        print(">>> Repo. Git plein à",str(round(100*(size/1000/1000),1))+"%")
        main = manga_select()
        #print(main)
        print('-------------------------------------------------')
        if main[1]==True:
            zp_cover_dl(manga = main[0])
        zanpa(manga=main[0], scan_mode=main[2], arc=False)
    except KeyboardInterrupt:
        #Sortir du code avec ctrl+z ou ctrl+c
        quit()