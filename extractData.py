from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as r
import pandas as pd
from pandas import json_normalize
from bs4 import BeautifulSoup



action_postURL= "https://www.casablanca-bourse.com/api/proxy/fr/api/bourse_data/instrument_history?fields%5Binstrument_history%5D=drupal_internal__id%2CcoursCourant%2CcumulVolumeEchange%2Ccreated%2ClowPrice%2ChighPrice%2CopeningPrice%2CclosingPrice%2CratioConsolide&sort%5Bdate-seance%5D%5Bpath%5D=created&sort%5Bdate-seance%5D%5Bdirection%5D=ASC&filter%5Binstrument%5D%5Bcondition%5D%5Bpath%5D=symbol.meta.drupal_internal__target_id&filter%5Binstrument%5D%5Bcondition%5D%5Bvalue%5D=500&filter%5Binstrument%5D%5Bcondition%5D%5Boperator%5D=%3D&page%5Boffset%5D=500&page%5Blimit%5D=250&filter%5Bfilter-date-start-vh-select%5D%5Bcondition%5D%5Bpath%5D=field_seance_date&filter%5Bfilter-date-start-vh-select%5D%5Bcondition%5D%5Boperator%5D=%3E%3D&filter%5Bfilter-date-start-vh-select%5D%5Bcondition%5D%5Bvalue%5D=2021-04-10"
res=r.get(action_postURL)
search_cookies=res.cookies

get_data={"Request Method":"GET","Status Code":"200 OK","Remote Address":"194.204.197.233:443","Referrer Policy":"strict-origin-when-cross-origin",
          "Date":"Fri, 10 May 2024 20:35:32 GMT","Expires":"Sun, 19 Nov 1978 05:00:00 GMT"}
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res_get=r.get(action_postURL,data=get_data,cookies=search_cookies,headers=header)
values=res_get.json()
#print(values)
gold_values=res_get.json()["data"]
#mettre les données dans un dataframe 
df=json_normalize(gold_values) 

#ecrire les données de dataframe dans excel ,noté que la méthode to_excel on peut l'utiliser seulement pour un dataframe 
df.to_excel("C:/Users/user/Desktop/py/donnees_bourse1.xlsx", index=False)
print("Données écrites dans le fichier 'donnees_bourse1.xlsx'")




