from bs4 import BeautifulSoup
from urllib import request

url = "https://m.post.naver.com/viewer/postView.nhn?volumeNo=15402547&memberNo=1580855&vType=VERTICAL"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
#texts = eval(soup.text)
print(raw_text)
