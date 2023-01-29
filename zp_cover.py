import bs4
from urllib import request
import requests
from zp_configure import *
from folder_pth import *

op_url = 'https://comicvine.gamespot.com/one-piece/4050-21397/'

#--------------------
def url_request(url):
    reqt = request.urlopen(url).read()
    page = bs4.BeautifulSoup(reqt, "lxml")    #bien une page html maintenant 
    return page

#--------------------
def pages_list(url):
    page = url_request(url)
    class_nav = ['paginate__item', 'paginate__item on']

    nav = page.find("div", {"class":"navigation"}).find_all("li")
    if nav==[]:
        return [url]
    else:
        pg_list = []
        for li in nav:
            if " ".join(li.get('class')) in class_nav:
                pg_list.append('https://comicvine.gamespot.com'+li.find("a").get("href"))
        return pg_list

#--------------------
def cover_link_scraper(url):
    page = url_request(url)
    layer = {}
    all_li = page.find("ul", {"class":"editorial grid issue-grid js-simple-paginator-container"}).find_all("li")
    #print(all_li)
    for li in all_li:
        #link = li.find("div",{'class':'imgboxart'}).find('img').get('src')
        link = str(li.find("a").get('href'))
        link = 'https://comicvine.gamespot.com'+link
        nb = int(li.find("p",{'class':'issue-number'}).text.split('#')[1])
        layer[nb]=link
    return layer

#--------------------
def cov_dl(url, manga, update):
    dic = cover_link_scraper(url)
    next_page = True
    page_volumes = list(dic.keys())
    for key in page_volumes :
        if key<update:
            del dic[key]
            next_page=False #Sert de break pour pas aller voir les pages suivantes

    if os.path.exists(cover_dir+manga) == False:
        os.mkdir(os.path.join(cover_dir,manga))
    
    nb_dl = len(list(dic.keys()))
    with tqdm(total=nb_dl) as pbar:
        for vol in list(dic.keys()):
            link = dic[vol]
            page = url_request(link)
            img = page.find('div',{'class':'img imgboxart issue-cover'}).find('img').get('src')
            pth = os.path.join(cover_dir+manga, str(vol)+".jpg")
            with open(pth, "wb") as f:
                f.write(requests.get(img).content)  
            pbar.update(1)
    return next_page

#--------------------
#--------------------
def zp_cover_dl(url, manga):

    try:
        nul = '.DS_Store' in os.listdir(cover_dir+manga)
        dispo = len(os.listdir(cover_dir+manga)) - nul
    except:
        dispo=0

    pages = pages_list(url)
    for page in pages :
        print('Downloading page {0}/{1}'.format(pages.index(page)+1, len(pages)))
        if cov_dl(url = page, manga = manga, update = dispo) == False:
            print('Done ✅')
            return None

zp_cover_dl(url="https://comicvine.gamespot.com/one-piece/4050-21397/", manga="OP")
#cov_dl(url="https://comicvine.gamespot.com/sakamoto-days/4050-135095/", manga='SakDays', update = 9)

