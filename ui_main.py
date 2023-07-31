# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)


class Ui_VVCS(object):
    def setupUi(self, VVCS):
        if not VVCS.objectName():
            VVCS.setObjectName(u"VVCS")
        VVCS.resize(621, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VVCS.sizePolicy().hasHeightForWidth())
        VVCS.setSizePolicy(sizePolicy)
        VVCS.setMaximumSize(QSize(1920, 1080))
        VVCS.setWindowTitle(u"Stormworks VVCS")
        VVCS.setStyleSheet(u"background-color: rgb(47, 54, 52);")
        self.centralwidget = QWidget(VVCS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 611, 502))
        self.mainGrid = QGridLayout(self.gridLayoutWidget)
        self.mainGrid.setObjectName(u"mainGrid")
        self.mainGrid.setSizeConstraint(QLayout.SetFixedSize)
        self.mainGrid.setContentsMargins(0, 0, 0, 0)
        self.contextLayout = QVBoxLayout()
        self.contextLayout.setObjectName(u"contextLayout")
        self.contextWidget = QWidget(self.gridLayoutWidget)
        self.contextWidget.setObjectName(u"contextWidget")
        self.contextWidget.setMinimumSize(QSize(250, 0))
        self.contextWidget.setStyleSheet(u"background-color: #1e2422;\n"
"border-radius: 7px;")
        self.CommentLine = QTextEdit(self.contextWidget)
        self.CommentLine.setObjectName(u"CommentLine")
        self.CommentLine.setGeometry(QRect(10, 300, 231, 151))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        self.CommentLine.setFont(font)
        self.CommentLine.setLayoutDirection(Qt.LeftToRight)
        self.CommentLine.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: #323a38;")
        self.CommentLine.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CommentLine.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CommentLine.setAcceptRichText(False)
        self.imageLabel = QLabel(self.contextWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(10, 60, 231, 231))
        self.imageLabel.setMinimumSize(QSize(231, 231))
        self.imageLabel.setStyleSheet(u"background-color: #101010;")
        self.nameLabel = QLabel(self.contextWidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 10, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        self.nameLabel.setFont(font1)
        self.nameLabel.setStyleSheet(u"background-color: #2a2927;\n"
"color: #ececec;\n"
"border-radius: 20px;\n"
"")
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.CommitBtn = QPushButton(self.contextWidget)
        self.CommitBtn.setObjectName(u"CommitBtn")
        self.CommitBtn.setGeometry(QRect(100, 460, 141, 30))
        self.CommitBtn.setMinimumSize(QSize(0, 30))
        self.CommitBtn.setFont(font)
        self.CommitBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255); \n"
"	background-color: #4091b3;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: #449abe;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #397e9b;\n"
"}")
        self.updateLabel = QLabel(self.contextWidget)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(20, 260, 171, 21))
        self.updateLabel.setFont(font1)
        self.updateLabel.setStyleSheet(u"background-color: #101010;\n"
"color: #ececec;\n"
"border-radius: 7px;\n"
"")
        self.updateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refreshBtn = QPushButton(self.contextWidget)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(10, 460, 31, 31))
        self.refreshBtn.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-radius: 15px;\n"
"	image: url(:/icons/refresh.ico);\n"
"	background-color: #1e2422;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: #282e2d;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #3e4342;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/refresh.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.refreshBtn.setIcon(icon)
        self.refreshBtn.setIconSize(QSize(27, 27))

        self.contextLayout.addWidget(self.contextWidget)


        self.mainGrid.addLayout(self.contextLayout, 0, 2, 1, 1)

        self.gameWgt = QWidget(self.gridLayoutWidget)
        self.gameWgt.setObjectName(u"gameWgt")
        self.gameWgt.setMinimumSize(QSize(170, 500))
        self.gameWgt.setStyleSheet(u"background-color: rgb(29, 35, 34);\n"
"border-radius: 10px;")
        self.gameVehiclesList = QListWidget(self.gameWgt)
        self.gameVehiclesList.setObjectName(u"gameVehiclesList")
        self.gameVehiclesList.setGeometry(QRect(10, 40, 151, 411))
        self.gameVehiclesList.setStyleSheet(u"QListWidget {\n"
"	outline: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	gridline-color: black;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background: #293130;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background: #363d3c;\n"
"	outline: 2px solid red;\n"
"	selection-color: #d86e3d;\n"
"\n"
"}\n"
"")
        self.gameVehiclesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gameVehiclesList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.localLabel = QLabel(self.gameWgt)
        self.localLabel.setObjectName(u"localLabel")
        self.localLabel.setGeometry(QRect(10, 0, 151, 31))
        self.localLabel.setFont(font)
        self.localLabel.setStyleSheet(u"color: #d86e3d;\n"
"border-bottom: 1px solid;\n"
"border-radius: 0px;\n"
"border-bottom-color: #494e4d;")
        self.localLabel.setAlignment(Qt.AlignCenter)
        self.syncServBtn = QPushButton(self.gameWgt)
        self.syncServBtn.setObjectName(u"syncServBtn")
        self.syncServBtn.setGeometry(QRect(10, 460, 150, 30))
        self.syncServBtn.setMinimumSize(QSize(150, 30))
        self.syncServBtn.setFont(font)
        self.syncServBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255); \n"
