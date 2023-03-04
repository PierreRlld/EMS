# EMS

## Available

- <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MangaFox</a>
- <a href="https://manganato.com"><img src="https://favicon.malsync.moe/?domain=https://manganato.com"> MangaNato</a>

| Manga_code_name | Manga_path                   | Status | Volumes | Last update | Source      |
| --------------- | ---------------------------- | ------ | ------- | ----------- | ----------- |
| BCL             | Black Clover                 | ✅      | 33      | 31/01/2023  | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MangaFox</a>|
| Bleach          | Bleach                       | ✅      | 74      | \-          | <a href="http://fanfox.net"><img src="https://favicon.malsync.moe/?domain=http://fanfox.net"> MangaFox</a>|
| CJX             | Choujin X                    | ✅      | 4       |             |             |
| Conan           | Conan                        | ✅      | 103     |             |             |
| Gamaran         | Gamaran                      | ✅      | 22      |             |             |
| Gamaran_        | Gamaran_                     | ✅      | 22      |             |             |
| Gintama         | Gintama                      | ✅      | 77      |             |             |
| GTO             | GTO                          | ❌      | ..      |             |             |
| HellP           | Hell's Paradise Jigokuraku   | ✅      | 13      |             |             |
| HxH             | Hunter X Hunter              | ✅      | 37      |             |             |
| JJK             | Jujutsu Kaisen               | ✅      | 21      |             |             |
| Mashle          | Mashle                       | ✅      | 14      |             |             |
| MHA             | Boku no Hero Academia        | ✅      | 36      |             |             |
| OP              | One Piece                    | ✅      | 106     | 31/01/2023  |             |
| OP_Arc          | One Piece                    | ✅      | 32      | 31/01/2023  |             |
| OPman           | Onepunch-Man                 | ❌      | ..      |             |             |
| SakDays         | Sakamoto Days                | ✅      | 9       |             |             |
| SKR             | Sun-ken Rock                 | ✅      | 21      |             |             |
| SpyF            | Spy X Family                 | ✅      | 10      |             |             |
| SSY Lost Canva  | Saint Seiya - The Lost Canva | ❌      | .       |             |             |
| TKre            | Tokyo Ghoulre                | ✅      | 16      |             |             |
| Vagabond        | Vagabond                     | ✅      | 37      |             |             |


## zp_folder_pth.py edit
```python
global today, base_path, clean_path, output_dir, cover_dir

#==== BASE_PATH used ====
base_path = "/Volumes/222EXT/222Mangas_input/"
clean_path = "/Volumes/222EXT/222Mangas_clean/"
output_dir = '/Volumes/222EXT/222Mangas_output/'
cover_dir = '/Volumes/222EXT/222Covers/'
```
Example:
```
# Base storage
├── 222EXT
│
│   # Variable: cover_dir  
│   # Cover storage folder  
│   ├── 222Covers
│   │   ├── test
│   │   ├── test
│   │   ├── test
│   │   └── test
│   │
│   # Variable: base_path 
│   # Hakuneko download output folder  
│   ├── 222Mangas_input
│   │   ├── test
│   │   ├── test
│   │   ├── test
│   │   └── test
│   │
│   # Variable: clean_path
│   # Intermediate folder (check if always empty after running code) 
│   ├── 222Mangas_clean
│   │   └── *empty*
│   │
│   # Variable: output_dir
│   # Code output folder  
│   └── 222Mangas_output
│       ├── test
│       ├── test
│       ├── test
│       └── test
```

## Notes
- Si pb Kindle converter conversion zip avec erreur " '._(...).jpeg' corrompu " deziper et convertir le dossier