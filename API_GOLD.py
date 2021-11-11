import requests
import pandas as pd
import numpy as np
import os
import re
import glob
from bs4 import BeautifulSoup
result = []
r = requests.get("https://www.goldtraders.or.th/")
#soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(r.text, "html.parser")
data = soup.find_all("div", {"class": "main-panel"})
datause = data[0]
datause1 = datause.select('div',id="DetailPlace_uc_goldprices1_GoldPricesUpdatePanel")
#print(datause1[0])
#print(datause)
for post in datause1:
    try:
        price = post.find(id="DetailPlace_uc_goldprices1_lblBLSell").text.split(' ')[0]
        price1 = post.find(id="DetailPlace_uc_goldprices1_lblBLBuy").text.split(' ')[0]
        price2 = post.find(id="DetailPlace_uc_goldprices1_lblOMSell").text.split(' ')[0]
        price3 = post.find(id="DetailPlace_uc_goldprices1_lblOMBuy").text.split(' ')[0]
        result.append({'ทองคำแท่ง 96.5% ขายออก': price,'ทองคำแท่ง 96.5% รับซื้อ': price1,'ทองรูปพรรณ 96.5% ขายออก': price2,'ทองรูปพรรณ 96.5% รับซื้อ': price3})
    except:
        break
    df = pd.DataFrame(data=result)
    print(df)
