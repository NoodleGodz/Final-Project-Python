# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.main_frame = QFrame(self.page_1)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_welcome_icon = QFrame(self.main_frame)
        self.frame_welcome_icon.setObjectName(u"frame_welcome_icon")
        self.frame_welcome_icon.setMaximumSize(QSize(16777215, 16777215))
        self.frame_welcome_icon.setFrameShape(QFrame.NoFrame)
        self.frame_welcome_icon.setFrameShadow(QFrame.Plain)
        self.frame_logo = QVBoxLayout(self.frame_welcome_icon)
        self.frame_logo.setSpacing(0)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_welcome_icon)

        self.frame_middle_padding = QFrame(self.main_frame)
        self.frame_middle_padding.setObjectName(u"frame_middle_padding")
        self.frame_middle_padding.setMinimumSize(QSize(0, 25))
        self.frame_middle_padding.setFrameShape(QFrame.NoFrame)
        self.frame_middle_padding.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_middle_padding)

        self.frame_cred = QFrame(self.main_frame)
        self.frame_cred.setObjectName(u"frame_cred")
        self.frame_cred.setMinimumSize(QSize(0, 0))
        self.frame_cred.setFrameShape(QFrame.NoFrame)
        self.frame_cred.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_cred)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_username = QFrame(self.frame_cred)
        self.frame_username.setObjectName(u"frame_username")
        self.frame_username.setMinimumSize(QSize(300, 36))
        self.frame_username.setMaximumSize(QSize(300, 36))
        self.frame_username.setFrameShape(QFrame.NoFrame)
        self.frame_username.setFrameShadow(QFrame.Plain)
        self.layout_username = QVBoxLayout(self.frame_username)
        self.layout_username.setSpacing(0)
        self.layout_username.setObjectName(u"layout_username")
        self.layout_username.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_username, 0, Qt.AlignHCenter)

        self.frame_password = QFrame(self.frame_cred)
        self.frame_password.setObjectName(u"frame_password")
        self.frame_password.setMinimumSize(QSize(300, 36))
        self.frame_password.setMaximumSize(QSize(300, 36))
        self.frame_password.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_password.setLayoutDirection(Qt.LeftToRight)
        self.frame_password.setFrameShape(QFrame.NoFrame)
        self.frame_password.setFrameShadow(QFrame.Plain)
        self.layout_password = QVBoxLayout(self.frame_password)
        self.layout_password.setSpacing(0)
        self.layout_password.setObjectName(u"layout_password")
        self.layout_password.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_password, 0, Qt.AlignHCenter)

        self.frame_login = QFrame(self.frame_cred)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMinimumSize(QSize(100, 36))
        self.frame_login.setMaximumSize(QSize(100, 36))
        self.frame_login.setFrameShape(QFrame.NoFrame)
        self.frame_login.setFrameShadow(QFrame.Plain)
        self.layout_login = QVBoxLayout(self.frame_login)
        self.layout_login.setSpacing(0)
        self.layout_login.setObjectName(u"layout_login")
        self.layout_login.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_login, 0, Qt.AlignHCenter)

        self.frame_bottom_padding = QFrame(self.frame_cred)
        self.frame_bottom_padding.setObjectName(u"frame_bottom_padding")
        self.frame_bottom_padding.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_padding.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_bottom_padding)


        self.verticalLayout.addWidget(self.frame_cred)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)

        self.page_1_layout.addWidget(self.main_frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame {\n"
"	  font-size: 16pt;\n"
"       }")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setStyleSheet(u"font: 45pt \"Ubuntu\";\n"
"color: rgb(79, 159, 238);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.page_2_layout.addWidget(self.label_2)

        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 10))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.page_2_layout.addWidget(self.frame_3)

        self.label_from_to = QLabel(self.page_2)
        self.label_from_to.setObjectName(u"label_from_to")
        self.label_from_to.setMaximumSize(QSize(16777215, 50))
        self.label_from_to.setAlignment(Qt.AlignCenter)

        self.page_2_layout.addWidget(self.label_from_to)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 10))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.page_2_layout.addWidget(self.frame_5)

        self.frame_linechart = QFrame(self.page_2)
        self.frame_linechart.setObjectName(u"frame_linechart")
        self.frame_linechart.setMinimumSize(QSize(0, 275))
        self.frame_linechart.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_linechart.setFrameShape(QFrame.NoFrame)
        self.frame_linechart.setFrameShadow(QFrame.Raised)
        self.layout_linechart = QVBoxLayout(self.frame_linechart)
        self.layout_linechart.setSpacing(0)
        self.layout_linechart.setObjectName(u"layout_linechart")
        self.layout_linechart.setContentsMargins(0, 0, 0, 0)

        self.page_2_layout.addWidget(self.frame_linechart)

        self.frame_stat_btn = QFrame(self.page_2)
        self.frame_stat_btn.setObjectName(u"frame_stat_btn")
        self.frame_stat_btn.setMinimumSize(QSize(0, 0))
        self.frame_stat_btn.setFrameShape(QFrame.NoFrame)
        self.frame_stat_btn.setFrameShadow(QFrame.Raised)
        self.layout_stat_btns = QHBoxLayout(self.frame_stat_btn)
        self.layout_stat_btns.setSpacing(10)
        self.layout_stat_btns.setObjectName(u"layout_stat_btns")
        self.layout_stat_btns.setContentsMargins(15, 0, 15, 10)
        self.frame_export_usage = QFrame(self.frame_stat_btn)
        self.frame_export_usage.setObjectName(u"frame_export_usage")
        self.frame_export_usage.setFrameShape(QFrame.NoFrame)
        self.frame_export_usage.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_export_usage = QVBoxLayout(self.frame_export_usage)
        self.layout_frame_btn_export_usage.setSpacing(0)
        self.layout_frame_btn_export_usage.setObjectName(u"layout_frame_btn_export_usage")
        self.layout_frame_btn_export_usage.setContentsMargins(0, 0, 0, 0)

        self.layout_stat_btns.addWidget(self.frame_export_usage)

        self.frame_export_price = QFrame(self.frame_stat_btn)
        self.frame_export_price.setObjectName(u"frame_export_price")
        self.frame_export_price.setFrameShape(QFrame.NoFrame)
        self.frame_export_price.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_export_price = QVBoxLayout(self.frame_export_price)
        self.layout_frame_btn_export_price.setSpacing(0)
        self.layout_frame_btn_export_price.setObjectName(u"layout_frame_btn_export_price")
        self.layout_frame_btn_export_price.setContentsMargins(0, 0, 0, 0)

        self.layout_stat_btns.addWidget(self.frame_export_price)

        self.frame_flush = QFrame(self.frame_stat_btn)
        self.frame_flush.setObjectName(u"frame_flush")
        self.frame_flush.setFrameShape(QFrame.NoFrame)
        self.frame_flush.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_flush = QVBoxLayout(self.frame_flush)
        self.layout_frame_btn_flush.setSpacing(0)
        self.layout_frame_btn_flush.setObjectName(u"layout_frame_btn_flush")
        self.layout_frame_btn_flush.setContentsMargins(0, 0, 0, 0)

        self.layout_stat_btns.addWidget(self.frame_flush)

        self.frame_load_versipn = QFrame(self.frame_stat_btn)
        self.frame_load_versipn.setObjectName(u"frame_load_versipn")
        self.frame_load_versipn.setFrameShape(QFrame.NoFrame)
        self.frame_load_versipn.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_load_version = QVBoxLayout(self.frame_load_versipn)
        self.layout_frame_btn_load_version.setSpacing(0)
        self.layout_frame_btn_load_version.setObjectName(u"layout_frame_btn_load_version")
        self.layout_frame_btn_load_version.setContentsMargins(0, 0, 0, 0)

        self.layout_stat_btns.addWidget(self.frame_load_versipn)


        self.page_2_layout.addWidget(self.frame_stat_btn)

        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 20))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.page_2_layout.addWidget(self.frame_11)

        self.pages.addWidget(self.page_2)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.page_0.setStyleSheet(u"QFrame {\n"
"	  font-size: 16pt;\n"
"       }")
        self.page_3_layout = QVBoxLayout(self.page_0)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_0)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.page_3_layout.addWidget(self.frame)

        self.main_frame_logged = QFrame(self.page_0)
        self.main_frame_logged.setObjectName(u"main_frame_logged")
        self.main_frame_logged.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame_logged.setFrameShape(QFrame.NoFrame)
        self.main_frame_logged.setFrameShadow(QFrame.Plain)
        self.main_frame_logged.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame_logged)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_welcome = QLabel(self.main_frame_logged)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(45)
        font.setBold(False)
        font.setItalic(False)
        self.label_welcome.setFont(font)
        self.label_welcome.setStyleSheet(u"font: 45pt \"Ubuntu\";\n"
"color: \"#4f9fee\"")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_welcome)

        self.frame_2 = QFrame(self.main_frame_logged)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 10))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.label_datetime = QLabel(self.main_frame_logged)
        self.label_datetime.setObjectName(u"label_datetime")
        self.label_datetime.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_datetime)

        self.frame_4 = QFrame(self.main_frame_logged)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 10))
        self.frame_4.setMaximumSize(QSize(16777215, 10))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.label_4 = QLabel(self.main_frame_logged)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 75))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.logged_btn_logged_frame = QFrame(self.main_frame_logged)
        self.logged_btn_logged_frame.setObjectName(u"logged_btn_logged_frame")
        self.logged_btn_logged_frame.setMinimumSize(QSize(0, 160))
        self.logged_btn_logged_frame.setFrameShape(QFrame.NoFrame)
        self.logged_btn_logged_frame.setFrameShadow(QFrame.Raised)
        self.layout_btn_logged_frame = QHBoxLayout(self.logged_btn_logged_frame)
        self.layout_btn_logged_frame.setSpacing(15)
        self.layout_btn_logged_frame.setObjectName(u"layout_btn_logged_frame")
        self.layout_btn_logged_frame.setContentsMargins(-1, -1, 9, -1)
        self.frame_btn_mleft = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_mleft.setObjectName(u"frame_btn_mleft")
        self.frame_btn_mleft.setMaximumSize(QSize(50, 16777215))
        self.frame_btn_mleft.setFrameShape(QFrame.NoFrame)
        self.frame_btn_mleft.setFrameShadow(QFrame.Raised)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_mleft)

        self.frame_btn_stat = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_stat.setObjectName(u"frame_btn_stat")
        self.frame_btn_stat.setMinimumSize(QSize(0, 0))
        self.frame_btn_stat.setFrameShape(QFrame.NoFrame)
        self.frame_btn_stat.setFrameShadow(QFrame.Plain)
        self.layout_frame_btn_stat = QVBoxLayout(self.frame_btn_stat)
        self.layout_frame_btn_stat.setSpacing(0)
        self.layout_frame_btn_stat.setObjectName(u"layout_frame_btn_stat")
        self.layout_frame_btn_stat.setContentsMargins(0, 0, 0, 0)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_stat)

        self.frame_btn_manage = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_manage.setObjectName(u"frame_btn_manage")
        self.frame_btn_manage.setMinimumSize(QSize(0, 0))
        self.frame_btn_manage.setFrameShape(QFrame.NoFrame)
        self.frame_btn_manage.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_manage = QVBoxLayout(self.frame_btn_manage)
        self.layout_frame_btn_manage.setSpacing(0)
        self.layout_frame_btn_manage.setObjectName(u"layout_frame_btn_manage")
        self.layout_frame_btn_manage.setContentsMargins(0, 0, 0, 0)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_manage)

        self.frame_btn_newday = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_newday.setObjectName(u"frame_btn_newday")
        self.frame_btn_newday.setFrameShape(QFrame.NoFrame)
        self.frame_btn_newday.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_newday = QVBoxLayout(self.frame_btn_newday)
        self.layout_frame_btn_newday.setSpacing(0)
        self.layout_frame_btn_newday.setObjectName(u"layout_frame_btn_newday")
        self.layout_frame_btn_newday.setContentsMargins(0, 0, 0, 0)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_newday)

        self.frame_btn_logout = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_logout.setObjectName(u"frame_btn_logout")
        self.frame_btn_logout.setFrameShape(QFrame.NoFrame)
        self.frame_btn_logout.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_logout = QVBoxLayout(self.frame_btn_logout)
        self.layout_frame_btn_logout.setSpacing(0)
        self.layout_frame_btn_logout.setObjectName(u"layout_frame_btn_logout")
        self.layout_frame_btn_logout.setContentsMargins(0, 0, 0, 0)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_logout)

        self.frame_btn_sright = QFrame(self.logged_btn_logged_frame)
        self.frame_btn_sright.setObjectName(u"frame_btn_sright")
        self.frame_btn_sright.setMinimumSize(QSize(0, 0))
        self.frame_btn_sright.setMaximumSize(QSize(50, 16777215))
        self.frame_btn_sright.setFrameShape(QFrame.NoFrame)
        self.frame_btn_sright.setFrameShadow(QFrame.Raised)

        self.layout_btn_logged_frame.addWidget(self.frame_btn_sright)


        self.verticalLayout_3.addWidget(self.logged_btn_logged_frame)


        self.page_3_layout.addWidget(self.main_frame_logged)

        self.frame_6 = QFrame(self.page_0)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 100))
        self.frame_6.setMaximumSize(QSize(16777215, 120))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.frame_6)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 0))
        self.label_status.setMaximumSize(QSize(16777215, 16777215))
        self.label_status.setStyleSheet(u"font: 10pt \"Ubuntu\";")
        self.label_status.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_2.addWidget(self.label_status)


        self.page_3_layout.addWidget(self.frame_6)

        self.pages.addWidget(self.page_0)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	  font-size: 16pt;\n"
