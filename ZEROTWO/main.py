from tkinter import *
from tkinter import messagebox
import base64
from tkinter import ttk
from googlesearch import search
import wikipedia
import random
import requests
from bs4 import BeautifulSoup


# TODO
# 3) display tweets!!!!
# 4) display reddit post and comments!!!
# 6) make a proper logo(I need to hire someone again for free)
# 10) make a whole new window where there will be a huge list box and it will show the reddit and twitter posts(separately) with timings
#     and other things just like in snowden movie
# 11) most importantly figure out how to extract twitter and reddit posts with timings and other things 
# 12) make more new random display quotes ask for somebody help if needed lol
# 13) find more ways to extract information from internet
# 14) remember your main motive is to make a intelligence and osint app, with low system requirements , fast and reliable
#     with many features available

root = Tk()

displaywords = ['The sun rises from the east:)', 'Developer was cooked while developing this', 'Dont go to r/jeeneetards', 'Hi!, My name is!........', 'Learning languages is good for you colonizer -Duolingo', 'Dont ask me for help, do it your own']
randomdis = random.choice(displaywords)

def infomenu():
    messagebox.showinfo("About us", 
    """
    ZEROTWO V 0.0.3
    Made by BHVYM
    
    
    
    """)

def helpmenu():
    messagebox.showinfo("Lets help you",
    """
    enter your target in query name
    enter keywords related to query
    enter number of urls you want
    select the website you want to
    see results of.
    run!
    
    
    
    
    
    """)


mainmenu = Menu(root)
mainmenu.add_command(label="About us", command=infomenu)

root.config(menu = mainmenu)


def get_reddit_post_details():
    url = "https://www.reddit.com/r/unitedstatesofindia/comments/1du5ryx/what_a_poor_display_of_character_from_prime/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Making the request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page, status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1')
    if title:
        print(f"Title: {title.text.strip()}")
    else:
        print("Title not found")
    
    description = soup.find('p')
    if description:
        print("\nDescription: " + description.text.strip())
    else:
        print("Description not found")

    user = soup.find('a', {'class': 'author-name'})
    if user:
        print("\nPosted by: " + user.text.strip())
    else:
        print("User not found")

    community = soup.find('a', {'class': 'subreddit-name'})
    if community:
        print("\nPosted in: " + community.text.strip())
    else:
        print("Community not found")

def filter_twitter_urls(url_list):
    try:
        urls = int(t5.get())
        twitter_urls = [url for url in url_list if "twitter.com" in url]
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        
        
        return twitter_urls
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return twitter_urls
        

def filter_instagram_urls(url_list):
    try:
        insta_urls = [url for url in url_list if "instagram.com" in url]
        urls = int(t5.get())
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        return insta_urls
    
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return insta_urls

def filter_reddit_urls(url_list):
    try:
        reddit_urls = [url for url in url_list if "reddit.com" in url]
        urls = int(t5.get())
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        return reddit_urls
    
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return reddit_urls
    
    

def filter_youtube_urls(url_list):
    try:
        youtube_urls = [url for url in url_list if "youtube.com" in url]
        urls = int(t5.get())
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        return youtube_urls
    
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return youtube_urls

def filter_wikipedia_urls(url_list):
    try:
        wikipedia_urls = [url for url in url_list if "wikipedia.org" in url]
        urls = int(t5.get())
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        return wikipedia_urls
    
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return wikipedia_urls

def filter_facebook_urls(url_list):
    try:
        facebook_urls = [url for url in url_list if "facebook.com" in url]
        urls = int(t5.get())
        wiki = str(wikipedia.summary(query, urls))
        wiki = wiki.split(". ")
        result_urls_scrap.delete(0, urls)
        for w in wiki:
            result_urls_scrap.insert(END, w)
        return facebook_urls
    
    except:
        result_urls_scrap.delete(0, urls)
        result_urls_scrap.insert(END, "No such results")
        result_urls_scrap.itemconfig(0, {'fg':'red', 'bg':'black'})
        return facebook_urls

def login():
    try:
    
        user = t1.get()
        passw = t2.get()
        encuser = base64.b64encode(bytes(user, 'utf-8'))
        encpass = base64.b64encode(bytes(passw, 'utf-8'))

        username1 = base64.b64encode(bytes("narender", 'utf-8'))
        password1 = base64.b64encode(bytes("modi", 'utf-8'))


        if encuser ==  username1 and encpass == password1:
            mainscreen()       
        
        if encuser !=  username1 or encpass != password1:        
            messagebox.showerror("Error", "Please check username and password again") 
            t1.delete("1.0", 'end-1c')
            t2.delete("1.0", 'end-1c') 
    
    except:
        print("Chill!")


