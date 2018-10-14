# 1. download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://dantri.com.vn"

# 1.1 open a connection 
conn = urlopen(url)

# 1.2 download raw data
raw_data = conn.read()

# 1.3 decode data
webpage_text = raw_data.decode("utf-8")
# print(len(webpage_text))
# 1.4 save text 
# w = write
# b = binary
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

# 2. extract ROI (Region Of Interest)
# 2.1 convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser") #doi text thanh html bang html.parser
ul = soup.find("ul", "ul1 ulnew") # id = "ul1 ulnew"
li_list = ul.find_all("li") #find_all: tim nhieu

#  for li in li_list:
#     print(li.prettify())
#     print("********")
news_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    title = a.string
    link = url + a["href"]
    # print(title)
    # print(link)
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    print(*news_list, sep="\n")
    


# 3. extract data

# 4. save data
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
