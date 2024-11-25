from googlesearch import search
import requests
from bs4 import BeautifulSoup
from tkinter import *

def app():
    global _url
    global disp
    redditwin = Tk()
    redditwin.state('zoomed')
    redditwin.wm_title("ZEROTWO")
    redditwin.configure(background="black")

    _url = Entry(redditwin, width=70, bg="black", fg="skyblue", insertbackground="skyblue")
    _url.pack(pady=20)

    disp = Listbox(redditwin, width=225, height=40, background="black", foreground="skyblue")
    disp.pack()

    postbutton = Button(redditwin, text="GO", background="black", foreground="skyblue", command=reddit_post_details).place(x=0, y=0)
    
    
    
    redditwin.mainloop()

def reddit_post_details():
    url = _url.get().strip()
    
    # Check if the URL starts with http:// or https://, if not, prepend https://
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) redditwinleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Making the request
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        disp.insert(END, f"Error: {e}")
        return
    
    # Check if the request was successful
    if response.status_code != 200:
        disp.insert(END, f"Failed to retrieve page, status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1')
    if title:
        disp.insert(END, f"Title: {title.text.strip()}")
    else:
        disp.insert(END, "Title not found")

















        
    
    description = soup.find('p')
    if description:
        disp.insert(END, "\nDescription: " + description.text.strip())
    else:
        disp.insert(END, "Description not found")

    user = soup.find('a', {'class': 'author-name'})
    if user:
        disp.insert(END, "\nPosted by: " + user.text.strip())
    else:
        disp.insert(END, "User not found")

    community = soup.find('a', {'class': 'subreddit-name'})
    if community:
        disp.insert(END, "\nPosted in: " + community.text.strip())
    else:
        disp.insert(END, "Community not found")


app()
