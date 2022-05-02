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
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

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

        self.page_2_layout.addWidget(self.label_2)

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
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.label_welcome.setFont(font)
        self.label_welcome.setStyleSheet(u"font: 700 30pt \"Ubuntu\";\n"
"color: \"#4f9fee\"")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_welcome)

        self.frame_2 = QFrame(self.main_frame_logged)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 10))
        self.frame_2.setMaximumSize(QSize(16777215, 10))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)

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
        self.frame_btn_mleft.setMaximumSize(QSize(100, 16777215))
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
        self.frame_btn_sright.setMaximumSize(QSize(100, 16777215))
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

        self.page_3_layout1.addWidget(self.label)

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
        self.label1 = QLabel(self.page_4)
        self.label1.setObjectName(u"label1")

        self.page_3_layout2.addWidget(self.label1)

        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Page 2", None))
        self.label_welcome.setText(QCoreApplication.translate("MainPages", u"Welcome back, User!", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Select an operation below to get started:", None))
        self.label_status.setText(QCoreApplication.translate("MainPages", u"Error fetching status data: please contact IT support.", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Page 3", None))
        self.label1.setText(QCoreApplication.translate("MainPages", u"Page 4", None))
    # retranslateUi

