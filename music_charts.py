from urllib.request import urlopen
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#melon top100 charts address
urladdress="https://www.melon.com/chart/index.htm"

#HTTP Error 406:Not Acceptable;크롤링거부 에러
#https://www.useragentstring.com/
header = {'User-Agent':'Mozilla/5.0'} #접속 브라우저 정보 선언
modi = urllib.request.Request(urladdress, headers = header)

url = urlopen(modi)
soup = BeautifulSoup(url.read(), 'html.parser')

timeSearch=soup.find('div',{'class':'calendar_prid mt12'})
timeSearch.find('div',{'class':'time_layer'}).extract()#시간선택 태그 제거
timeSearch=list(timeSearch.stripped_strings)
print("=====================================================")
print("수집된 TOP100 차트 기준 : ",timeSearch[0],timeSearch[1])

#song=soup.findAll('div',{'class':"ellipsis rank01"}) #곡명
#artist=soup.findAll('div',{'class':'ellipsis rank02'}) #아티스트
song=soup.select(".ellipsis.rank01") #곡명
artist=soup.select(".ellipsis.rank02") #아티스트
print("=====================================================")
for i in range(len(song)):
    print(str(i+1)+"위", end=" ")
    print(":",song[i].a.text, end=" ") #곡명 출력
    print("/",artist[i].a.text) #아티스트 출력
print("=====================================================")

#next
#조회한 순위 기록 저장
#dataframe or txt