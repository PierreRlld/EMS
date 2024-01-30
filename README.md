# EMS

## [!] installation
install : [Hakuneko](https://hakuneko.download/)

install : [Kindle Comic Converter](https://github.com/ciromattia/kcc?tab=readme-ov-file)

Python installation, in a new terminal:
```python
cd ; conda deactivate
conda create -n ems python=3.10
conda activate ems
cd <main-folder-path-frm-root>
pip install -r requirements.txt
cd main
python3 ems_run.py
```
Edit .zshrc file to add the following command:
```zsh
alias ems@r="conda activate ems  && cd <main-folder-path-frm-root> && python3 ems_run.py ; conda deactivate && cd"
```


## [!] ems_folder_pth.py : edit paths used

```python
global today, base_path, clean_path, output_dir, cover_dir, git_pth, hk_chapt_name, converted

#==== BASE_PATH used ====
cover_dir = '/Volumes/222EXT/222Covers/'
base_path = "/Volumes/222EXT/222Mangas_input/"
clean_path = "/Volumes/222EXT/222Mangas_clean/"
output_dir = '/Volumes/222EXT/222Mangas_output/'
converted = '/Volumes/222EXT/Converted/'
#git_pth = "https://github.com/PierreRlld/EMS"

# Chapitres avec noms différents de "Ch.X" ou "Chapter X"
# Compléter la liste si nécessaire
hk_chapt_name = ['Page',
                 'Days',
                 'Kapitel',
                 'Lesson',
                 'Level',
                 'Episode',
                 'No.',
                 'Quarter',
                 "#",
                 "Prologue",
                 "Class",
                 "Z="]

```
**Architecture**
```
# Base storage
├── /Volumes/222EXT/
│
│   # Variable: cover_dir
│   # Cover storage folder
│   ├── 222Covers
│   │   ├── (xxx)
│   │   │    ├── 1.jpeg
│   │   │    └── [...].jpeg 
│   │   └── [...]
│   │
│   # Variable: base_path 
│   # Hakuneko download output folder
│   # Folders'name (xxx) = 'Manga_path' in origin.xlsx
│   # 'Chapt xxx' is an empty folder once 'ems_chapt_central.py' ran
│   ├── 222Mangas_input 
│   │   ├── (xxx)
│   │   │    ├── 'Chapt xxx'
│   │   │    │    └── *empty* 
│   │   │    ├── 'Chapt xxx'
│   │   │    │    └── *empty*
│   │   │    └── [...]
│   │   └── [...]
│   │
│   # Variable: clean_path
│   # Cleaned version of previous folder
│   # Updated with 'ems_chapt_central.py'
│   ├── 222Mangas_clean
│   │   ├── (xxx)
│   │   │    ├── 'Vol.X Chapter X'
│   │   │    ├── 'Vol.X Chapter X'
│   │   │    └── [...]
│   │   └── [...]
│   │
│   # Variable: output_dir
│   # Code output folder for 'ems_run.py'
│   └── 222Mangas_output
│   │   ├── (xxx)
│   │   │    ├── 'XXX Vol.X.zip'
│   │   └── [...]
│   │
│   # Variable: converted
│   # Stores hand-converted files
│   # 'TBD update' option tries to replace 'XXX TBD.cbz'
│   └── Converted
│   │   ├── (xxx)
│   │   │    ├── 'XXX Vol.X.cbz'
│   │   └── [...]
```

## Available

| Manga                        | Chapt | Vol | Source                                                                                                                     | Statut | /!\\ N.B /!\\                                                              |
| ---------------------------- | ----- | --- | -------------------------------------------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| 20th Century Boys            | F     | 22  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      | Ch223img2 / Ch225img1                                                      |
| 21st Century Boys            | F     | 2   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Akame ga Kill                | F     | 15  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Akame ga Kill - Zero         | F     | 10  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Akira                        | F     | 6   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Assassination Classroom      | F     | 21  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Bakemonogatari               | 157   | 18  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |  + manga-scan.co                                                           |
| Baki1 - Grappler             | 371   | 42  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Baki2 - New Grappler         | 31    | 31  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Baki3 - Hanma: son of ogre   | 312   | 37  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Baki4: Baki-dou1             | 198   | 22  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Baki5: Baki-dou2             | 151   | 17  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Black Clover                 | 368   | 35  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Berserk                      | 374   | 41  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Berserk prologue             | F     | 4   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      | /!\\ Créer dossier Berserk_prologue & déplacer Prologue du dossier Berserk |
| Bleach                       | F     | 74  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Blue Lock                    | 233   | 25  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Chainsaw Man                 | 143   | 15  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Choujin X                    | 41    | 6   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Detective Conan              | 1118  | 103 | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>               | ✅      | Vol.3 End Of Volume Bonus Page                                             |
| Dragon Ball                  | F     | 42  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Dragon Ball Super            | 89    | 19  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      | Ch34img07,27,39                                                            |
| Death Note                   | F     | 12  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Demon Slayer                 | F     | 23  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Dr Stone                     | F     | 26  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Dr Stone - Byakuya           | F     | 1   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Fire Force                   | 304   | 34  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Full Metal Alchemist         | F     | 27  | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>               | ✅      |                                                                            |
| Gamaran                      | F     | 22  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Gantz                        | F     | 37  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Gintama                      | F     | 77  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| GTO                          | F     | 25  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| Hell's Paradise              | F     | 13  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Hunter X Hunter              | 400   | 37  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Ikigami                      | 60    | 10  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Blade of the Immortal        | F     | 30  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Hajime no Ippo               | 1433  | 138 | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Issak                        | 41    | 9   | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>               | ✅      |                                                                            |
| Jagaaan                      | 161   | 14  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Jujutsu Kaisen               | 236   | 23  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      | DL jusqu'au 594 !                                                          |
| Jojo1                        | F     | 5   | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Jojo2                        | F     | 12  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Jojo3                        | F     | 28  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Jojo4                        | F     | 46  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Jojo5                        | F     | 63  | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a>           | ✅      |                                                                            |
| Jojo6                        | F     | 17  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Jojo7                        | F     | 24  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Jojo8                        | F     | 27  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Jojo9                        | 7     | 1   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Kaiju No. 8                  | 93    | 10  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Kingdom                      | 768   | 70  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Kuroko no Basket             | F     | 30  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Mariko                       | F     | 1   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Mashle                       | 162   | 16  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| My Hero Academia             | 400   | 38  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Mob Psycho 100               | F     | 16  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Monster                      | F     | 18  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Montage                      | F     | 19  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Moriarty                     | 76    | 19  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Naruto                       | F     | 72  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Nanatsu no Taizai            | F     | 41  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| Noragami                     | 107   | 26  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| One Piece                    | 1092  | 106 | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Onepunch Man                 | 189   | 27  | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>               | ✅      |                                                                            |
| Prison School                | F     | 28  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Sakamoto Days                | 135   | 13  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Sidooh                       | F     | 25  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Sun-ken Rock                 | F     | 0   | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ❌      |                                                                            |
| Slamdunk                     | F     | 31  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| Shingeki no Kyojin           | F     | 34  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Soul Eater                   | F     | 25  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Spy X Family                 | 85    | 11  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| Saint Seiya - The Lost Canva | F     | 0   | <a href="https://mangajar.com/"><img src="https://favicon.malsync.moe/?domain=https://mangajar.com/"> MJ</a>               | ❌      |                                                                            |
| The Way of the House Husband | 104   | 11  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>                       | ✅      |                                                                            |
| Tokyo Ghoul                  | F     | 14  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Tokyo Ghoulre                | F     | 16  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Tokyo Revengers              | F     | 31  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Vagabond                     | F     | 37  | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>               | ✅      |                                                                            |
| Vinland Saga                 | 203   | 27  | <a href="https://www.mangasee123.com/"><img src="https://favicon.malsync.moe/?domain=https://www.mangasee123.com/"> MS</a> | ✅      |                                                                            |
| Yu-Gi-Oh                     | F     | 19  | <a href="https://sushiscan.net/"><img src="https://favicon.malsync.moe/?domain=https://sushiscan.net/"> SS</a>             | ✅      |                                                                            |

## Notes
- Si pb Kindle converter conversion zip avec erreur " '._(...).jpeg' corrompu " deziper et convertir le dossier