"	background-color: #4091b3;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: #449abe;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #397e9b;\n"
"}")

        self.mainGrid.addWidget(self.gameWgt, 0, 0, 1, 1, Qt.AlignLeft)

        self.serverWgt = QWidget(self.gridLayoutWidget)
        self.serverWgt.setObjectName(u"serverWgt")
        self.serverWgt.setMinimumSize(QSize(170, 500))
        self.serverWgt.setLayoutDirection(Qt.LeftToRight)
        self.serverWgt.setAutoFillBackground(False)
        self.serverWgt.setStyleSheet(u"background-color: rgb(29, 35, 34);\n"
"border-radius: 10px;")
        self.serverVehiclesList = QListWidget(self.serverWgt)
        self.serverVehiclesList.setObjectName(u"serverVehiclesList")
        self.serverVehiclesList.setGeometry(QRect(10, 40, 151, 411))
        self.serverVehiclesList.setStyleSheet(u"QListWidget {\n"
"	outline: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	gridline-color: black;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background: #293130;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background: #363d3c;\n"
"	outline: 2px solid red;\n"
"	selection-color: #d86e3d;\n"
"\n"
"}\n"
"")
        self.serverVehiclesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.serverVehiclesList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(self.serverWgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 151, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #d86e3d;\n"
"border-bottom: 1px solid;\n"
"border-radius: 0px;\n"
"border-bottom-color: #494e4d;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.syncGameBtn = QPushButton(self.serverWgt)
        self.syncGameBtn.setObjectName(u"syncGameBtn")
        self.syncGameBtn.setGeometry(QRect(10, 460, 150, 30))
        self.syncGameBtn.setMinimumSize(QSize(150, 30))
        self.syncGameBtn.setFont(font)
        self.syncGameBtn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255); \n"
"	background-color: #4091b3;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: #449abe;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #397e9b;\n"
"}")

        self.mainGrid.addWidget(self.serverWgt, 0, 1, 1, 1)

        VVCS.setCentralWidget(self.centralwidget)

        self.retranslateUi(VVCS)

        QMetaObject.connectSlotsByName(VVCS)
    # setupUi

    def retranslateUi(self, VVCS):
#if QT_CONFIG(tooltip)
        self.CommentLine.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.CommentLine.setPlaceholderText(QCoreApplication.translate("VVCS", u"Type comment here...", None))
        self.imageLabel.setText("")
        self.nameLabel.setText(QCoreApplication.translate("VVCS", u"Vehicle name", None))
        self.CommitBtn.setText(QCoreApplication.translate("VVCS", u"Commit changes", None))
        self.updateLabel.setText(QCoreApplication.translate("VVCS", u"Last update: 00-00-00 00:00", None))
        self.refreshBtn.setText("")
        self.refreshBtn.setToolTip("Refresh remote objects list")
        self.localLabel.setText(QCoreApplication.translate("VVCS", u"Local objects", None))
        self.syncServBtn.setText(QCoreApplication.translate("VVCS", u"Sync from remote", None))
        self.label_2.setText(QCoreApplication.translate("VVCS", u"Remote objects", None))
        self.syncGameBtn.setText(QCoreApplication.translate("VVCS", u"Sync to remote", None))
        pass
    # retranslateUi

