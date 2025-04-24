# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1147, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tConfigurationsRegister = QTableWidget(self.centralwidget)
        if (self.tConfigurationsRegister.columnCount() < 4):
            self.tConfigurationsRegister.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tConfigurationsRegister.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tConfigurationsRegister.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tConfigurationsRegister.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tConfigurationsRegister.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tConfigurationsRegister.rowCount() < 47):
            self.tConfigurationsRegister.setRowCount(47)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(2, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(2, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(3, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(3, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(4, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(4, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(5, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(5, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(6, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(6, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(7, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(7, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(8, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(8, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(9, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(10, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(10, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(11, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(11, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(12, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(12, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(13, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(13, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(14, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(14, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(15, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(15, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(16, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(16, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(17, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(17, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(18, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(18, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(19, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(19, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(20, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(20, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(21, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(21, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(22, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(22, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(23, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(23, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(24, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(24, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(25, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(25, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(26, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(26, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(27, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(27, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(28, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(28, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(29, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(29, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(30, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(30, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(31, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(31, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(32, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(32, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(33, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(33, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(34, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(34, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(35, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(35, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(36, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(36, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(37, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(37, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(38, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(38, 1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(39, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(39, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(40, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(40, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(41, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(41, 1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(42, 0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(42, 1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(43, 0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(43, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(44, 0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(44, 1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(45, 0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(45, 1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(46, 0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tConfigurationsRegister.setItem(46, 1, __qtablewidgetitem97)
        self.tConfigurationsRegister.setObjectName(u"tConfigurationsRegister")
        self.tConfigurationsRegister.setGeometry(QRect(0, 0, 451, 541))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 530, 49, 16))
        self.LStateMachine = QLabel(self.centralwidget)
        self.LStateMachine.setObjectName(u"LStateMachine")
        self.LStateMachine.setGeometry(QRect(500, 530, 271, 20))
        self.cListPort = QComboBox(self.centralwidget)
        self.cListPort.setObjectName(u"cListPort")
        self.cListPort.setGeometry(QRect(460, 470, 311, 22))
        self.bConnectDisconnect = QPushButton(self.centralwidget)
        self.bConnectDisconnect.setObjectName(u"bConnectDisconnect")
        self.bConnectDisconnect.setGeometry(QRect(460, 500, 311, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 450, 49, 16))
        self.tStatusRegister = QTableWidget(self.centralwidget)
        if (self.tStatusRegister.columnCount() < 3):
            self.tStatusRegister.setColumnCount(3)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tStatusRegister.setHorizontalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tStatusRegister.setHorizontalHeaderItem(1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tStatusRegister.setHorizontalHeaderItem(2, __qtablewidgetitem100)
        if (self.tStatusRegister.rowCount() < 14):
            self.tStatusRegister.setRowCount(14)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tStatusRegister.setItem(0, 0, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tStatusRegister.setItem(0, 1, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tStatusRegister.setItem(1, 0, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tStatusRegister.setItem(1, 1, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tStatusRegister.setItem(2, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tStatusRegister.setItem(2, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tStatusRegister.setItem(3, 0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tStatusRegister.setItem(3, 1, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tStatusRegister.setItem(4, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tStatusRegister.setItem(4, 1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tStatusRegister.setItem(5, 0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tStatusRegister.setItem(5, 1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tStatusRegister.setItem(6, 0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tStatusRegister.setItem(6, 1, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tStatusRegister.setItem(7, 0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tStatusRegister.setItem(7, 1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tStatusRegister.setItem(8, 0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tStatusRegister.setItem(8, 1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tStatusRegister.setItem(9, 0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tStatusRegister.setItem(9, 1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tStatusRegister.setItem(10, 0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tStatusRegister.setItem(10, 1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tStatusRegister.setItem(11, 0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tStatusRegister.setItem(11, 1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tStatusRegister.setItem(12, 0, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tStatusRegister.setItem(12, 1, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tStatusRegister.setItem(13, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tStatusRegister.setItem(13, 1, __qtablewidgetitem128)
        self.tStatusRegister.setObjectName(u"tStatusRegister")
        self.tStatusRegister.setGeometry(QRect(460, 0, 341, 441))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(810, 30, 321, 181))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bSPWD = QPushButton(self.gridLayoutWidget)
        self.bSPWD.setObjectName(u"bSPWD")

        self.gridLayout.addWidget(self.bSPWD, 2, 2, 1, 1)

        self.bSCAL = QPushButton(self.gridLayoutWidget)
        self.bSCAL.setObjectName(u"bSCAL")

        self.gridLayout.addWidget(self.bSCAL, 1, 0, 1, 1)

        self.bSFTX = QPushButton(self.gridLayoutWidget)
        self.bSFTX.setObjectName(u"bSFTX")

        self.gridLayout.addWidget(self.bSFTX, 3, 1, 1, 1)

        self.bSXOFF = QPushButton(self.gridLayoutWidget)
        self.bSXOFF.setObjectName(u"bSXOFF")

        self.gridLayout.addWidget(self.bSXOFF, 0, 2, 1, 1)

        self.bSTX = QPushButton(self.gridLayoutWidget)
        self.bSTX.setObjectName(u"bSTX")

        self.gridLayout.addWidget(self.bSTX, 1, 2, 1, 1)

        self.bSRES = QPushButton(self.gridLayoutWidget)
        self.bSRES.setObjectName(u"bSRES")

        self.gridLayout.addWidget(self.bSRES, 0, 0, 1, 1)

        self.bSWORRST = QPushButton(self.gridLayoutWidget)
        self.bSWORRST.setObjectName(u"bSWORRST")

        self.gridLayout.addWidget(self.bSWORRST, 3, 2, 1, 1)

        self.bSRX = QPushButton(self.gridLayoutWidget)
        self.bSRX.setObjectName(u"bSRX")

        self.gridLayout.addWidget(self.bSRX, 1, 1, 1, 1)

        self.bSFSTXON = QPushButton(self.gridLayoutWidget)
        self.bSFSTXON.setObjectName(u"bSFSTXON")

        self.gridLayout.addWidget(self.bSFSTXON, 0, 1, 1, 1)

        self.bSIDLE = QPushButton(self.gridLayoutWidget)
        self.bSIDLE.setObjectName(u"bSIDLE")

        self.gridLayout.addWidget(self.bSIDLE, 2, 0, 1, 1)

        self.bSFRX = QPushButton(self.gridLayoutWidget)
        self.bSFRX.setObjectName(u"bSFRX")

        self.gridLayout.addWidget(self.bSFRX, 3, 0, 1, 1)

        self.bSWOR = QPushButton(self.gridLayoutWidget)
        self.bSWOR.setObjectName(u"bSWOR")

        self.gridLayout.addWidget(self.bSWOR, 2, 1, 1, 1)

        self.bSNOP = QPushButton(self.gridLayoutWidget)
        self.bSNOP.setObjectName(u"bSNOP")

        self.gridLayout.addWidget(self.bSNOP, 4, 1, 1, 1)

        self.bWriteConfigurationsRegister = QPushButton(self.gridLayoutWidget)
        self.bWriteConfigurationsRegister.setObjectName(u"bWriteConfigurationsRegister")

        self.gridLayout.addWidget(self.bWriteConfigurationsRegister, 4, 0, 1, 1)

        self.bLoadFile = QPushButton(self.gridLayoutWidget)
        self.bLoadFile.setObjectName(u"bLoadFile")

        self.gridLayout.addWidget(self.bLoadFile, 4, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(810, 10, 49, 16))
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(810, 230, 321, 103))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bWriteFIFO = QPushButton(self.gridLayoutWidget_2)
        self.bWriteFIFO.setObjectName(u"bWriteFIFO")

        self.gridLayout_2.addWidget(self.bWriteFIFO, 2, 1, 1, 1)

        self.bReadFIFO = QPushButton(self.gridLayoutWidget_2)
        self.bReadFIFO.setObjectName(u"bReadFIFO")

        self.gridLayout_2.addWidget(self.bReadFIFO, 2, 0, 1, 1)

        self.plainFIFO = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainFIFO.setObjectName(u"plainFIFO")

        self.gridLayout_2.addWidget(self.plainFIFO, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1147, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tConfigurationsRegister.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0430", None));
        ___qtablewidgetitem1 = self.tConfigurationsRegister.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0456\u0441\u0442\u0440", None));
        ___qtablewidgetitem2 = self.tConfigurationsRegister.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043a\u0442\u0438\u0447\u043d\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f", None));
        ___qtablewidgetitem3 = self.tConfigurationsRegister.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f", None));

        __sortingEnabled = self.tConfigurationsRegister.isSortingEnabled()
        self.tConfigurationsRegister.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tConfigurationsRegister.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"0x00", None));
        ___qtablewidgetitem5 = self.tConfigurationsRegister.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"IOCFG2", None));
        ___qtablewidgetitem6 = self.tConfigurationsRegister.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"0x01", None));
        ___qtablewidgetitem7 = self.tConfigurationsRegister.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"IOCFG1", None));
        ___qtablewidgetitem8 = self.tConfigurationsRegister.item(2, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"0x02", None));
        ___qtablewidgetitem9 = self.tConfigurationsRegister.item(2, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"IOCFG0", None));
        ___qtablewidgetitem10 = self.tConfigurationsRegister.item(3, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"0x03", None));
        ___qtablewidgetitem11 = self.tConfigurationsRegister.item(3, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"FIFOTHR", None));
        ___qtablewidgetitem12 = self.tConfigurationsRegister.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"0x04", None));
        ___qtablewidgetitem13 = self.tConfigurationsRegister.item(4, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"SYNC1", None));
        ___qtablewidgetitem14 = self.tConfigurationsRegister.item(5, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"0x05", None));
        ___qtablewidgetitem15 = self.tConfigurationsRegister.item(5, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"SYNC0", None));
        ___qtablewidgetitem16 = self.tConfigurationsRegister.item(6, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"0x06", None));
        ___qtablewidgetitem17 = self.tConfigurationsRegister.item(6, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"PKTLEN", None));
        ___qtablewidgetitem18 = self.tConfigurationsRegister.item(7, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"0x07", None));
        ___qtablewidgetitem19 = self.tConfigurationsRegister.item(7, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PKTCTRL1", None));
        ___qtablewidgetitem20 = self.tConfigurationsRegister.item(8, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"0x08", None));
        ___qtablewidgetitem21 = self.tConfigurationsRegister.item(8, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"PKTCTRL0", None));
        ___qtablewidgetitem22 = self.tConfigurationsRegister.item(9, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"0x09", None));
        ___qtablewidgetitem23 = self.tConfigurationsRegister.item(9, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ADDR", None));
        ___qtablewidgetitem24 = self.tConfigurationsRegister.item(10, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0x0A", None));
        ___qtablewidgetitem25 = self.tConfigurationsRegister.item(10, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"CHANNR", None));
        ___qtablewidgetitem26 = self.tConfigurationsRegister.item(11, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"0x0B", None));
        ___qtablewidgetitem27 = self.tConfigurationsRegister.item(11, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"FSCTRL1", None));
        ___qtablewidgetitem28 = self.tConfigurationsRegister.item(12, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"0x0C", None));
        ___qtablewidgetitem29 = self.tConfigurationsRegister.item(12, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"FSCTRL0", None));
        ___qtablewidgetitem30 = self.tConfigurationsRegister.item(13, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"0x0D", None));
        ___qtablewidgetitem31 = self.tConfigurationsRegister.item(13, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"FREQ2", None));
        ___qtablewidgetitem32 = self.tConfigurationsRegister.item(14, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"0x0E", None));
        ___qtablewidgetitem33 = self.tConfigurationsRegister.item(14, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"FREQ1", None));
        ___qtablewidgetitem34 = self.tConfigurationsRegister.item(15, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"0x0F", None));
        ___qtablewidgetitem35 = self.tConfigurationsRegister.item(15, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"FREQ0", None));
        ___qtablewidgetitem36 = self.tConfigurationsRegister.item(16, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"0x10", None));
        ___qtablewidgetitem37 = self.tConfigurationsRegister.item(16, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"MDMCFG4", None));
        ___qtablewidgetitem38 = self.tConfigurationsRegister.item(17, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"0x11", None));
        ___qtablewidgetitem39 = self.tConfigurationsRegister.item(17, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"MDMCFG3", None));
        ___qtablewidgetitem40 = self.tConfigurationsRegister.item(18, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"0x12", None));
        ___qtablewidgetitem41 = self.tConfigurationsRegister.item(18, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"MDMCFG2", None));
        ___qtablewidgetitem42 = self.tConfigurationsRegister.item(19, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"0x13", None));
        ___qtablewidgetitem43 = self.tConfigurationsRegister.item(19, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"MDMCFG1", None));
        ___qtablewidgetitem44 = self.tConfigurationsRegister.item(20, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"0x14", None));
        ___qtablewidgetitem45 = self.tConfigurationsRegister.item(20, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"MDMCFG0", None));
        ___qtablewidgetitem46 = self.tConfigurationsRegister.item(21, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"0x15", None));
        ___qtablewidgetitem47 = self.tConfigurationsRegister.item(21, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"DEVIATN", None));
        ___qtablewidgetitem48 = self.tConfigurationsRegister.item(22, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"0x16", None));
        ___qtablewidgetitem49 = self.tConfigurationsRegister.item(22, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"MCSM2", None));
        ___qtablewidgetitem50 = self.tConfigurationsRegister.item(23, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0x17", None));
        ___qtablewidgetitem51 = self.tConfigurationsRegister.item(23, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"MCSM1", None));
        ___qtablewidgetitem52 = self.tConfigurationsRegister.item(24, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"0x18", None));
        ___qtablewidgetitem53 = self.tConfigurationsRegister.item(24, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"MCSM0", None));
        ___qtablewidgetitem54 = self.tConfigurationsRegister.item(25, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"0x19", None));
        ___qtablewidgetitem55 = self.tConfigurationsRegister.item(25, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"FOCCFG", None));
        ___qtablewidgetitem56 = self.tConfigurationsRegister.item(26, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"0x1A", None));
        ___qtablewidgetitem57 = self.tConfigurationsRegister.item(26, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"BSCFG", None));
        ___qtablewidgetitem58 = self.tConfigurationsRegister.item(27, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"0x1B", None));
        ___qtablewidgetitem59 = self.tConfigurationsRegister.item(27, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"AGCTRL2", None));
        ___qtablewidgetitem60 = self.tConfigurationsRegister.item(28, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"0x1C", None));
        ___qtablewidgetitem61 = self.tConfigurationsRegister.item(28, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"AGCTRL1", None));
        ___qtablewidgetitem62 = self.tConfigurationsRegister.item(29, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"0x1D", None));
        ___qtablewidgetitem63 = self.tConfigurationsRegister.item(29, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"AGCTRL0", None));
        ___qtablewidgetitem64 = self.tConfigurationsRegister.item(30, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0x1E", None));
        ___qtablewidgetitem65 = self.tConfigurationsRegister.item(30, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"WOREVT1", None));
        ___qtablewidgetitem66 = self.tConfigurationsRegister.item(31, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"0x1F", None));
        ___qtablewidgetitem67 = self.tConfigurationsRegister.item(31, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"WOREVT0", None));
        ___qtablewidgetitem68 = self.tConfigurationsRegister.item(32, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"0x20", None));
        ___qtablewidgetitem69 = self.tConfigurationsRegister.item(32, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"WORCTRL", None));
        ___qtablewidgetitem70 = self.tConfigurationsRegister.item(33, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"0x21", None));
        ___qtablewidgetitem71 = self.tConfigurationsRegister.item(33, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"FREND1", None));
        ___qtablewidgetitem72 = self.tConfigurationsRegister.item(34, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"0x22", None));
        ___qtablewidgetitem73 = self.tConfigurationsRegister.item(34, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"FREND0", None));
        ___qtablewidgetitem74 = self.tConfigurationsRegister.item(35, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"0x23", None));
        ___qtablewidgetitem75 = self.tConfigurationsRegister.item(35, 1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"FSCAL3", None));
        ___qtablewidgetitem76 = self.tConfigurationsRegister.item(36, 0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"0x24", None));
        ___qtablewidgetitem77 = self.tConfigurationsRegister.item(36, 1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"FSCAL2", None));
        ___qtablewidgetitem78 = self.tConfigurationsRegister.item(37, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"0x25", None));
        ___qtablewidgetitem79 = self.tConfigurationsRegister.item(37, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"FSCAL1", None));
        ___qtablewidgetitem80 = self.tConfigurationsRegister.item(38, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"0x26", None));
        ___qtablewidgetitem81 = self.tConfigurationsRegister.item(38, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"FSCAL0", None));
        ___qtablewidgetitem82 = self.tConfigurationsRegister.item(39, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"0x27", None));
        ___qtablewidgetitem83 = self.tConfigurationsRegister.item(39, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"RCCTRL1", None));
        ___qtablewidgetitem84 = self.tConfigurationsRegister.item(40, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"0x28", None));
        ___qtablewidgetitem85 = self.tConfigurationsRegister.item(40, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"RCCTRL0", None));
        ___qtablewidgetitem86 = self.tConfigurationsRegister.item(41, 0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"0x29", None));
        ___qtablewidgetitem87 = self.tConfigurationsRegister.item(41, 1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"FSTEST", None));
        ___qtablewidgetitem88 = self.tConfigurationsRegister.item(42, 0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"0x2A", None));
        ___qtablewidgetitem89 = self.tConfigurationsRegister.item(42, 1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"PTEST", None));
        ___qtablewidgetitem90 = self.tConfigurationsRegister.item(43, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"0x2B", None));
        ___qtablewidgetitem91 = self.tConfigurationsRegister.item(43, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"AGCTEST", None));
        ___qtablewidgetitem92 = self.tConfigurationsRegister.item(44, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"0x2C", None));
        ___qtablewidgetitem93 = self.tConfigurationsRegister.item(44, 1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"TEST2", None));
        ___qtablewidgetitem94 = self.tConfigurationsRegister.item(45, 0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"0x2D", None));
        ___qtablewidgetitem95 = self.tConfigurationsRegister.item(45, 1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"TEST1", None));
        ___qtablewidgetitem96 = self.tConfigurationsRegister.item(46, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"0x2E", None));
        ___qtablewidgetitem97 = self.tConfigurationsRegister.item(46, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"TEST0", None));
        self.tConfigurationsRegister.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.LStateMachine.setText(QCoreApplication.translate("MainWindow", u"Unknown", None))
        self.bConnectDisconnect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        ___qtablewidgetitem98 = self.tStatusRegister.horizontalHeaderItem(0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0430", None));
        ___qtablewidgetitem99 = self.tStatusRegister.horizontalHeaderItem(1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0456\u0441\u0442\u0440", None));
        ___qtablewidgetitem100 = self.tStatusRegister.horizontalHeaderItem(2)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u043d\u044f", None));

        __sortingEnabled1 = self.tStatusRegister.isSortingEnabled()
        self.tStatusRegister.setSortingEnabled(False)
        ___qtablewidgetitem101 = self.tStatusRegister.item(0, 0)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"0xF0", None));
        ___qtablewidgetitem102 = self.tStatusRegister.item(0, 1)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"PARTNUM", None));
        ___qtablewidgetitem103 = self.tStatusRegister.item(1, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"0xF1", None));
        ___qtablewidgetitem104 = self.tStatusRegister.item(1, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"VERSION", None));
        ___qtablewidgetitem105 = self.tStatusRegister.item(2, 0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"0xF2", None));
        ___qtablewidgetitem106 = self.tStatusRegister.item(2, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"FREQEST", None));
        ___qtablewidgetitem107 = self.tStatusRegister.item(3, 0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"0xF3", None));
        ___qtablewidgetitem108 = self.tStatusRegister.item(3, 1)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"LQI", None));
        ___qtablewidgetitem109 = self.tStatusRegister.item(4, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"0xF4", None));
        ___qtablewidgetitem110 = self.tStatusRegister.item(4, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"RSSI", None));
        ___qtablewidgetitem111 = self.tStatusRegister.item(5, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"0xF5", None));
        ___qtablewidgetitem112 = self.tStatusRegister.item(5, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"MARCSTATE", None));
        ___qtablewidgetitem113 = self.tStatusRegister.item(6, 0)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"0xF6", None));
        ___qtablewidgetitem114 = self.tStatusRegister.item(6, 1)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"WORTIME1", None));
        ___qtablewidgetitem115 = self.tStatusRegister.item(7, 0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"0xF7", None));
        ___qtablewidgetitem116 = self.tStatusRegister.item(7, 1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"WORTIME0", None));
        ___qtablewidgetitem117 = self.tStatusRegister.item(8, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"0xF8", None));
        ___qtablewidgetitem118 = self.tStatusRegister.item(8, 1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"PKTSTATUS", None));
        ___qtablewidgetitem119 = self.tStatusRegister.item(9, 0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"0xF9", None));
        ___qtablewidgetitem120 = self.tStatusRegister.item(9, 1)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"VCO_VC_DAC", None));
        ___qtablewidgetitem121 = self.tStatusRegister.item(10, 0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"0xFA", None));
        ___qtablewidgetitem122 = self.tStatusRegister.item(10, 1)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"TXBYTES", None));
        ___qtablewidgetitem123 = self.tStatusRegister.item(11, 0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"0xFB", None));
        ___qtablewidgetitem124 = self.tStatusRegister.item(11, 1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"RXBYTES", None));
        ___qtablewidgetitem125 = self.tStatusRegister.item(12, 0)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"0xFC", None));
        ___qtablewidgetitem126 = self.tStatusRegister.item(12, 1)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"RCCTRL1_STATUS", None));
        ___qtablewidgetitem127 = self.tStatusRegister.item(13, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"0xFD", None));
        ___qtablewidgetitem128 = self.tStatusRegister.item(13, 1)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"RCCTRL0_STATUS", None));
        self.tStatusRegister.setSortingEnabled(__sortingEnabled1)

        self.bSPWD.setText(QCoreApplication.translate("MainWindow", u"SPWD", None))
        self.bSCAL.setText(QCoreApplication.translate("MainWindow", u"SCAL", None))
        self.bSFTX.setText(QCoreApplication.translate("MainWindow", u"SFTX", None))
        self.bSXOFF.setText(QCoreApplication.translate("MainWindow", u"SXOFF", None))
        self.bSTX.setText(QCoreApplication.translate("MainWindow", u"STX", None))
        self.bSRES.setText(QCoreApplication.translate("MainWindow", u"SRES", None))
        self.bSWORRST.setText(QCoreApplication.translate("MainWindow", u"SWORRST", None))
        self.bSRX.setText(QCoreApplication.translate("MainWindow", u"SRX", None))
        self.bSFSTXON.setText(QCoreApplication.translate("MainWindow", u"SFSTXON", None))
        self.bSIDLE.setText(QCoreApplication.translate("MainWindow", u"SIDLE", None))
        self.bSFRX.setText(QCoreApplication.translate("MainWindow", u"SFRX", None))
        self.bSWOR.setText(QCoreApplication.translate("MainWindow", u"SWOR", None))
        self.bSNOP.setText(QCoreApplication.translate("MainWindow", u"SNOP", None))
        self.bWriteConfigurationsRegister.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u0438 \u043a\u043e\u043d\u0444.", None))
        self.bLoadFile.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0438", None))
        self.bWriteFIFO.setText(QCoreApplication.translate("MainWindow", u"TX FIFO", None))
        self.bReadFIFO.setText(QCoreApplication.translate("MainWindow", u"RX FIFO", None))
    # retranslateUi

