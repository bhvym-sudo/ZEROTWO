import requests
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) redditwinleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
r = requests.get("https://www.youtube.com/watch?v=C1pjPv3WJyo", headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
# title = soup.find_all('h1')
# title = soup.find_all('yt-formatted-string')
print(soup)

