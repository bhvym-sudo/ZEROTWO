from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time
r = []
for url in search("bhavyamverma site:linkedin.com", tld="co.in", num=10, stop=30, pause=2):     
    f = url.split()
    r.append(f[0])
u = [urls for urls in r if "/in/" in urls]
print(u)

