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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

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
        self.verticalLayout.setObjectName(u"verticalLayout")
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
"	font-size: 16pt;\n"
"}")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")

        self.page_2_layout.addWidget(self.label_2)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.page_3_layout.addWidget(self.label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Page 2", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Page 3", None))
    # retranslateUi

