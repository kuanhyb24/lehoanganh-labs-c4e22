from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
# w = write
# b = binary
# f = open("apple.html", "wb")
# f.write(raw_data)
# f.close()
soup = BeautifulSoup(webpage_text, "html.parser")
ul = soup.find("ul")
li_list = ul.find_all
news_list = []
for li in li_list:
    a = li.a
    title = a.string
    link = url + a['href']
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    print(*news_list, sep="\n")

