# EMS

## zp_folder_pth.py edit
```python
global today, base_path, clean_path, output_dir, cover_dir, git_pth, hk_chapt_name, converted

#==== BASE_PATH used ====
cover_dir = '/Volumes/222EXT/222Covers/'
base_path = "/Volumes/222EXT/222Mangas_input/"
clean_path = "/Volumes/222EXT/222Mangas_clean/"
output_dir = '/Volumes/222EXT/222Mangas_output/'
converted = '/Volumes/222EXT/Converted/'
#git_pth = "https://github.com/PierreRlld/EMS"

# Noms de chapt =/= de "Ch.X" ou "Chapter X"
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
Architecture:
```
# Base storage
├── 222EXT
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
│   # Folders' name = 'Manga_path' in origin.xlsx  
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
│   # Code output folder  
│   └── 222Mangas_output
│   │   ├── (xxx)
│   │   │    ├── 'XXX Vol.X.zip'
│   │   └── [...]
│   │
│   # Variable: converted
│   └── Converted
│   │   ├── (xxx)
│   │   └── [...]
```

## Available


| Manga          | Manga_path                                 | Chapt | Update     | Source                                                                                                           | Statut | Commentaire                          |
| -------------- | ------------------------------------------ | ----- | ---------- | ---------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------ |
| 20thCB         | 20th Century Boys                          | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| BCL            | Black Clover                               | 365   | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Bleach         | Bleach                                     | F     | \-         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| Chainsaw       | Chainsaw Man                               | 119   | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| CJX            | Choujin X                                  | 40    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Conan          | Detective Conan                            | 1115  | \*         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      | Vol.3 End Of Volume Bonus Page       |
| DB             | Dragon Ball                                | F     | \-         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      |                                      |
| DBSuper        | Dragon Ball Super                          | 89    | \*         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      | Chapitre 34 image corrompue à delete |
| Gamaran        | Gamaran                                    | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ❌      |                                      |
| Gintama        | Gintama                                    | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| GTO            | GTO                                        | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| HellP          | Hell's Paradise Jigokuraku                 | F     | \-         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| HxH            | Hunter X Hunter                            | 400   | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| JJK            | Jujutsu Kaisen                             | 228   | 07/07/2023 | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Jojo1          | JoJo’s Bizarre Adventure                   | F     | \-         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      |                                      |
| Jojo2          | JoJo’s Bizarre Adventure                   | F     | \-         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      | Rename les couvertures               |
| Jojo3          | JoJo’s Bizarre Adventure                   | F     | \-         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      | Rename les couvertures               |
| Jojo4          | Jojo’s Bizarre Adventure Part 8 – Jojolion | F     | \-         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ✅      | Rename les couvertures               |
| Kaiju          | Kaiju No. 8                                | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ❌      |                                      |
| KNB            | Kuroko no Basuke                           | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Mashle         | Mashle                                     | 162   | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| MHA            | Boku no Hero Academia                      | 392   | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| NNTZ           | Nanatsu no Taizai                          | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| OP             | One Piece                                  | 1080  | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Opman          | Onepunch-Man                               | 178   | \*         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| SakDays        | Sakamoto Days                              | 125   | 07/07/2023 | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| SKR            | Sun-ken Rock                               | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| SNK            | Shingeki no Kyojin                         | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| SpyF           | Spy X Family                               | 85    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| SSY Lost Canva | Saint Seiya - The Lost Canva               | \-    | \*         | <a href="https://mangajar.com/"><img src="https://favicon.malsync.moe/?domain=https://mangajar.com/"> MJ</a>     | ❌      |                                      |
| TK             | Tokyo Ghoul                                | F     | \-         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      | renomer 2 derniers chapt             |
| TKre           | Tokyo Ghoulre                              | F     | \-         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| Vagabond       | Vagabond                                   | F     | \-         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| Vinland        | Vinland Saga                               | \-    | \*         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ❌      |                                      |
| YuGiOh         | Yu-Gi-Oh ! – Edition Double                | \-    | \*         | Sushi scans                                                                                                      | ✅      | Directement convertir en kindle      |
| Mob100         | Mob Psycho 100                             | \-    | \*         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ✅      |                                      |
| Tablier        | Gokushufudou The Way of the House Husband  | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ✅      |                                      |
| Kingdom        |                                            | \-    | \*         | <a href="https://mangaclash.com/"><img src="https://favicon.malsync.moe/?domain=https://mangaclash.com/"> MC</a> | ❌      |                                      |
| Naruto         | Naruto                                     | F     | \-         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ❌      |                                      |
| FireForce      | Enen no Shouboutai                         | \-    | \*         | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ❌      |                                      |
| Immortal       | Blade of the Immortal                      | \-    | \*         | <a href="https://mangajar.com/"><img src="https://favicon.malsync.moe/?domain=https://mangajar.com/"> MJ</a>     | ✅      |                                      |
| Monster        |                                            | \-    | \*         | <a href="https://mangajar.com/"><img src="https://favicon.malsync.moe/?domain=https://mangajar.com/"> MJ</a>     | ❌      |                                      |
| FMB            |                                            | \-    | \*         | <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MN</a>     | ❌      | Rename 108.6 et 108.7                |
| BlueL          | Blue Lock                                  | \-    | 07/07/2023 | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MF</a>             | ❌      |                                      |


## Notes
- Si pb Kindle converter conversion zip avec erreur " '._(...).jpeg' corrompu " deziper et convertir le dossier