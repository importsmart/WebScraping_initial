import bs4
import requests

res = requests.get('https://www.flipkart.com/witcher-3-wild-hunt-game-year-edition/p/itmemyy9ayg6ruyk?pid=GAMEMYY9N9AZQJ5J&lid=LSTGAMEMYY9N9AZQJ5JPKBWM4&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=91302d11-5b2b-40ce-a6bd-2052bc4b9208.GAMEMYY9N9AZQJ5J.SEARCH&ppt=sp&ppn=sp&ssid=vidiats4gg0000001584707237095&qH=959720b3f44d2c31')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
#returns beautiful soup object. Parsing html

prices = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
#get this by copying elemnt in inspect element

print(prices[0].text.strip())
#strip removes white spaces