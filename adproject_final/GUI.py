"""layout practice
"""

import datetime
import sys
import line, line_sat, line_holi
from get_timeline import GetTime


from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from station_info import *


class Example(QWidget):
    """simple window class"""

    def __init__(self):

        super().__init__()

        self.init_ui()
        self.qp = QPainter()
        self.setFixedSize(500, 600)

    def init_ui(self):
        label1 = QLabel("역명")
        label2 = QLabel("호선")
        label3 = QLabel("상/하행")

        self.lineedit_station = QLineEdit()
        self.combo_line = QComboBox()
        self.combo_updown = QComboBox()
        self.showtext = QLineEdit()


        self.showtext.setReadOnly(1)

        self.combo_line.addItems(lineNoList)
        self.combo_updown.addItems(["상행", "하행"])

        self.button_find = QPushButton("보기")
        self.button_find.clicked.connect(self.showResult)

        hbox1 = QHBoxLayout()

        hbox1.addWidget(label1)
        hbox1.addWidget(self.lineedit_station)
        hbox1.addWidget(label2)
        hbox1.addWidget(self.combo_line)
        hbox1.addWidget(label3)
        hbox1.addWidget(self.combo_updown)
        hbox1.addWidget(self.button_find)

        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.showtext)



        self.setLayout(vbox1)

        self.move(300, 150)
        self.setWindowTitle('지하철 도착 정보')
        self.show()


    def showResult(self):

        self.month = str(datetime.datetime.now().month)
        self.day = str(datetime.datetime.now().day)
        self.date = self.month + '.' + self.day

        self.station = self.lineedit_station.text()
        self.no = self.combo_line.currentText()
        self.direction = self.combo_updown.currentText()


        while True:
            try:
                if datetime.datetime.now().weekday() == 5:
                    Info = line_sat.Line(self.station, self.no, self.direction)
                elif datetime.datetime.now().weekday() == 6 or self.date in holiday_list:
                    Info = line_holi.Line(self.station, self.no, self.direction)
                else:
                    Info = line.Line(self.station, self.no, self.direction)

                self.update()

            except:
                return '역 정보가 틀립니다. 다시 확인해주세요'
                self.showtext.setText('역 정보가 틀립니다. 다시 확인해주세요')
                self.station = self.lineedit_station.text()
                self.no = self.combo_line.currentText()
                self.direction = self.combo_updown.currentText()

            else:
                break

        if self.station in except_stations and self.no != '05호선':
            self.showtext.setText(Info.noInfoStations())
        elif self.no == '01호선':
            url = Info.line01()
            print(url)
            Info = GetTime(url, self.station, self.no, self.direction)
            res = Info.time()
            print(res)
            self.showtext.setText(res)
            self.show_no = self.no[0:1]
        elif self.no == '05호선':
            url = Info.line05()
            print(url)
            Info = GetTime(url, self.station, self.no, self.direction)
            res = Info.time()
            print(res)
            self.showtext.setText(res)
            self.show_no = self.no[0:1]
        else:
            url = Info.lineN()
            print(url)
            Info = GetTime(url, self.station, self.no, self.direction)
            res = Info.time()
            print(res)
            self.showtext.setText(res)
            self.show_no = self.no[0:1]

    def paintEvent(self, e):
        try:
            self.station = self.lineedit_station.text()
            self.no = self.combo_line.currentText()
            self.direction = self.combo_updown.currentText()

            self.qp.begin(self)

            if self.no == "01호선":
                self.draw_Lines01(self.qp)
                self.draw_point01(self.qp)
                self.draw_direction01(self.qp)
            elif self.no == "02호선":
                self.draw_Lines02(self.qp)
                self.draw_point02(self.qp)
                self.draw_direction02(self.qp)
            elif self.no == "03호선":
                self.draw_Lines03(self.qp)
                self.draw_point03(self.qp)
                self.draw_direction03(self.qp)
            elif self.no == "04호선":
                self.draw_Lines04(self.qp)
                self.draw_point04(self.qp)
                self.draw_direction04(self.qp)
            elif self.no == "05호선":
                self.draw_Lines05(self.qp)
                self.draw_point05(self.qp)
                self.draw_direction05(self.qp)
            elif self.no == "06호선":
                self.draw_Lines06(self.qp)
                self.draw_point06(self.qp)
                self.draw_direction06(self.qp)
            elif self.no == "07호선":
                self.draw_Lines07(self.qp)
                self.draw_point07(self.qp)
                self.draw_direction07(self.qp)
            elif self.no == "08호선":
                self.draw_Lines08(self.qp)
                self.draw_point08(self.qp)
                self.draw_direction08(self.qp)
            else:
                self.draw_Lines09(self.qp)
                self.draw_point09(self.qp)
                self.draw_direction09(self.qp)

            self.qp.end()
        except:
            pass

    def draw_Lines01(self, qp):  # 1호선
        darkBlue = Qt.darkBlue
        linePen = QPen(darkBlue, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 4 * x, 44 * x, 4 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 12 * x, 44 * x, 12 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 3행
        qp.drawLine(6 * x, 25 * x, 42 * x, 25 * x)  # 4행    # 가로 길이 = 36 * x
        qp.drawLine(6 * x, 32 * x, 40 * x, 32 * x)  # 5행    # 가로 길이 = 34 * x
        qp.drawLine(6 * x, 38 * x, 40 * x, 38 * x)  # 6행
        qp.drawLine(6 * x, 46 * x, 30 * x, 46 * x)  # 7행    # 가로 길이 = 24 * x
        qp.drawLine(6 * x, 4 * x, 6 * x, 12 * x)  # 1열    # 세로 길이 = 8 * x
        qp.drawLine(44 * x, 12 * x, 44 * x, 20 * x)  # 2열    # 세로 길이 = 8 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 32 * x)  # 3열    # 세로 길이 = 12 * x
        qp.drawLine(42 * x, 25 * x, 42 * x, 46 * x)  # 4열    # 세로 길이 = 21 * x
        qp.drawLine(40 * x, 32 * x, 40 * x, 38 * x)  # 5열    # 세로 길이 = 6 * x
        qp.drawLine(6 * x, 38 * x, 6 * x, 46 * x)  # 6열    # 세로 길이 = 8 * x
        qp.drawLine(12 * x, 32 * x, 15 * x, 35 * x)  # 광명역
        qp.drawLine(33 * x, 38 * x, 36 * x, 41 * x)  # 서동탄역


    def draw_point01(self, qp):  # 현재 위치를 포인트로 표시
        qp.setBrush(QColor(255, 85, 105))  # RGB Red
        # qp.drawRect(400, 35, 12, 12)      # x, y, 크기

        line1 = ['도봉', '도봉산', '망월사', '회룡', '의정부', '가능', '녹양', '양주', '덕계', '덕정', '지행', '동두천중앙', '보산', '동두천', '소요산',
                 '방학', '창동', '녹천', '월계', '광운대', '석계', '신이문', '외대앞', '회기', '청량리', '제기동', '신설동', '동묘앞', '동대문',
                 '신도림', '영등포', '신길', '대방', '노량진', '용산', '남영', '서울역', '시청', '종각', '종로3가', '종로5가',
                 '구로', '구일', '개봉', '오류동', '온수', '역곡', '소사', '부천', '중동', '송내', '부개', '부평', '백운', '동암', '간석',
                 '가산디지털단지', '독산', '금천구청', '석수', '관악', '안양', '명학', '금정', '군포', '당정', '의왕', '성균관대', '화서',
                 '직산', '성환', '평택', '지제', '서정리', '송탄', '진위', '오산', '오산대', '세마', '병점', '세류', '수원',
                 '두정', '천안', '봉명', '쌍용(나사렛대)', '아산', '배방', '온양온천', '신창',
                 '주안', '도화', '제물포', '도원', '동인천', '인천',
                 '광명', '서동탄']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line1)):
            if now_station == line1[i]:
                now_stationNum = i  # line2, 즉 역들 리스트 안에 now_station이 있을 경우 해당 인덱스를 now_stationNum에 저장
                # 리스트 내에 없을 경우, now_stationNum은 그대로 -1이고 노선도에 표시가 안 됨

        # qp.drawRect(x좌표, y좌표, 포인트의 크기(x, y) => 포인트 생성
        # int() 넣는 이유: 실수형으로 넣을 경우 경고문이 떠서
        if 0 <= now_stationNum < 15:
            qp.drawRect(int(7 + 2.5 * now_stationNum) * x, int(3.5 * x), 12, 12)
        elif 15 <= now_stationNum < 29:
            qp.drawRect(int(7 + 2.5 * (now_stationNum - 15)) * x, int(11.5 * x), 12, 12)
        elif 29 <= now_stationNum < 41:
            qp.drawRect(int(8 + 3 * (now_stationNum - 29)) * x, int(19.5 * x), 12, 12)
        elif 41 <= now_stationNum < 56:
            qp.drawRect(int((5.4 + 2.45 * (now_stationNum - 41)) * x), int(24.5 * x), 12, 12)
        elif 56 <= now_stationNum < 69:
            if now_stationNum == 58:
                qp.drawRect(12 * x, int(31.5 * x), 12, 12)
            else:
                qp.drawRect(int((6.8 + 2.45 * (now_stationNum - 56)) * x), int(31.5 * x), 12, 12)
        elif 69 <= now_stationNum < 82:
            if now_stationNum == 79:
                qp.drawRect(33 * x, int(37.5 * x), 12, 12)
            else:
                qp.drawRect(int((7.5 + 2.54 * (now_stationNum - 69)) * x), int(37.5 * x), 12, 12)
        elif 82 <= now_stationNum < 90:
            qp.drawRect(int((7.5 + 2.8 * (now_stationNum - 82)) * x), int(45.5 * x), 12, 12)
        elif 90 <= now_stationNum < 96:
            qp.drawRect(int(41.5 * x), int((27 + 3.2 * (now_stationNum - 90)) * x), 12, 12)
        elif now_stationNum == 96:
            qp.drawRect(14 * x, 34 * x, 12, 12)
        elif now_stationNum == 97:
            qp.drawRect(35 * x, 40 * x, 12, 12)


    def draw_direction01(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 14 or now_stationNum == 89 or now_stationNum == 95 or now_stationNum == 96 or now_stationNum == 97:
            pass
        elif 0 <= now_stationNum < 14:
            if now_direction == '상행':
                qp.drawText(int(8 + 2.5 * now_stationNum) * x, int(2.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(8 + 2.5 * now_stationNum) * x, int(2.5 * x), '◀◀◀')
        elif 15 <= now_stationNum < 29:
            if now_direction == '상행':
                qp.drawText(int(8 + 2.5 * (now_stationNum - 15)) * x, int(10.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(8 + 2.5 * (now_stationNum - 15)) * x, int(10.5 * x), '▶▶▶')
        elif 29 <= now_stationNum < 41:
            if now_direction == '상행':
                qp.drawText(int(8 + 2.5 * (now_stationNum - 29)) * x, int(18.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(8 + 2.5 * (now_stationNum - 29)) * x, int(18.5 * x), '◀◀◀')
        elif 41 <= now_stationNum < 56:
            if now_direction == '상행':
                qp.drawText(int(7.5 + 2 * (now_stationNum - 41)) * x, int(23.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7.5 + 2 * (now_stationNum - 41)) * x, int(23.5 * x), '▶▶▶')
        elif 56 <= now_stationNum < 69:
            if now_direction == '상행':
                qp.drawText(int(7.5 + 2.3 * (now_stationNum - 56)) * x, int(30.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7.5 + 2.3 * (now_stationNum - 56)) * x, int(30.5 * x), '▶▶▶')
        elif 69 <= now_stationNum < 82:
            if now_direction == '상행':
                qp.drawText(int(7.5 + 2.2 * (now_stationNum - 69)) * x, int(36.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(7.5 + 2.2 * (now_stationNum - 69)) * x, int(36.5 * x), '◀◀◀')
        elif 82 <= now_stationNum < 89:
            if now_direction == '상행':
                qp.drawText(int(7.5 + 2.3 * (now_stationNum - 82)) * x, int(44.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7.5 + 2.3 * (now_stationNum - 82)) * x, int(44.5 * x), '▶▶▶')
        elif 90 <= now_stationNum < 96:
            if now_direction == '상행':
                qp.drawText(int(43.5 * x), int((28 + 3.2 * (now_stationNum - 90)) * x), '▲')
            elif now_direction == '하행':
                qp.drawText(int(43.5 * x), int((28 + 3.2 * (now_stationNum - 90)) * x), '▼')


    ###########################################################################################


    # 2호선
    def draw_Lines02(self, qp):
        darkGreen = Qt.darkGreen
        linePen = QPen(darkGreen, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(7 * x, 13 * x, 43 * x, 13 * x)  # x1, y1, x2, y2  # 위 가로 라인
        qp.drawLine(7 * x, 37 * x, 43 * x, 37 * x)  # 아래 가로 라인    # 가로 길이 = 36 * x
        qp.drawLine(7 * x, 13 * x, 7 * x, 44 * x)  # 왼쪽 라인        # 세로 길이(왼) = 31 * x
        qp.drawLine(43 * x, 4 * x, 43 * x, 37 * x)  # 오른쪽 라인      # 세로 길이(오) = 33 * x
        qp.drawLine(43 * x, 4 * x, 30 * x, 4 * x)  # 위쪽 짧은 가로   # 짧은 가로 길이 = 13 * x
        qp.drawLine(7 * x, 44 * x, 20 * x, 44 * x)  # 아래쪽 짧은 가로


    def draw_point02(self, qp):
        qp.setBrush(QColor(255, 85, 105))  # RGB Red

        line2 = ['신설동', '용두', '신답',
                 '충정로', '시청', '을지로입구', '을지로3가', '을지로4가', '동대문역사문화공원', '신당', '상왕십리', '왕십리', '한양대', '뚝섬',
                 '아현', '이대', '신촌', '홍대입구', '합정', '당산', '영등포구청', '문래',
                 '용답', '성수', '건대입구', '구의', '강변', '잠실나루', '잠실', '잠실새내', '종합운동장', '삼성', '선릉',
                 '신도림', '대림', '구로디지털단지', '신대방', '신림', '봉천', '서울대입구', '낙성대', '사당', '방배', '서초', '교대', '강남', '역삼',
                 '도림천',
                 '양천구청', '신정네거리', '까치산']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line2)):
            if now_station == line2[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 3:
            qp.drawRect((32 + 4 * now_stationNum) * x, int(3.5 * x), 12, 12)
        elif 3 <= now_stationNum < 14:
            qp.drawRect(int(8 + 3.2 * (now_stationNum - 3)) * x, int(12.5 * x), 12, 12)
        elif 14 <= now_stationNum < 22:
            qp.drawRect(int(6.5 * x), int(14 + 2.97 * (now_stationNum - 14)) * x, 12, 12)
        elif 22 <= now_stationNum < 33:
            qp.drawRect(int(42.4 * x), int(10 + (2.5 * (now_stationNum - 22))) * x, 12, 12)
        elif 33 <= now_stationNum < 47:
            qp.drawRect(int(7 + 2.65 * (now_stationNum - 33)) * x, int(36.5 * x), 12, 12)
        elif now_stationNum == 47:
            qp.drawRect(int(6.5 * x), 40 * x, 12, 12)
        elif 48 <= now_stationNum <= 50:
            qp.drawRect((9 + 3 * (now_stationNum - 48)) * x, int(43.5 * x), 12, 12)


    def draw_direction02(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(32 * x, int(2.5 * x), '▶▶▶')
            pass
        elif 0 < now_stationNum < 3:
            if now_direction == '상행':
                qp.drawText(int(32 + 2.5 * now_stationNum) * x, int(2.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(32 + 2.5 * now_stationNum) * x, int(2.5 * x), '▶▶▶')
        elif 3 <= now_stationNum < 14:
            if now_direction == '상행':
                qp.drawText(int(5.8 + 3.2 * (now_stationNum - 3)) * x, int(11.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(5.8 + 3.2 * (now_stationNum - 3)) * x, int(11.5 * x), '▶▶▶')
        elif 14 <= now_stationNum < 22:
            if now_direction == '상행':
                qp.drawText(int(3.5 * x), int(15 + 2.97 * (now_stationNum - 14)) * x, '▼')
            elif now_direction == '하행':
                qp.drawText(int(3.5 * x), int(15 + 2.97 * (now_stationNum - 14)) * x, '▲')
        elif 22 <= now_stationNum < 33:
            if now_direction == '상행':
                qp.drawText(int(44.5 * x), int(11 + 2.5 * (now_stationNum - 22)) * x, '▲')
            elif now_direction == '하행':
                qp.drawText(int(44.5 * x), int(11 + 2.5 * (now_stationNum - 22)) * x, '▼')
        elif 33 <= now_stationNum < 47:
            if now_direction == '상행':
                qp.drawText(int((7.5 + 2.28 * (now_stationNum - 33)) * x), int(35.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int((7.5 + 2.28 * (now_stationNum - 33)) * x), int(35.5 * x), '◀◀◀')
        elif now_stationNum == 47:
            if now_direction == '상행':
                qp.drawText(int(3.5 * x), 41 * x, '▲')
            elif now_direction == '하행':
                qp.drawText(int(3.5 * x), 41 * x, '▼')
        elif 48 <= now_stationNum < 50:
            if now_direction == '상행':
                qp.drawText((8 + 3 * (now_stationNum - 48)) * x, int(42.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText((8 + 3 * (now_stationNum - 48)) * x, int(42.5 * x), '▶▶▶')
        elif now_stationNum == 50:
            if now_direction == '상행':
                qp.drawText(14 * x, int(42.5 * x), '◀◀◀')
            elif now_direction == '하행':
                pass


    ###########################################################################################


    # 3호선
    def draw_Lines03(self, qp):  # 3호선
        darkRed = Qt.darkRed
        linePen = QPen(darkRed, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 10 * x, 44 * x, 10 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 30 * x, 44 * x, 30 * x)  # 3행
        qp.drawLine(6 * x, 40 * x, 44 * x, 40 * x)  # 4행
        qp.drawLine(44 * x, 10 * x, 44 * x, 20 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 30 * x)  # 2열
        qp.drawLine(44 * x, 30 * x, 44 * x, 40 * x)  # 3열


    def draw_point03(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line3 = ['대화', '주엽', '정발산', '마두', '백석', '대곡', '화정', '원당', '원흥', '삼송', '지축', '구파발',
                 '충무로', '을지로3가', '종로3가', '안국', '경복궁', '독립문', '무악재', '홍제', '녹번', '불광', '연신내',
                 '동대입구', '약수', '금호', '옥수', '압구정', '신사', '잠원', '고속터미널', '교대', '남부터미널', '양재',
                 '오금', '경찰병원', '가락시장', '수서', '일원', '대청', '학여울', '대치', '도곡', '매봉']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line3)):
            if now_station == line3[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 12:
            qp.drawRect(int(8 + 2.95 * now_stationNum) * x, int(9.5 * x), 12, 12)
        elif 12 <= now_stationNum < 23:
            qp.drawRect(int(8 + 3.25 * (now_stationNum - 12)) * x, int(19.5 * x), 12, 12)
        elif 23 <= now_stationNum < 34:
            qp.drawRect(int(8 + 3.25 * (now_stationNum - 23)) * x, int(29.5 * x), 12, 12)
        elif 34 <= now_stationNum <= 43:
            qp.drawRect(int(8 + 3.55 * (now_stationNum - 34)) * x, int(39.5 * x), 12, 12)


    def draw_direction03(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(6 * x, int(8.5 * x), '▶▶▶')
        elif 0 < now_stationNum < 12:
            if now_direction == '상행':
                qp.drawText(int(6 + 2.9 * now_stationNum) * x, int(8.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(6 + 2.9 * now_stationNum) * x, int(8.5 * x), '▶▶▶')
        elif 12 <= now_stationNum < 23:
            if now_direction == '상행':
                qp.drawText(int(6.1 + 3.2 * (now_stationNum - 12)) * x, int(18.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6.1 + 3.2 * (now_stationNum - 12)) * x, int(18.5 * x), '◀◀◀')
        elif 23 <= now_stationNum < 34:
            if now_direction == '상행':
                qp.drawText(int(7 + 3.19 * (now_stationNum - 23)) * x, int(28.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 3.19 * (now_stationNum - 23)) * x, int(28.5 * x), '▶▶▶')
        elif now_stationNum == 34:
            if now_direction == '상행':
                qp.drawText(6 * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 35 <= now_stationNum <= 43:
            if now_direction == '상행':
                qp.drawText(int(8 + 3.5 * (now_stationNum - 35)) * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(8 + 3.5 * (now_stationNum - 35)) * x, int(38.5 * x), '◀◀◀')


    ###########################################################################################


    # 4호선
    def draw_Lines04(self, qp):
        darkCyan = Qt.darkCyan
        linePen = QPen(darkCyan, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 10 * x, 44 * x, 10 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 30 * x, 44 * x, 30 * x)  # 3행
        qp.drawLine(6 * x, 40 * x, 44 * x, 40 * x)  # 4행
        qp.drawLine(44 * x, 10 * x, 44 * x, 20 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 30 * x)  # 2열
        qp.drawLine(44 * x, 30 * x, 44 * x, 40 * x)  # 3열


    def draw_point04(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line4 = ['당고개', '상계', '노원', '창동', '쌍문', '수유', '미아', '미아사거리', '길음', '성신여대입구', '한성대입구',
                 '동작', '이촌', '신용산', '삼각지', '숙대입구', '서울역', '회현', '명동', '충무로', '동대문역사문화공원', '동대문', '혜화',
                 '총신대입구', '사당', '남태령', '선바위', '경마공원', '대공원', '과천', '정부과천청사', '인덕원', '평촌', '범계', '금정', '산본',
                 '오이도', '정왕', '신길온천', '안산', '초지', '고잔', '중앙', '한대앞', '상록수', '반월', '대야미', '수리산']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line4)):
            if now_station == line4[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 11:
            qp.drawRect(int(8 + 3.25 * now_stationNum) * x, int(9.5 * x), 12, 12)
        elif 11 <= now_stationNum < 23:
            qp.drawRect(int(8 + 2.95 * (now_stationNum - 11)) * x, int(19.5 * x), 12, 12)
        elif 23 <= now_stationNum < 36:
            qp.drawRect(int(8 + 2.8 * (now_stationNum - 23)) * x, int(29.5 * x), 12, 12)
        elif 36 <= now_stationNum <= 48:
            qp.drawRect(int(8 + 2.95 * (now_stationNum - 36)) * x, int(39.5 * x), 12, 12)


    def draw_direction04(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(6 * x, int(8.5 * x), '▶▶▶')
        elif 0 < now_stationNum < 11:
            if now_direction == '상행':
                qp.drawText(int(6 + 3.25 * now_stationNum) * x, int(8.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(6 + 3.25 * now_stationNum) * x, int(8.5 * x), '▶▶▶')
        elif 11 <= now_stationNum < 23:
            if now_direction == '상행':
                qp.drawText(int(6.1 + 2.9 * (now_stationNum - 11)) * x, int(18.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6.1 + 2.9 * (now_stationNum - 11)) * x, int(18.5 * x), '◀◀◀')
        elif 23 <= now_stationNum < 36:
            if now_direction == '상행':
                qp.drawText(int(7 + 2.7 * (now_stationNum - 23)) * x, int(28.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 2.7 * (now_stationNum - 23)) * x, int(28.5 * x), '▶▶▶')
        elif now_stationNum == 36:
            if now_direction == '상행':
                qp.drawText(6 * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 37 <= now_stationNum <= 48:
            if now_direction == '상행':
                qp.drawText(int(8 + 2.95 * (now_stationNum - 37)) * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(8 + 2.95 * (now_stationNum - 37)) * x, int(38.5 * x), '◀◀◀')


    ###########################################################################################


    # 5호선
    def draw_Lines05(self, qp):
        darkMagenta = Qt.darkMagenta
        linePen = QPen(darkMagenta, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10  # 크기조정하면 위치가 이상해짐.....수정필요
        qp.drawLine(6 * x, 10 * x, 44 * x, 10 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 30 * x, 44 * x, 30 * x)  # 3행
        qp.drawLine(37 * x, 40 * x, 44 * x, 40 * x)  # 4행    # 4행 길이 7 * x
        qp.drawLine(44 * x, 10 * x, 44 * x, 20 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 30 * x)  # 2열
        qp.drawLine(44 * x, 30 * x, 44 * x, 40 * x)  # 3열
        qp.drawLine(37 * x, 36 * x, 37 * x, 44 * x)  # 갈림길 세로 길이 = 8 * x
        qp.drawLine(37 * x, 36 * x, 15 * x, 36 * x)  # 갈림길 1행 길이 = 22 * x
        qp.drawLine(37 * x, 44 * x, 10 * x, 44 * x)  # 갈림길 2행 길이 = 27 * x


    def draw_point05(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line5 = ['방화', '개화산', '김포공항', '송정', '마곡', '발산', '우장산', '화곡', '까치산', '신정', '목동', '오목교',
                 '종로3가', '광화문', '서대문', '충정로', '애오개', '공덕', '마포', '여의나루', '여의도', '신길', '영등포시장', '영등포구청', '양평',
                 '을지로4가', '동대문역사문화공원', '청구', '신금호', '행당', '왕십리', '마장', '답십리', '장한평', '군자', '아차산', '광나루',
                 '강동', '천호',
                 '상일동', '고덕', '명일', '굽은다리', '길동',
                 '마천', '거여', '개롱', '오금', '방이', '올림픽공원', '둔촌동']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line5)):
            if now_station == line5[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 12:
            qp.drawRect(int(8 + 2.95 * now_stationNum) * x, int(9.5 * x), 12, 12)
        elif 12 <= now_stationNum < 25:
            qp.drawRect(int(8 + 2.8 * (now_stationNum - 12)) * x, int(19.5 * x), 12, 12)
        elif 25 <= now_stationNum < 37:
            qp.drawRect(int(8 + 2.95 * (now_stationNum - 25)) * x, int(29.5 * x), 12, 12)
        elif 37 <= now_stationNum < 39:
            qp.drawRect(int((36.5 + 3.4 * (now_stationNum - 37)) * x), int(39.5 * x), 12, 12)
        elif 39 <= now_stationNum < 44:
            qp.drawRect(int((18 + 3.8 * (now_stationNum - 39)) * x), int(35.5 * x), 12, 12)
        elif 44 <= now_stationNum < 51:
            qp.drawRect(int((12 + 3.5 * (now_stationNum - 44)) * x), int(43.5 * x), 12, 12)


    def draw_direction05(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(6 * x, int(8.5 * x), '▶▶▶')
        elif 0 < now_stationNum < 12:
            if now_direction == '상행':
                qp.drawText(int(5 + 3 * now_stationNum) * x, int(8.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(5 + 3 * now_stationNum) * x, int(8.5 * x), '▶▶▶')
        elif 12 <= now_stationNum < 25:
            if now_direction == '상행':
                qp.drawText(int(6 + 2.6 * (now_stationNum - 12)) * x, int(18.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6 + 2.6 * (now_stationNum - 12)) * x, int(18.5 * x), '◀◀◀')
        elif 25 <= now_stationNum < 37:
            if now_direction == '상행':
                qp.drawText(int(7 + 2.9 * (now_stationNum - 25)) * x, int(28.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 2.9 * (now_stationNum - 25)) * x, int(28.5 * x), '▶▶▶')
        elif 37 <= now_stationNum < 39:
            if now_direction == '상행':
                qp.drawText(int(37.7 * x), int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(37.7 * x), int(38.5 * x), '◀◀◀')
        elif now_stationNum == 39:
            if now_direction == '상행':
                qp.drawText(16 * x, int(34.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 40 <= now_stationNum < 44:
            if now_direction == '상행':
                qp.drawText(int(20 + 3.8 * (now_stationNum - 40)) * x, int(34.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(20 + 3.8 * (now_stationNum - 40)) * x, int(34.5 * x), '◀◀◀')
        elif now_stationNum == 44:
            if now_direction == '상행':
                qp.drawText(10 * x, int(42.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 45 <= now_stationNum < 51:
            if now_direction == '상행':
                qp.drawText(int(13 + 3.5 * (now_stationNum - 45)) * x, int(42.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(13 + 3.5 * (now_stationNum - 45)) * x, int(42.5 * x), '◀◀◀')


    ###########################################################################################


    # 6호선 - 색상 부족
    def draw_Lines06(self, qp):
        lightGray = Qt.lightGray
        linePen = QPen(lightGray, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(18 * x, 10 * x, 44 * x, 10 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 2행    # 1행 길이 = 26 * x
        qp.drawLine(6 * x, 30 * x, 44 * x, 30 * x)  # 3행    # 가로 길이 = 38 * x
        qp.drawLine(25 * x, 40 * x, 44 * x, 40 * x)  # 4행    # 4행 길이 = 19 * x
        qp.drawLine(44 * x, 10 * x, 44 * x, 20 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 30 * x)  # 2열
        qp.drawLine(44 * x, 30 * x, 44 * x, 40 * x)  # 3열
        qp.drawLine(7 * x, 6 * x, 18 * x, 6 * x)  # 순환지점 1행
        qp.drawLine(7 * x, 14 * x, 18 * x, 14 * x)  # 순환지점 2행
        qp.drawLine(7 * x, 6 * x, 7 * x, 14 * x)  # 순환지점 왼쪽
        qp.drawLine(18 * x, 6 * x, 18 * x, 14 * x)  # 순환지점 오른쪽


    def draw_point06(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line6 = ['독바위', '응암', '새절', '증산', '디지털미디어시티', '월드컵경기장', '마포구청', '망원',
                 '버티고개', '한강진', '이태원', '녹사평', '삼각지', '효창공원앞', '공덕', '대흥', '광흥창', '상수', '합정',
                 '약수', '청구', '신당', '동묘앞', '창신', '보문', '안암', '고려대', '월곡', '상월곡', '돌곶이',
                 '신내', '봉화산', '화랑대', '태릉입구', '석계',
                 '불광', '역촌',
                 '연신내', '구산']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line6)):
            if now_station == line6[i]:
                now_stationNum = i

        if now_stationNum == 0:
            qp.drawRect(int(6.45 * x), int(9.5 * x), 12, 12)
        elif 1 <= now_stationNum < 8:
            qp.drawRect(int(20 + 2.95 * now_stationNum) * x, int(9.5 * x), 12, 12)
        elif 8 <= now_stationNum < 19:
            qp.drawRect(int(8 + 3.28 * (now_stationNum - 8)) * x, int(19.5 * x), 12, 12)
        elif 19 <= now_stationNum < 30:
            qp.drawRect(int(8 + 3.28 * (now_stationNum - 19)) * x, int(29.5 * x), 12, 12)
        elif 30 <= now_stationNum < 35:
            qp.drawRect(int((28 + 3.1 * (now_stationNum - 30)) * x), int(39.5 * x), 12, 12)
        elif 35 <= now_stationNum < 37:
            qp.drawRect(int((10 + 4 * (now_stationNum - 35)) * x), int(5.5 * x), 12, 12)
        elif 37 <= now_stationNum < 39:
            qp.drawRect(int((10 + 4 * (now_stationNum - 37)) * x), int(13.5 * x), 12, 12)


    def draw_direction06(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            pass
        elif 1 <= now_stationNum < 8:
            if now_direction == '상행':
                qp.drawText(int(16 + 3 * now_stationNum) * x, int(8.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(16 + 3 * now_stationNum) * x, int(8.5 * x), '▶▶▶')
        elif 8 <= now_stationNum < 19:
            if now_direction == '상행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 8)) * x, int(18.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 8)) * x, int(18.5 * x), '◀◀◀')
        elif 19 <= now_stationNum < 30:
            if now_direction == '상행':
                qp.drawText(int(7 + 3.1 * (now_stationNum - 19)) * x, int(28.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 3.1 * (now_stationNum - 19)) * x, int(28.5 * x), '▶▶▶')
        elif now_stationNum == 30:
            if now_direction == '상행':
                qp.drawText(27 * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 31 <= now_stationNum < 35:
            if now_direction == '상행':
                qp.drawText(int(26 + 2.9 * (now_stationNum - 30)) * x, int(38.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(26 + 2.9 * (now_stationNum - 30)) * x, int(38.5 * x), '◀◀◀')
        elif 35 <= now_stationNum < 39:
            pass


    ###########################################################################################


    # 7호선
    def draw_Lines07(self, qp):
        darkYellow = Qt.darkYellow
        linePen = QPen(darkYellow, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 5 * x, 44 * x, 5 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 15 * x, 44 * x, 15 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 25 * x, 44 * x, 25 * x)  # 3행
        qp.drawLine(6 * x, 35 * x, 44 * x, 35 * x)  # 4행
        qp.drawLine(6 * x, 45 * x, 30 * x, 45 * x)  # 5행    # 5행 길이 = 24 * x
        qp.drawLine(44 * x, 5 * x, 44 * x, 15 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 15 * x, 6 * x, 25 * x)  # 2열
        qp.drawLine(44 * x, 25 * x, 44 * x, 35 * x)  # 3열
        qp.drawLine(6 * x, 35 * x, 6 * x, 45 * x)  # 4열


    def draw_point07(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line7 = ['장암', '도봉산', '수락산', '마들', '노원', '중계', '하계', '공릉', '태릉입구', '먹골', '중화', '상봉', '면목',
                 '논현', '학동', '강남구청', '청담', '뚝섬유원지', '건대입구', '어린이대공원', '군자', '중곡', '용마산', '사가정',
                 '반포', '고속터미널', '내방', '총신대입구(이수)', '남성', '숭실대입구', '상도', '장승배기', '신대방삼거리', '보라매', '신풍',
                 '신중동', '춘의', '부천종합운동장', '까치울', '온수', '천왕', '광명사거리', '철산', '가산디지털단지', '남구로', '대림',
                 '부천시청', '상동', '삼산체육관', '굴포천', '부평구청']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line7)):
            if now_station == line7[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 13:
            qp.drawRect(int(8 + 2.83 * now_stationNum) * x, int(4.5 * x), 12, 12)
        elif 13 <= now_stationNum < 24:
            qp.drawRect(int(8 + 3.3 * (now_stationNum - 13)) * x, int(14.5 * x), 12, 12)
        elif 24 <= now_stationNum < 35:
            qp.drawRect(int(8 + 3.3 * (now_stationNum - 24)) * x, int(24.5 * x), 12, 12)
        elif 35 <= now_stationNum < 46:
            qp.drawRect(int(8 + 3.3 * (now_stationNum - 35)) * x, int(34.5 * x), 12, 12)
        elif 46 <= now_stationNum < 51:
            qp.drawRect(int(8 + 4.2 * (now_stationNum - 46)) * x, int(44.5 * x), 12, 12)


    def draw_direction07(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(6 * x, int(3.5 * x), '▶▶▶')
        elif 1 <= now_stationNum < 13:
            if now_direction == '상행':
                qp.drawText(int(4 + 2.9 * now_stationNum) * x, int(3.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(4 + 2.9 * now_stationNum) * x, int(3.5 * x), '▶▶▶')
        elif 13 <= now_stationNum < 24:
            if now_direction == '상행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 13)) * x, int(13.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 13)) * x, int(13.5 * x), '◀◀◀')
        elif 24 <= now_stationNum < 35:
            if now_direction == '상행':
                qp.drawText(int(7 + 3.1 * (now_stationNum - 24)) * x, int(23.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 3.1 * (now_stationNum - 24)) * x, int(23.5 * x), '▶▶▶')
        elif 35 <= now_stationNum < 46:
            if now_direction == '상행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 35)) * x, int(33.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6 + 3.1 * (now_stationNum - 35)) * x, int(33.5 * x), '◀◀◀')
        elif 46 <= now_stationNum < 50:
            if now_direction == '상행':
                qp.drawText(int(7 + 3.7 * (now_stationNum - 46)) * x, int(43.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(7 + 3.7 * (now_stationNum - 46)) * x, int(43.5 * x), '▶▶▶')
        elif now_stationNum == 50:
            if now_direction == '상행':
                qp.drawText(22 * x, int(43.5 * x), '◀◀◀')
            elif now_direction == '하행':
                pass


    ###########################################################################################


    # 8호선
    def draw_Lines08(self, qp):  # 9호선
        red = Qt.red
        linePen = QPen(red, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 15 * x, 44 * x, 15 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 25 * x, 44 * x, 25 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 35 * x, 44 * x, 35 * x)  # 3행
        qp.drawLine(44 * x, 15 * x, 44 * x, 25 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 25 * x, 6 * x, 35 * x)  # 2열


    def draw_point08(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line8 = ['암사', '천호', '강동구청', '몽촌토성', '잠실', '석촌',
                 '산성', '복정', '장지', '문정', '가락시장', '송파',
                 '남한산성입구', '단대오거리', '신흥', '수진', '모란']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line8)):
            if now_station == line8[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 6:
            qp.drawRect(int(10 + 6 * now_stationNum) * x, int(14.5 * x), 12, 12)
        elif 6 <= now_stationNum < 12:
            qp.drawRect(int(10 + 6 * (now_stationNum - 6)) * x, int(24.5 * x), 12, 12)
        elif 12 <= now_stationNum <= 16:
            qp.drawRect(int(11 + 7 * (now_stationNum - 12)) * x, int(34.5 * x), 12, 12)


    def draw_direction08(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(7 * x, int(13.5 * x), '▶▶▶')
        elif 1 <= now_stationNum < 6:
            if now_direction == '상행':
                qp.drawText(int(11 + 5.5 * now_stationNum) * x, int(13.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(11 + 5.5 * now_stationNum) * x, int(13.5 * x), '▶▶▶')
        elif 6 <= now_stationNum < 12:
            if now_direction == '상행':
                qp.drawText(int(8 + 5.9 * (now_stationNum - 6)) * x, int(23.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(8 + 5.9 * (now_stationNum - 6)) * x, int(23.5 * x), '◀◀◀')
        elif 12 <= now_stationNum < 16:
            if now_direction == '상행':
                qp.drawText(int(8.5 + 7.2 * (now_stationNum - 12)) * x, int(33.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(8.5 + 7.2 * (now_stationNum - 12)) * x, int(33.5 * x), '▶▶▶')
        elif now_stationNum == 16:
            if now_direction == '상행':
                qp.drawText(37 * x, int(33.5 * x), '◀◀◀')
            elif now_direction == '하행':
                pass


    ###########################################################################################


    # 9호선
    def draw_Lines09(self, qp):
        darkGray = Qt.darkGray
        linePen = QPen(darkGray, 3.5, Qt.SolidLine)
        qp.setPen(linePen)

        global x
        x = 10
        qp.drawLine(6 * x, 10 * x, 44 * x, 10 * x)  # x1, y1, x2, y2  # 1행
        qp.drawLine(6 * x, 20 * x, 44 * x, 20 * x)  # 2행    # 가로 길이 = 38 * x
        qp.drawLine(6 * x, 30 * x, 44 * x, 30 * x)  # 3행
        qp.drawLine(6 * x, 40 * x, 44 * x, 40 * x)  # 4행
        qp.drawLine(44 * x, 10 * x, 44 * x, 20 * x)  # 1열    # 세로 길이 = 10 * x
        qp.drawLine(6 * x, 20 * x, 6 * x, 30 * x)  # 2열
        qp.drawLine(44 * x, 30 * x, 44 * x, 40 * x)  # 3열


    def draw_point09(self, qp):
        qp.setBrush(QColor(255, 85, 105))

        line9 = ['개화', '김포공항', '공항시장', '신방화', '마곡나루', '양천향교', '가양', '증미', '등촌', '염창',
                 '동작', '흑석', '노들', '노량진', '샛강', '여의도', '국회의사당', '당산', '선유도', '신목동',
                 '구반포', '신반포', '고속터미널', '사평', '신논현', '언주', '선정릉', '삼성중앙', '봉은사', '종합운동장',
                 '중앙보훈병원', '둔촌오륜', '올림픽공원', '한성백제', '송파나루', '석촌', '석촌고분', '삼전']

        global now_station
        global now_stationNum
        now_station = self.lineedit_station.text()
        now_stationNum = -1
        for i in range(len(line9)):
            if now_station == line9[i]:
                now_stationNum = i

        if 0 <= now_stationNum < 10:
            qp.drawRect(int(8 + 3.7 * now_stationNum) * x, int(9.5 * x), 12, 12)
        elif 10 <= now_stationNum < 20:
            qp.drawRect(int(8 + 3.7 * (now_stationNum - 10)) * x, int(19.5 * x), 12, 12)
        elif 20 <= now_stationNum < 30:
            qp.drawRect(int(8 + 3.7 * (now_stationNum - 20)) * x, int(29.5 * x), 12, 12)
        elif 30 <= now_stationNum < 38:
            qp.drawRect(int(10 + 4 * (now_stationNum - 30)) * x, int(39.5 * x), 12, 12)


    def draw_direction09(self, qp):
        now_direction = self.combo_updown.currentText()
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('맑은 고딕', 14))
        if now_direction == '상행' or now_direction == '하행':
            qp.drawText(x, int(48.8 * x), '방향: ' + now_direction + ', 현재 역: ' + now_station)

        if now_stationNum == 0:
            if now_direction == '상행':
                qp.drawText(6 * x, int(8.5 * x), '▶▶▶')
            elif now_direction == '하행':
                pass
        elif 0 < now_stationNum < 10:
            if now_direction == '상행':
                qp.drawText(int(6 + 3.7 * now_stationNum) * x, int(8.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(6 + 3.7 * now_stationNum) * x, int(8.5 * x), '◀◀◀')
        elif 10 <= now_stationNum < 20:
            if now_direction == '상행':
                qp.drawText(int(6.1 + 3.5 * (now_stationNum - 10)) * x, int(18.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText(int(6.1 + 3.5 * (now_stationNum - 10)) * x, int(18.5 * x), '▶▶▶')
        elif 20 <= now_stationNum < 30:
            if now_direction == '상행':
                qp.drawText(int(7 + 3.6 * (now_stationNum - 20)) * x, int(28.5 * x), '▶▶▶')
            elif now_direction == '하행':
                qp.drawText(int(7 + 3.6 * (now_stationNum - 20)) * x, int(28.5 * x), '◀◀◀')
        elif now_stationNum == 30:
            if now_direction == '상행':
                pass
            elif now_direction == '하행':
                qp.drawText(8 * x, int(38.5 * x), '▶▶▶')
        elif 31 <= now_stationNum <= 37:
            if now_direction == '상행':
                qp.drawText((12 + 4 * (now_stationNum - 31)) * x, int(38.5 * x), '◀◀◀')
            elif now_direction == '하행':
                qp.drawText((12 + 4 * (now_stationNum - 31)) * x, int(38.5 * x), '▶▶▶')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())   # 이벤트루프 돎

