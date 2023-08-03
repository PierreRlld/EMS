from main.zp_main import *
from main.zp_cover import *
import openpyxl

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

def name_code(name):
    f = pd.read_excel("/Users/prld/git/EMS/origin.xlsx", sheet_name="SETTINGS",usecols="A,P")
    df = dict(zip(f.edit_name, f.Manga))
    return df[name]

def manga_select():

    f = pd.read_excel("origin.xlsx", sheet_name="SETTINGS",usecols="P,O")
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

def edit_origin():

    f = pd.read_excel("origin.xlsx", sheet_name="SETTINGS",usecols="P,C")
    df = f[f["Chapt"].isin(["F","*"])==False]['edit_name']
    manga_list = df.to_list()

    q_manga = [
    inquirer.List(name='manga_choice',
                    message="Manga à update dans origin",
                    choices=manga_list+['↪ Quit'],
                    carousel=True,
                )
    ]
    a_manga = inquirer.prompt(q_manga, theme=CustomTheme(), raise_keyboard_interrupt=True)['manga_choice']
    if a_manga == "↪ Quit":
        quit()
    a_manga = name_code(a_manga)
    q_update = [
        inquirer.Text("vols", message="Vol à maj 'x,x' "),
        inquirer.Text("chapts", message="Chapt fin 'x,x' ")
    ]
    a_update = inquirer.prompt(q_update, theme=CustomTheme(), raise_keyboard_interrupt=True)

    vols = [x.replace(' ','') for x in a_update["vols"].split(',')]
    for vol in vols:
        try:
            int(vol)
        except:
            if vol.lower() != 'tbd':
                print(term.red('>> Value error in Volumes'))
                quit()
            else:
                vols[vols.index(vol)] = "TBD"
    try:
        chapts = [int(x) for x in a_update["chapts"].split(',')]
    except ValueError:
        print(term.red('>> Value error in Chapts'))
        quit()
    updates = dict(zip(vols,chapts))
    pd_wb = pd.read_excel("origin.xlsx", sheet_name="update_copy",usecols="A")
    pd_wb["xl_rows"] = [k for k in range(2,len(pd_wb)+2)]
    pd_wb = pd_wb.set_index("Vol",drop=True)
    pd_wb = pd_wb.to_dict()["xl_rows"]

    wb = openpyxl.load_workbook('origin.xlsx')
    ws = wb["update_copy"]
    ml = [c.value for c in ws["1"] if c.value != None]
    col_n = ml.index(a_manga)+1

    for v in updates.keys():
        ws.cell(row=pd_wb[v],column=col_n).value = updates[v]
    wb.save('origin.xlsx')
    return()

if __name__ == "__main__":
    print('-------------------------------------------------')
    size = check_repo_size(git_pth)
    print(">(info) Repo. Git plein à",str(round(100*(size/1000/1000),1))+"%\n")

    edit_origin()

    # ## scan download
    """
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
    """

    # ##
    print(term.gray90('28ix®'))