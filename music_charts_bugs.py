from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total')
soup = BeautifulSoup(url.read(), 'html.parser')

#musics = soup.find_all('p',{'class':'title'})
musics = soup.find_all('tr',{'rowtype':'track'})

dateTime = soup.find('fieldset',{'class':'filterChart'}).find('time')
dateTime = list(dateTime.stripped_strings)

print("=====================================================")
print("벅스 차트 {} {}".format(dateTime[0],dateTime[1]))
print("=====================================================")
for i in range(len(musics)):
    t=musics[i]
    music = t.find('p',{'class':'title'}).get_text().strip()
    artist = list(t.find('p',{'class':'artist'}).stripped_strings)[0] #아티스트 상세보기 관련 중복 출력
    #album = t.find('a',{'class':'album'}).get_text().strip()
    print("{}위 : {} / {}".format(i+1,music,artist))
print("=====================================================")