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
def cover_link_scraper(url):
    page = url_request(url)
    layer = {}
    all_li = page.find("ul", {"class":"editorial grid issue-grid js-simple-paginator-container"}).findAll("li")
    #print(all_li)
    for li in all_li:
        #link = li.find("div",{'class':'imgboxart'}).find('img').get('src')
        link = str(li.find("a").get('href'))
        link = 'https://comicvine.gamespot.com'+link
        nb = str(li.find("p",{'class':'issue-number'}).text.split('#')[1])
        layer[nb]=link
    return layer

#--------------------
#--------------------   
def cov_dl(url, manga):
    dic = cover_link_scraper(url)

    if os.path.exists(cover_dir+manga) == False:
        os.mkdir(os.path.join(cover_dir,manga))
    else:
        pass
    
    nb_dl = len(list(dic.keys()))
    with tqdm(total=nb_dl) as pbar:
        for vol in list(dic.keys()):
            link = dic[vol]
            page = url_request(link)
            img = page.find('div',{'class':'img imgboxart issue-cover'}).find('img').get('src')
            pth = os.path.join(cover_dir+manga, vol+".jpg")
            with open(pth, "wb") as f:
                f.write(requests.get(img).content)  
            pbar.update(1)

cov_dl('https://comicvine.gamespot.com/sakamoto-days/4050-135095/','SakDays')