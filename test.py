import pandas as pd
import requests
from bs4 import BeautifulSoup

station_info = pd.read_csv('station_id.csv', encoding='CP949')
station = "합정"
no = '02호선'
station_info = station_info[station_info['전철역명']==station]
station_info = station_info[station_info['호선']==no]

station_no = station_info.iloc[0]['외부코드']

url = "https://bus.go.kr/getSubway_6.jsp?statnId=1002000"+station_no+"&subwayId=1002&tabmn=5"
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
# opportunity = soup.select_one('tr > td').get('rowspan') #:nth-of-type(2)
# print(opportunity)
# uptrain = []
# downtrain = []
# arrivestationlist = soup.select('tr')[1:]   #int(opportunity)+2
timelist = soup.select('tr')[3:]            #int(opportunity)+2
for time in timelist:
    t = time.get_text().replace('\n', '')
    print(t)
