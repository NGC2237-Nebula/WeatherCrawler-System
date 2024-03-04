# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
from Constant import DayList, CityCode


class WindowLayout(object):
    def __init__(self):
        self.central_widget = None
        self.menubar = None
        self.statusbar = None
        self.title_label = None
        self.result_label = None

        self.search_button = None
        self.flush_button = None
        self.export_button = None

        self.other_button = None
        self.close_button = None
        self.minimize_button = None

        self.select_day_comboBox = None
        self.select_city_comboBox = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")

        # 关闭按钮
        self.close_button = QtWidgets.QPushButton(self.central_widget)
        self.close_button.setGeometry(QtCore.QRect(30, 30, 27, 27))
        self.close_button.setObjectName("close_button")
        # 空白按钮
        self.other_button = QtWidgets.QPushButton(self.central_widget)
        self.other_button.setGeometry(QtCore.QRect(90, 30, 27, 27))
        self.other_button.setObjectName("other_button")
        # 最小化按钮
        self.minimize_button = QtWidgets.QPushButton(self.central_widget)
        self.minimize_button.setGeometry(QtCore.QRect(150, 30, 27, 27))
        self.minimize_button.setObjectName("minimize_button")

        self.title_label = QtWidgets.QLabel(self.central_widget)
        self.title_label.setGeometry(QtCore.QRect(180, 40, 400, 50))
        self.title_label.setObjectName("title_label")
        self.title_label.setText("天气预报查询")

        self.search_button = QtWidgets.QPushButton(self.central_widget)
        self.search_button.setGeometry(QtCore.QRect(400, 120, 90, 28))
        self.search_button.setObjectName("search_button")
        self.search_button.setText("查询")

        self.export_button = QtWidgets.QPushButton(self.central_widget)
        self.export_button.setGeometry(QtCore.QRect(500, 120, 90, 28))
        self.export_button.setObjectName("search_button")
        self.export_button.setText("导出")

        self.flush_button = QtWidgets.QPushButton(self.central_widget)
        self.flush_button.setGeometry(QtCore.QRect(600, 120, 90, 28))
        self.flush_button.setObjectName("search_button")
        self.flush_button.setText("刷新")

        self.select_city_comboBox = QtWidgets.QComboBox(self.central_widget)
        self.select_city_comboBox.setGeometry(QtCore.QRect(60, 120, 150, 28))
        self.select_city_comboBox.setObjectName("select_comboBox")

        for city in CityCode.keys():
            self.select_city_comboBox.addItem(city)

        self.select_day_comboBox = QtWidgets.QComboBox(self.central_widget)
        self.select_day_comboBox.setGeometry(QtCore.QRect(230, 120, 150, 28))
        self.select_day_comboBox.setObjectName("select_comboBox")

        for day in DayList:
            self.select_day_comboBox.addItem(day)

        self.result_label = QtWidgets.QLabel(self.central_widget)
        self.result_label.setGeometry(QtCore.QRect(100, 180, 530, 250))
        self.result_label.setObjectName("result_label")
        self.result_label.setText("查询结果")

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.central_widget.setStyleSheet('''
            QWidget#central_widget{
                border-radius:7px;
                border-image:url(../res/background.png)};}
            ''')

        self.close_button.setStyleSheet('''
            QPushButton{
                background-color: rgba(247, 102, 119, 0.8);
                border-radius:8px;}
            QPushButton:hover{
                background-color: rgba(255, 0, 0, 0.7);}''')
        self.other_button.setStyleSheet('''
            QPushButton{
                background-color: rgba(250, 210, 116, 0.8);
                border-radius:8px;}
            QPushButton:hover{
                background-color: rgba(255, 255, 0, 0.8);}''')
        self.minimize_button.setStyleSheet('''
            QPushButton{
                background-color: rgba(50, 200, 50, 0.8);
                border-radius:8px;}
            QPushButton:hover{
                background-color: rgba(0, 250, 0, 0.8);}''')

        self.result_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.result_label.setStyleSheet('''
                border-radius:5px;
                padding-left: 15px; 
                padding-top: 15px;
                color:white;
                font-size:20px;
                font-weight:bold;
                font-family:Roman times;
                background-color: rgba(255, 255, 255, 0.2)
            ''')

        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet('''
                color:white;
                font-size:23px;
                font-weight:bold;
                font-family:Roman times;
            ''')

        # 设置整体样式
        MainWindow.setWindowOpacity(1)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 隐藏外围边框
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏系统状态栏，并且生成的窗口用户不能移动和改变大小
        MainWindow.setWindowIcon(QIcon('../res/logo.ico'))  # 设置logo


if __name__ == '__main__':
    # 创建一个Qt应用程序对象，用于管理应用程序的事件循环和窗口系统的交互。
    app = QtWidgets.QApplication(sys.argv)
    # 创建一个WindowLayout（自己写的类）对象，创建的时候自动进行初始化__init__
    windowLayout = WindowLayout()
    # 生成一个QtWidgets.QMainWindow对象，用于设置到 WindowLayout.setupUi() 方法中
    mainWindow = QtWidgets.QMainWindow()
    # 调用 WindowLayout.setupUi() 方法，将QtWidgets.QMainWindow对象作为参数传入
    windowLayout.setupUi(mainWindow)
    # 调用 QWidget.setupUi() 方法，展示界面
    mainWindow.show()
    # 调用系统方法进行界面关闭
    sys.exit(app.exec_())