"       }")
        self.page_3_layout1 = QVBoxLayout(self.page_3)
        self.page_3_layout1.setSpacing(5)
        self.page_3_layout1.setObjectName(u"page_3_layout1")
        self.page_3_layout1.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 45pt \"Ubuntu\";\n"
"color: rgb(79, 159, 238);")
        self.label.setAlignment(Qt.AlignCenter)

        self.page_3_layout1.addWidget(self.label)

        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.page_3_layout1.addWidget(self.frame_15)

        self.frame_btn_add_cstmr = QFrame(self.page_3)
        self.frame_btn_add_cstmr.setObjectName(u"frame_btn_add_cstmr")
        self.frame_btn_add_cstmr.setMinimumSize(QSize(0, 100))
        self.frame_btn_add_cstmr.setStyleSheet(u"font: 16pt \"Ubuntu\";")
        self.frame_btn_add_cstmr.setFrameShape(QFrame.NoFrame)
        self.frame_btn_add_cstmr.setFrameShadow(QFrame.Raised)
        self.layout_btn_add_cstmr = QVBoxLayout(self.frame_btn_add_cstmr)
        self.layout_btn_add_cstmr.setSpacing(0)
        self.layout_btn_add_cstmr.setObjectName(u"layout_btn_add_cstmr")
        self.layout_btn_add_cstmr.setContentsMargins(0, 0, 0, 0)

        self.page_3_layout1.addWidget(self.frame_btn_add_cstmr)

        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.page_3_layout1.addWidget(self.frame_13)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(300, 36))
        self.label_3.setMaximumSize(QSize(16777212, 16777215))
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.page_3_layout1.addWidget(self.label_3)

        self.frame_labeledit_search = QFrame(self.page_3)
        self.frame_labeledit_search.setObjectName(u"frame_labeledit_search")
        self.frame_labeledit_search.setMinimumSize(QSize(500, 36))
        self.frame_labeledit_search.setMaximumSize(QSize(500, 36))
        self.frame_labeledit_search.setFrameShape(QFrame.NoFrame)
        self.frame_labeledit_search.setFrameShadow(QFrame.Raised)
        self.layout_frame_labeledit_search = QVBoxLayout(self.frame_labeledit_search)
        self.layout_frame_labeledit_search.setSpacing(0)
        self.layout_frame_labeledit_search.setObjectName(u"layout_frame_labeledit_search")
        self.layout_frame_labeledit_search.setContentsMargins(0, 0, 0, 0)

        self.page_3_layout1.addWidget(self.frame_labeledit_search, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_18 = QFrame(self.page_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.page_3_layout1.addWidget(self.frame_18)

        self.label_match_text = QLabel(self.page_3)
        self.label_match_text.setObjectName(u"label_match_text")
        self.label_match_text.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.page_3_layout1.addWidget(self.label_match_text)

        self.listWidget_cstmr = QListWidget(self.page_3)
        self.listWidget_cstmr.setObjectName(u"listWidget_cstmr")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_cstmr.sizePolicy().hasHeightForWidth())
        self.listWidget_cstmr.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.listWidget_cstmr.setFont(font1)
        self.listWidget_cstmr.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"font: 11pt \"Ubuntu\";")

        self.page_3_layout1.addWidget(self.listWidget_cstmr)

        self.frame_17 = QFrame(self.page_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.page_3_layout1.addWidget(self.frame_17)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"QFrame {\n"
"	  font-size: 16pt;\n"
"       }")
        self.page_3_layout2 = QVBoxLayout(self.page_4)
        self.page_3_layout2.setSpacing(5)
        self.page_3_layout2.setObjectName(u"page_3_layout2")
        self.page_3_layout2.setContentsMargins(5, 5, 5, 5)
        self.frame_cstmr_back = QFrame(self.page_4)
        self.frame_cstmr_back.setObjectName(u"frame_cstmr_back")
        self.frame_cstmr_back.setMaximumSize(QSize(200, 35))
        self.frame_cstmr_back.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_back.setFrameShadow(QFrame.Raised)
        self.layout_frame_cstmr_back = QVBoxLayout(self.frame_cstmr_back)
        self.layout_frame_cstmr_back.setSpacing(0)
        self.layout_frame_cstmr_back.setObjectName(u"layout_frame_cstmr_back")
        self.layout_frame_cstmr_back.setContentsMargins(0, 0, 0, 0)

        self.page_3_layout2.addWidget(self.frame_cstmr_back)

        self.frame_7 = QFrame(self.page_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 375))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_icon_template = QFrame(self.frame_9)
        self.frame_icon_template.setObjectName(u"frame_icon_template")
        self.frame_icon_template.setMinimumSize(QSize(256, 256))
        self.frame_icon_template.setMaximumSize(QSize(256, 256))
        self.frame_icon_template.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_template.setFrameShadow(QFrame.Raised)
        self.layout_icon_template = QVBoxLayout(self.frame_icon_template)
        self.layout_icon_template.setObjectName(u"layout_icon_template")

        self.verticalLayout_4.addWidget(self.frame_icon_template, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_cstmr_title_name = QLabel(self.frame_10)
        self.label_cstmr_title_name.setObjectName(u"label_cstmr_title_name")
        self.label_cstmr_title_name.setStyleSheet(u"font: 30pt \"Ubuntu\";\n"
"color: rgb(79, 159, 238);")

        self.verticalLayout_5.addWidget(self.label_cstmr_title_name)

        self.frame_view_edit_profile = QFrame(self.frame_10)
        self.frame_view_edit_profile.setObjectName(u"frame_view_edit_profile")
        self.frame_view_edit_profile.setMinimumSize(QSize(0, 30))
        self.frame_view_edit_profile.setMaximumSize(QSize(175, 30))
        self.frame_view_edit_profile.setFrameShape(QFrame.StyledPanel)
        self.frame_view_edit_profile.setFrameShadow(QFrame.Raised)
        self.layout_frame_view_edit_profile = QVBoxLayout(self.frame_view_edit_profile)
        self.layout_frame_view_edit_profile.setSpacing(0)
        self.layout_frame_view_edit_profile.setObjectName(u"layout_frame_view_edit_profile")
        self.layout_frame_view_edit_profile.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_view_edit_profile)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_14)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.billing_text_browser = QTextBrowser(self.frame_10)
        self.billing_text_browser.setObjectName(u"billing_text_browser")
        sizePolicy.setHeightForWidth(self.billing_text_browser.sizePolicy().hasHeightForWidth())
        self.billing_text_browser.setSizePolicy(sizePolicy)
        self.billing_text_browser.setStyleSheet(u"background-color: rgb(40, 44, 52);")

        self.verticalLayout_5.addWidget(self.billing_text_browser)


        self.horizontalLayout.addWidget(self.frame_10)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.page_3_layout2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_btn_export_customer = QFrame(self.frame_12)
        self.frame_btn_export_customer.setObjectName(u"frame_btn_export_customer")
        self.frame_btn_export_customer.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_export_customer.setFrameShadow(QFrame.Raised)
        self.layout_frame_export_customer = QVBoxLayout(self.frame_btn_export_customer)
        self.layout_frame_export_customer.setSpacing(0)
        self.layout_frame_export_customer.setObjectName(u"layout_frame_export_customer")
        self.layout_frame_export_customer.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_btn_export_customer)

        self.frame_btn_cstmr_plot = QFrame(self.frame_12)
        self.frame_btn_cstmr_plot.setObjectName(u"frame_btn_cstmr_plot")
        self.frame_btn_cstmr_plot.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_cstmr_plot.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_cstmr_plot = QVBoxLayout(self.frame_btn_cstmr_plot)
        self.layout_frame_btn_cstmr_plot.setSpacing(0)
        self.layout_frame_btn_cstmr_plot.setObjectName(u"layout_frame_btn_cstmr_plot")
        self.layout_frame_btn_cstmr_plot.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_btn_cstmr_plot)

        self.frame_btn_toggle_contract = QFrame(self.frame_12)
        self.frame_btn_toggle_contract.setObjectName(u"frame_btn_toggle_contract")
        self.frame_btn_toggle_contract.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_toggle_contract.setFrameShadow(QFrame.Raised)
        self.layout_frame_btn_toggle_contract = QVBoxLayout(self.frame_btn_toggle_contract)
        self.layout_frame_btn_toggle_contract.setSpacing(0)
        self.layout_frame_btn_toggle_contract.setObjectName(u"layout_frame_btn_toggle_contract")
        self.layout_frame_btn_toggle_contract.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_btn_toggle_contract)


        self.verticalLayout_7.addWidget(self.frame_12)


        self.page_3_layout2.addWidget(self.frame_8)

        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Statistic Dashboard", None))
        self.label_from_to.setText(QCoreApplication.translate("MainPages", u"From DateTime to DateTime", None))
        self.label_welcome.setText(QCoreApplication.translate("MainPages", u"Welcome back, User!", None))
        self.label_datetime.setText(QCoreApplication.translate("MainPages", u"Error fetching status data: please contact IT support.", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Select an operation below to get started:", None))
        self.label_status.setText(QCoreApplication.translate("MainPages", u"Error fetching status data: please contact IT support.", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Customers Management", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Or, search for Customer ID:", None))
        self.label_match_text.setText(QCoreApplication.translate("MainPages", u"XXX matches found, double-click to open Detailed View", None))
        self.label_cstmr_title_name.setText(QCoreApplication.translate("MainPages", u"Customer Name Here", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Contract Info", None))
        self.billing_text_browser.setMarkdown("")
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Operations Panel", None))
    # retranslateUi

