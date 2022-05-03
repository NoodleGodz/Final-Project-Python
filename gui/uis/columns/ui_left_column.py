# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_column.ui'
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
    QSizePolicy, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(239, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_label_one = QFrame(self.menu_1)
        self.frame_label_one.setObjectName(u"frame_label_one")
        self.frame_label_one.setMaximumSize(QSize(16777215, 30))
        self.frame_label_one.setFrameShape(QFrame.NoFrame)
        self.frame_label_one.setFrameShadow(QFrame.Raised)
        self.layout_label_one = QVBoxLayout(self.frame_label_one)
        self.layout_label_one.setSpacing(0)
        self.layout_label_one.setObjectName(u"layout_label_one")
        self.layout_label_one.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_label_one)

        self.frame_button_one = QFrame(self.menu_1)
        self.frame_button_one.setObjectName(u"frame_button_one")
        self.frame_button_one.setMaximumSize(QSize(16777215, 30))
        self.frame_button_one.setFrameShape(QFrame.NoFrame)
        self.frame_button_one.setFrameShadow(QFrame.Raised)
        self.layout_button_one = QVBoxLayout(self.frame_button_one)
        self.layout_button_one.setSpacing(0)
        self.layout_button_one.setObjectName(u"layout_button_one")
        self.layout_button_one.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_button_one)

        self.paddingFrame = QFrame(self.menu_1)
        self.paddingFrame.setObjectName(u"paddingFrame")
        self.paddingFrame.setFrameShape(QFrame.NoFrame)
        self.paddingFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.paddingFrame)

        self.frame_motd = QFrame(self.menu_1)
        self.frame_motd.setObjectName(u"frame_motd")
        self.frame_motd.setMaximumSize(QSize(16777215, 30))
        self.frame_motd.setFrameShape(QFrame.NoFrame)
        self.frame_motd.setFrameShadow(QFrame.Sunken)
        self.layout_motd = QHBoxLayout(self.frame_motd)
        self.layout_motd.setSpacing(6)
        self.layout_motd.setObjectName(u"layout_motd")
        self.layout_motd.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_motd)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 16pt \"Ubuntu\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.textBrowser = QTextBrowser(self.menu_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setLineWrapColumnOrWidth(0)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"<html><head/><body><p><span style=\" font-weight:700; color:#e06c75;\">E.M.C.P. v1.0.0</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("LeftColumn", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#e06c75; background-color:#282c34;\">Energy Management Control Panel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#282c34;\">~ A project from Advanced Programming with Python, Group X ~</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#e06c75; backgrou"
                        "nd-color:#282c34;\">License Info</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#282c34;\">This is free and unencumbered software released into the public domain.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#282c34;\">Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means. In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetu"
                        "ity of all present and future rights to this software under copyright law.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#282c34;\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#282c34;\">IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</span></p></body></html>", None))
    # retranslateUi

