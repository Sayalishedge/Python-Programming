import requests  
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
response = requests.get(url)
print(response.text)


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
print(html_soup)

award_list=html_soup.find_all("tr",{"style":'background:#FAEB86'})
print(len(award_list))

first_award=award_list[0]

val=first_award.find("a",{"href":re.compile("film")}).get("href")
print(val)

data=first_award.find("a",{"href":re.compile("film")})
val=data["href"]
print(val)

newurl="https://en.wikipedia.org"+val
newresponse = requests.get(newurl)
print(newresponse.text)
newdata=BeautifulSoup(newresponse.text,"html.parser")






