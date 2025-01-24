import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QLabel, QPushButton, QComboBox, QListWidget, QHBoxLayout
)
from PyQt5.QtChart import QChart, QChartView, QPieSeries


class DashboardTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # 총 자산 라벨
        total_balance = QLabel("총 자산: 1,200,000원")
        total_balance.setStyleSheet("font-size: 24px; color: blue;")
        layout.addWidget(total_balance)

        # 파이 차트
        chart = QChart()
        series = QPieSeries()
        series.append("식비", 40)
        series.append("교통비", 30)
        series.append("기타", 30)

        chart.addSeries(series)
        chart.setTitle("지출 비율")

        chart_view = QChartView(chart)
        chart_view.setMinimumSize(400, 300)
        layout.addWidget(chart_view)

        self.setLayout(layout)


class RecordsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # 새 기록 추가 버튼
        add_record_button = QPushButton("새 기록 추가")
        add_record_button.clicked.connect(self.add_record)
        layout.addWidget(add_record_button)

        # 기록 리스트
        self.record_list = QListWidget()
        self.record_list.addItem("2025-01-22: 점심 -12,000원")
        self.record_list.addItem("2025-01-21: 월급 +2,000,000원")
        layout.addWidget(self.record_list)

        self.setLayout(layout)

    def add_record(self):
        self.record_list.addItem("새로운 기록이 추가되었습니다.")  # 예시


class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # 통화 선택 드롭다운
        currency_selector = QComboBox()
        currency_selector.addItems(["원", "USD", "EUR"])
        layout.addWidget(currency_selector)

        # 데이터 내보내기 버튼
        export_button = QPushButton("데이터 내보내기")
        export_button.clicked.connect(self.export_data)
        layout.addWidget(export_button)

        self.setLayout(layout)

    def export_data(self):
        print("데이터 내보내기 실행!")  # 예시 출력


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("자금 관리 프로그램")
        self.setGeometry(100, 100, 800, 600)

        # 탭 위젯 추가
        tabs = QTabWidget()
        tabs.addTab(DashboardTab(), "대시보드")
        tabs.addTab(RecordsTab(), "기록 관리")
        tabs.addTab(SettingsTab(), "설정")

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