def search_web():
    
    global query
    global keywords
    query = t3.get()
    keywords = t4.get("1.0", 'end-1c')
    
    
    if query == "" or keywords == "" or t5.get() == "":
        messagebox.showerror("Error", "Please fill out properly")
    
    else:
        try:
            urlval = int(t5.get())
            result_urls.delete(0, urlval)
            keyword = keywords.split()
            for keys in keyword:
                pass
            
            result_urls.insert(END, f"showing {urlval} results for {query}")
            result_urls.itemconfig(0, {'fg':'red'})
            results = []
            
            
            if combo.get() == "twitter":
                result_urls.delete(0, urlval)
                for j in search(f"{query} site:twitter.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = j.split()
                    results.append(forfilter[0])
                twitters = filter_twitter_urls(results)
                result_urls.insert(END, f"showing results for {query} on twitter")
                result_urls.itemconfig(0, {'fg':'red'})
                for url in twitters:
                    urls = url.replace("twitter", "x")
                    result_urls.insert(END, urls)
            

            elif combo.get() == "reddit":
                result_urls.delete(0, urlval)
                for k in search(f"{query} site:reddit.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = k.split()
                    results.append(forfilter[0])
                reddit = filter_reddit_urls(results)
                result_urls.insert(END, f"showing results for {query} on reddit")
                result_urls.itemconfig(0, {'fg':'red'})
                for reurl in reddit:
                    result_urls.insert(END, reurl)

            elif combo.get() == "instagram":
                result_urls.delete(0, urlval)
                for l in search(f"{query} site:instagram.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = l.split()
                    results.append(forfilter[0])
                insta = filter_instagram_urls(results)
                result_urls.insert(END, f"showing results for {query} on instagram")
                result_urls.itemconfig(0, {'fg':'red'})
                for iurl in insta:
                    result_urls.insert(END, iurl)
            
            elif combo.get() == "facebook":
                result_urls.delete(0, urlval)
                for m in search(f"{query} site:facebook.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = m.split()
                    results.append(forfilter[0])
                fb = filter_facebook_urls(results)
                result_urls.insert(END, f"showing results for {query} on facebook")
                result_urls.itemconfig(0, {'fg':'red'})
                for fburl in fb:
                    result_urls.insert(END, fburl)
            
            elif combo.get() == "youtube":
                result_urls.delete(0, urlval)
                for n in search(f"{query} site:youtube.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = n.split()
                    results.append(forfilter[0])
                yt = filter_youtube_urls(results)
                result_urls.insert(END, f"showing results for {query} on youtube")
                result_urls.itemconfig(0, {'fg':'red'})
                for yturl in yt:
                    result_urls.insert(END, yturl)
            
            elif combo.get() == "wikipedia":
                result_urls.delete(0, urlval)
                for o in search(f"{query} site:wikipedia.com", tld="co.in", num=10, stop=urlval, pause=2):     
                    forfilter = o.split()
                    results.append(forfilter[0])
                wp = filter_wikipedia_urls(results)
                result_urls.insert(END, f"showing results for {query} on wikipedia")
                result_urls.itemconfig(0, {'fg':'red'})
                for wpurl in wp:
                    result_urls.insert(END, wpurl)

            
            else:
                for p in search(query, tld="co.in", num=10, stop=urlval, pause=2):     
                    result_urls.insert(END, p)
                    forfilter = p.split()
                    results.append(forfilter[0])
        except:
            messagebox.showerror("Error!", 
            """
            Now due to complexity of code, 
            many error can occur, 
            try following steps:
            
            1)Please enter an integer in 'no of url'.
            2)Check your internet connection.
            3)Maybe there are no such results of 
            the query
            
            """)
        # print(results)


def mainscreen():
    root.destroy()
    global app
    global result_urls
    app = Tk()
    photo = PhotoImage(file = "image.png")
    app .iconphoto(False, photo)
    app.state('zoomed')
    app.wm_title("ZEROTWO")
    app.configure(background="black")
    
    
    

    search_area = Frame(height=570, width=530, bg="black", borderwidth=3, highlightthickness=1, highlightbackground="skyblue")
    search_area.place(x=2,y=100)
    
    resulturl_area = Frame(height=570, width=780, bg="black", borderwidth=3, highlightthickness=1, highlightbackground="skyblue")
    resulturl_area.place(x=550,y=100)

    # result_are = Frame(height=340, width=760, bg="black", highlightthickness=1, highlightbackground="skyblue")
    # result_are.place(x=550, y=330)


    
    l4 = Label(app, text="ZEROTWO PROJECT", height=1, width=43, bg="black", fg="violet")
    l4.place(x=0,y=0)
    l4.config(font=("Courier", 40))

    l5 = Label(app, text="query name:", height=1, width=11, bg="black", fg="magenta")
    l5.place(x=5,y=130)
    l5.config(font=("Valmera Bold", 15))


    l9 = Label(app, text="URL:", height=1, width=4, bg="black", fg="magenta")
    l9.place(x=600,y=130)
    l9.config(font=("Valmera Bold", 15))

    l10 = Label(app, text="website filter:", height=1, width=11, bg="black", fg="magenta")
    l10.place(x=13,y=350)
    l10.config(font=("Valmera Bold", 15))

    global t3
    global t4
    global t5
    global combo
    global result_urls_scrap
    

    t3 = Entry(app, width=30, bg="black", fg="skyblue", borderwidth=2, insertbackground="skyblue", highlightthickness=1, highlightbackground="purple", highlightcolor="violet")
    t3.place(x=150, y=135)
    #t3.config(font=("Valmera Bolda", 14))

    t4 = Text(app, height=5,  width=30, bg="black", fg="skyblue", borderwidth=2, insertbackground="skyblue", highlightthickness=1, highlightbackground="purple", highlightcolor="violet")
    t4.place(x=150, y=190)
    


    result_urls = Listbox(app, height=11, width=93, bg="black", fg="skyblue", borderwidth=2, relief=SUNKEN, highlightthickness=1, highlightbackground="purple", highlightcolor="violet")
    result_urls.place(x=700, y=110)

    result_urls_scrap = Listbox(app, height=18, width=119, bg="black", fg="skyblue", borderwidth=2, relief=SUNKEN, highlightthickness=1, highlightbackground="purple", highlightcolor="violet")
    result_urls_scrap.place(x=570, y=350)

    s1 = Scrollbar(app)
    result_urls.config(yscrollcommand = s1.set)
    s1.pack(side=RIGHT)   
    s1.place(x=1265, y=110, height=170)
    s1.config(command=result_urls.yview)

    s2 = Scrollbar(app, orient='horizontal')
    result_urls.config(xscrollcommand = s2.set)
    s2.pack(side=BOTTOM)   
    s2.place(x=700, y=285, width=565)
    s2.config(command=result_urls.xview)
    
    s3 = Scrollbar(app)
    result_urls_scrap.config(yscrollcommand = s3.set)
    s3.pack(side=RIGHT)   
    s3.place(x=1290, y=350, height=290)
    s3.config(command=result_urls.yview)

    s4 = Scrollbar(app, orient='horizontal')
    result_urls_scrap.config(xscrollcommand = s4.set)
    s4.pack(side=BOTTOM)   
    s4.place(x=570, y=645, width=720)
    s4.config(command=result_urls_scrap.xview)
    

    l6 = Label(app, text="keywords:", height=1, width=8, bg="black", fg="magenta")
    l6.place(x=13,y=185)
    l6.config(font=("Valmera Bold", 15))

    l7 = Label(app, text=f"{randomdis}", height=1, width=130, bg="black", fg="skyblue")
    l7.place(x=100,y=65)
    l7.config(font=("Valmera Bold", 12))

    l8 = Label(app, text="no of url:", height=1, width=7, bg="black", fg="magenta")
    l8.place(x=15,y=300)
    l8.config(font=("Valmera Bold", 15))

    t5 = Entry(app, width=10, bg="black", fg="skyblue", borderwidth=2, insertbackground="skyblue", highlightthickness=1, highlightbackground="purple", highlightcolor="violet")
    t5.place(x=150, y=305)
    
    _help = Button(app, bg="black", fg="skyblue", activebackground="skyblue", text="HELP", command=helpmenu)
    _help.place(x=2,y=2)
    
    b2 = Button(app, text="run this shit", command=search_web, bg="black", fg="skyblue", relief=RAISED, activebackground="black", activeforeground="skyblue")
    b2.place(x=250,y=550)

    combo = ttk.Combobox(
        state="readonly",
        values=["all", "instagram", "facebook", "twitter", "reddit", "youtube", "wikipedia"],
    )
    combo.place(x=150, y=355)
    combo.set("all")

    mainmenu2 = Menu(app)
    mainmenu2.add_command(label="About us", command=infomenu)
    app.config(menu=mainmenu2)

    app.mainloop()

root.geometry("600x400")
root.wm_maxsize(600,400)
root.wm_minsize(600,400)
root.wm_title("ZEROTWO - Login")
root.configure(background="black")

b1 = Button(root, text="Login", command=login  , activebackground="skyblue", bg="black", fg="skyblue")
b1.place(x=250,y=300)

photo = PhotoImage(file = "image.png")
root.iconphoto(False, photo)

l1 = Label(root, text="Please Log in to continue to ZEROTWO", height=1, width=40, bg="black", fg="magenta")
l1.place(x=70,y=40)
l1.config(font=("Courier", 14))

l2 = Label(root, text="Enter username:", height=1, width=15, bg="black", fg="lightblue")
l2.place(x=70,y=130)
l2.config(font=("Courier", 10))

l3 = Label(root, text="Enter password:", height=1, width=15, bg="black", fg="lightblue")
l3.place(x=70,y=190)
l3.config(font=("Courier", 10))

t1 = Entry(root, bg="black", width=23, fg="white", foreground="skyblue", insertbackground="skyblue")
t1.place(x=230, y=130)

t2 = Entry(root, bg="black", width=23, fg="white", foreground="skyblue", show="*", insertbackground="skyblue")
t2.place(x=230, y=190)



root.mainloop()
