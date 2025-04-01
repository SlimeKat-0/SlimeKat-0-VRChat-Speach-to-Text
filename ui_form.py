# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(324, 180)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ip = QLineEdit(Widget)
        self.ip.setObjectName(u"ip")
        self.ip.setMaxLength(15)

        self.gridLayout.addWidget(self.ip, 0, 1, 1, 1)

        self.port = QLineEdit(Widget)
        self.port.setObjectName(u"port")
        self.port.setMaxLength(5)

        self.gridLayout.addWidget(self.port, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.connect = QPushButton(Widget)
        self.connect.setObjectName(u"connect")

        self.gridLayout.addWidget(self.connect, 2, 2, 1, 1)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"VRChat STT", None))
#if QT_CONFIG(whatsthis)
        Widget.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("Widget", u"                     IP:", None))
        self.ip.setText(QCoreApplication.translate("Widget", u"127.0.0.1", None))
        self.port.setText(QCoreApplication.translate("Widget", u"9000", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Exit", None))
        self.connect.setText(QCoreApplication.translate("Widget", u"Connect", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"                 Port:", None))
    # retranslateUi

