#function to give flipkart price

import bs4, requests

def getprice(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    return elems[0].text.strip()



price = getprice('https://www.flipkart.com/park-avenue-good-morning-grooming-kit/p/itm5780ba7567ac6?pid=CBKEQK85BKNVXGV6&lid=LSTCBKEQK85BKNVXGV6CBUF7Z&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_1_3.bannerX3.BANNER_bgm-big-shopping-days-store_2TXZIG2UZJYB&fm=neo%2Fmerchandising&iid=1fee745b-4d53-441a-af6c-4af1eda3ddb7.CBKEQK85BKNVXGV6.SEARCH&ppt=browse&ppn=browse&ssid=rw1cywemo00000001584708101959')
print('The price is ' + price)