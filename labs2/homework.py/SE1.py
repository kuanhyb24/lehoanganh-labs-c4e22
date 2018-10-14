from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"

conn= urlopen(url)

raw_data = conn.read()

webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text, "html.parser")
section = soup.find("section","section chart-grid")
ul = section.find("ul")
li_list = ul.find_all("li")
list_song = []
for li in li_list:
    h3 = li.h3.a
    h4 =li.h4.a
    songs = h3.string
    artists = h4.string
    news = {
        "Songs":songs,
        "Artists": artists,
    }
    list_song.append(news)    
print(*list_song, sep="\n")
pyexcel.save_as(records=list_song, dest_file_name="itunes top songs.xlsx")