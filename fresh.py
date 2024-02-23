import requests
from bs4 import BeautifulSoup
import pandas as pd
name = []
price = []
for i in range(2,12):
    url1 = "https://www.flipkart.com/search?q=smartphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)

    

    r = requests.get(url1)
    soup = BeautifulSoup(r.text, "lxml")

    np = soup.find("a", class_="_1LKTO3").get("href")
    cnp = "https://www.flipkart.com/" + np

    pname = soup.find_all("div", class_="_4rR01T")
    for i in pname:
        pro_name = i.text
        name.append(pro_name)

    pprice = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in pprice:
        pro_price = i.text
        price.append(pro_price)

    data = pd.DataFrame({"Product name": name, "Price": price})
    print(data)
data.to_csv("product_detals.csv")
