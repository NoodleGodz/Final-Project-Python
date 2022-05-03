# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
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

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_image = QFrame(self.menu_1)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMinimumSize(QSize(84, 84))
        self.frame_image.setMaximumSize(QSize(84, 84))
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Plain)
        self.layout_cstmr_image_right = QHBoxLayout(self.frame_image)
        self.layout_cstmr_image_right.setSpacing(0)
        self.layout_cstmr_image_right.setObjectName(u"layout_cstmr_image_right")
        self.layout_cstmr_image_right.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_image, 0, Qt.AlignHCenter)

        self.frame_cstmr_name = QFrame(self.menu_1)
        self.frame_cstmr_name.setObjectName(u"frame_cstmr_name")
        self.frame_cstmr_name.setMaximumSize(QSize(16777215, 40))
        self.frame_cstmr_name.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_name.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_name_input = QVBoxLayout(self.frame_cstmr_name)
        self.layout_cstmr_name_input.setSpacing(0)
        self.layout_cstmr_name_input.setObjectName(u"layout_cstmr_name_input")
        self.layout_cstmr_name_input.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_cstmr_name)

        self.frame_2 = QFrame(self.menu_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_cstmr_page = QFrame(self.frame_2)
        self.frame_cstmr_page.setObjectName(u"frame_cstmr_page")
        self.frame_cstmr_page.setMaximumSize(QSize(16777215, 36))
        self.frame_cstmr_page.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_page.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cstmr_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_cstmr_back = QFrame(self.frame_cstmr_page)
        self.frame_cstmr_back.setObjectName(u"frame_cstmr_back")
        self.frame_cstmr_back.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_back.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_back = QVBoxLayout(self.frame_cstmr_back)
        self.layout_cstmr_back.setSpacing(0)
        self.layout_cstmr_back.setObjectName(u"layout_cstmr_back")
        self.layout_cstmr_back.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_cstmr_back)


        self.verticalLayout_3.addWidget(self.frame_cstmr_page)

        self.frame_prop = QFrame(self.frame_2)
        self.frame_prop.setObjectName(u"frame_prop")
        self.frame_prop.setMaximumSize(QSize(16777215, 16777215))
        self.frame_prop.setFrameShape(QFrame.StyledPanel)
        self.frame_prop.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_prop)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.frame_cstmr_id = QFrame(self.frame_prop)
        self.frame_cstmr_id.setObjectName(u"frame_cstmr_id")
        self.frame_cstmr_id.setMaximumSize(QSize(16777215, 60))
        self.frame_cstmr_id.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_id.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_cstmr_id)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_cstmr_id)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.label_3.setIndent(3)

        self.verticalLayout_5.addWidget(self.label_3)

        self.frame_cstmr_id_input = QFrame(self.frame_cstmr_id)
        self.frame_cstmr_id_input.setObjectName(u"frame_cstmr_id_input")
        self.frame_cstmr_id_input.setMinimumSize(QSize(0, 30))
        self.frame_cstmr_id_input.setMaximumSize(QSize(16777215, 30))
        self.frame_cstmr_id_input.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_id_input.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_id_input = QVBoxLayout(self.frame_cstmr_id_input)
        self.layout_cstmr_id_input.setSpacing(0)
        self.layout_cstmr_id_input.setObjectName(u"layout_cstmr_id_input")
        self.layout_cstmr_id_input.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_cstmr_id_input)


        self.verticalLayout_4.addWidget(self.frame_cstmr_id)

        self.frame_cstmr_address = QFrame(self.frame_prop)
        self.frame_cstmr_address.setObjectName(u"frame_cstmr_address")
        self.frame_cstmr_address.setMaximumSize(QSize(16777215, 60))
        self.frame_cstmr_address.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_address.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_cstmr_address)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_cstmr_address)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.label_5.setIndent(3)

        self.verticalLayout_8.addWidget(self.label_5)

        self.frame_cstmr_address_input = QFrame(self.frame_cstmr_address)
        self.frame_cstmr_address_input.setObjectName(u"frame_cstmr_address_input")
        self.frame_cstmr_address_input.setMinimumSize(QSize(0, 30))
        self.frame_cstmr_address_input.setMaximumSize(QSize(16777215, 30))
        self.frame_cstmr_address_input.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_address_input.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_address_input = QVBoxLayout(self.frame_cstmr_address_input)
        self.layout_cstmr_address_input.setSpacing(0)
        self.layout_cstmr_address_input.setObjectName(u"layout_cstmr_address_input")
        self.layout_cstmr_address_input.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_cstmr_address_input)


        self.verticalLayout_4.addWidget(self.frame_cstmr_address)

        self.frame_cstmr_info = QFrame(self.frame_prop)
        self.frame_cstmr_info.setObjectName(u"frame_cstmr_info")
        self.frame_cstmr_info.setMaximumSize(QSize(16777215, 60))
        self.frame_cstmr_info.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_cstmr_info)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_cstmr_info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setStyleSheet(u"font: 11pt \"Ubuntu\";")
        self.label_6.setIndent(3)

        self.verticalLayout_9.addWidget(self.label_6)

        self.frame_cstmr_info_input = QFrame(self.frame_cstmr_info)
        self.frame_cstmr_info_input.setObjectName(u"frame_cstmr_info_input")
        self.frame_cstmr_info_input.setMinimumSize(QSize(0, 30))
        self.frame_cstmr_info_input.setMaximumSize(QSize(16777215, 30))
        self.frame_cstmr_info_input.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_info_input.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_info_input = QVBoxLayout(self.frame_cstmr_info_input)
        self.layout_cstmr_info_input.setSpacing(0)
        self.layout_cstmr_info_input.setObjectName(u"layout_cstmr_info_input")
        self.layout_cstmr_info_input.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.frame_cstmr_info_input)


        self.verticalLayout_4.addWidget(self.frame_cstmr_info)


        self.verticalLayout_3.addWidget(self.frame_prop, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_cstmr_btn_edit = QFrame(self.menu_1)
        self.frame_cstmr_btn_edit.setObjectName(u"frame_cstmr_btn_edit")
        self.frame_cstmr_btn_edit.setMaximumSize(QSize(16777215, 36))
        self.frame_cstmr_btn_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_cstmr_btn_edit.setFrameShadow(QFrame.Raised)
        self.layout_cstmr_btn_edit = QVBoxLayout(self.frame_cstmr_btn_edit)
        self.layout_cstmr_btn_edit.setSpacing(0)
        self.layout_cstmr_btn_edit.setObjectName(u"layout_cstmr_btn_edit")
        self.layout_cstmr_btn_edit.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_cstmr_btn_edit)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("RightColumn", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("RightColumn", u"Address:", None))
        self.label_6.setText(QCoreApplication.translate("RightColumn", u"Info:", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

