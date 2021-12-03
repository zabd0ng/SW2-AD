import datetime
import requests
from bs4 import BeautifulSoup
from station_info import *

class GetTime:
    def __init__(self, url, station, no, direction):


        self.station = station
        self.no = no
        self.direction = direction

        self.response = requests.get(url)

        html = self.response.text
        self.soup = BeautifulSoup(html, 'html.parser')

        self.opportunity = self.soup.select_one('tr:nth-of-type(2) > td').get('rowspan')  # 배정된 열차 수 가져오기
        # print(opportunity)

        self.hour = datetime.datetime.now().hour  # - 시간만 따오기
        if self.hour == 0:
            self.hour = 24
        self.minute = datetime.datetime.now().minute  # - 분만 따오기
        # print(datetime.datetime.now().weekday()) #(0이 월요일, 6이 일요일)

        self.u_timelist = self.soup.select('tr')[2: int(self.opportunity) + 2]  # 상행 첫차부터 막차까지 뽑아오기
        self.d_timelist = self.soup.select('tr')[int(self.opportunity) + 4: -1]  # 하행 첫차부터 막차까지 뽐아오기

    def time(self):
        if self.station in circle_line_6 and self.direction == '상행':
            if self.no == '06호선':
                self.direction = '하행'

        if self.direction == '상행':  # 상행선
            min1 = 99
            min2 = 99
            res = ''
            for time in self.u_timelist:
                t = time.get_text().replace('\n', '')
                t1 = t.replace('상행(외선)', '')
                subh = int(t1[0:2]) - self.hour
                subm = int(t1[3:5]) - self.minute
                if (subh == 0 and subm >= 0) or (subh == 1 and subm > -60):
                    res = t1
                    break

            if res == '':  # 막차가 끊겼을 경우
                for time in self.u_timelist:
                    t = time.get_text().replace('\n', '')
                    t1 = t.replace('상행(외선)', '')
                    if '(급행)' in t1[5:]:
                        ex_rapid = t1.replace('(급행)', '')
                        if ex_rapid[5:] == self.station:
                            return '이번 열차는 당역에 종착하는 열차입니다.'

                        else:
                            return res

                    elif t1[5:] == self.station:  # 열차가 당역에 종차할 시
                        return '이번 열차는 당역에 종착하는 열차입니다.'

                    return t1  # 첫차 표시


            elif self.station != '성수' and self.station != '신도림':  # 2호선의 경우, 순환 형태를 띰
                if '(급행)' in res[5:]:
                    ex_rapid = res.replace('(급행)', '')
                    if ex_rapid[5:] == self.station:
                        return '이번 열차는 당역에 종착하는 열차입니다.'
                    else:
                        return res
                elif res[5:] == self.station:  # 열차가 당역에 종차할 시
                    return '이번 열차는 당역에 종착하는 열차입니다.'

                else:
                    return res

            else:
                return res

        if self.direction == '하행':  # 하행선
            res = ''
            for time in self.d_timelist:
                t = time.get_text().replace('\n', '')
                t2 = t.replace('하행(내선)', '')
                subh = int(t2[0:2]) - self.hour
                subm = int(t2[3:5]) - self.minute
                if (subh == 0 and subm >= 0) or (subh == 1 and subm > -60):
                    res = t2
                    break

            if res == '':
                for time in self.d_timelist:
                    t = time.get_text().replace('\n', '')
                    t2 = t.replace('하행(내선)', '')
                    if '(급행)' in t2[5:]:
                        ex_rapid = t2.replace('(급행)', '')
                        if ex_rapid[5:] == self.station:
                            return '이번 열차는 당역에 종착하는 열차입니다.'

                        else:
                            return res

                    elif t2[5:] == self.station:  # 열차가 당역에 종차할 시
                        return '이번 열차는 당역에 종착하는 열차입니다.'

                    return t2


            elif self.station != '성수' and self.station != '신도림':  # 2호선의 경우, 순환 형태를 띰
                if '(급행)' in res[5:]:
                    ex_rapid = res.replace('(급행)', '')
                    if ex_rapid[5:] == self.station:
                        return '이번 열차는 당역에 종착하는 열차입니다.'
                    else:
                        return res
                elif res[5:] == self.station:  # 열차가 당역에 종차할 시
                    return '이번 열차는 당역에 종착하는 열차입니다.'
                else:
                    return res

            else:
                return res
