# -*- coding: utf-8 -*-
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from Constant import CityCode
from WinLayout import WindowLayout
from SqlUtil import search_by_id
from Dispatcher import dataSaver, dataExporter


class WindowLogic(QMainWindow, WindowLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.flush_thread = CrawlDataThread()
        self.export_thread = None

        self.export_path = None
        self.data = ()
        self.text = None

        self.close_button.clicked.connect(self.close)  # 关闭窗口按钮
        self.minimize_button.clicked.connect(self.showMinimized)  # 最小化窗口按钮
        self.search_button.clicked.connect(self.search_data)  # 搜索数据按钮
        self.flush_button.clicked.connect(self.flush_data)  # 刷新数据按钮
        self.export_button.clicked.connect(self.export_data)  # 导出数据按钮

    # ================================== 数据查询 ================================== #
    def search_data(self):
        QApplication.processEvents()
        city_name = self.select_city_comboBox.currentText()
        city_id = CityCode[city_name]
        data = self.select_day_comboBox.currentText()
        self.data = search_by_id(str(city_id), data)[0]
        self.make_text()

    def make_text(self):
        if self.data == ():
            self.text = "暂无结果，请点击刷新按钮"
        else:
            record = self.data
            self.text = (f"{record[1]} {record[3]} {record[2]} 天气如下:"
                         f"\n\n日间天气:{record[4]} \n日间风向:{record[5]}  日间风级:{record[6]}"
                         f"\n\n夜间天气:{record[7]} \n夜间风向:{record[8]}  夜间风级:{record[9]}"
                         f"\n\n平均气温: {record[10]} ~ {record[11]}")
            self.result_label.setText(self.text)
        self.show_label(self.text)

    # ================================== 数据刷新 ================================== #
    def flush_data(self):
        self.show_label("刷新中，请稍后")
        self.flush_button.setEnabled(False)
        self.search_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.flush_thread.signal.connect(self.flush_callback)
        self.flush_thread.start()

    def flush_callback(self, msg):
        self.result_label.setText(msg)
        self.flush_button.setEnabled(True)
        self.search_button.setEnabled(True)
        self.export_button.setEnabled(True)

    # ================================== 数据导出 ================================== #
    def export_data(self):
        self.export_path = QFileDialog.getExistingDirectory(self, '请选择导出文件夹的目录')
        self.show_label("导出中，请稍后")
        self.flush_button.setEnabled(False)
        self.search_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.export_thread = ExportDataThread(self.export_path)
        self.export_thread.signal.connect(self.export_callback)
        self.export_thread.start()

    def export_callback(self, msg):
        self.result_label.setText(msg)
        self.flush_button.setEnabled(True)
        self.search_button.setEnabled(True)
        self.export_button.setEnabled(True)

    def show_label(self, msg):
        self.result_label.setText(msg)


class CrawlDataThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super(CrawlDataThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        QApplication.processEvents()
        dataSaver()
        self.signal.emit("刷新成功")


class ExportDataThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, param):
        super(ExportDataThread, self).__init__()
        self.param = param

    def __del__(self):
        self.wait()

    def run(self):
        QApplication.processEvents()
        dataExporter(self.param, "各省会城市最近7天天气预报.xls")
        self.signal.emit(f"导出成功\n已导入{self.param}目录下")
