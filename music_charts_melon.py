from urllib.request import urlopen
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#melon top100 charts address
urladdress="https://www.melon.com/chart/index.htm"

#HTTP Error 406:Not Acceptable;크롤링거부 에러
#https://www.useragentstring.com/
header = {'User-Agent':'Mozilla/5.0'} #접속 브라우저 정보 선언
modi = urllib.request.Request(urladdress, headers = header) #header 정보를 수정하여 406에러 해결

url = urlopen(modi)
soup = BeautifulSoup(url.read(), 'html.parser') #페이지 소스 불러오기

timeSearch=soup.find('div',{'class':'calendar_prid mt12'}) #페이지 내 표시된 조회시점 순위기준 날짜, 시간 정보 조회
timeSearch.find('div',{'class':'time_layer'}).extract() #시간선택 태그 제거
timeSearch=list(timeSearch.stripped_strings) #문자열 선후 개행문자, 여백 제거

print("=====================================================")
print("수집된 TOP100 차트 기준 : ",timeSearch[0],timeSearch[1]) #조회시점 순위기준 날짜 및 시간 출력
print("=====================================================")

song=soup.select(".ellipsis.rank01") #곡명
artist=soup.select(".ellipsis.rank02") #아티스트

for i in range(len(song)):
    print("{}위 : {} / {}".format(i+1,song[i].a.text,artist[i].a.text))
    #print(str(i+1)+"위", end=" ") #순위 출력
    #print(":",song[i].a.text, end=" ") #곡명 출력
    #print("/",artist[i].a.text) #아티스트 출력
print("=====================================================")

#next
#조회한 순위 기록 저장
#dataframe or txt