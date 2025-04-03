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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QWidget)

class Ui_Console(object):
    def setupUi(self, Console):
        if not Console.objectName():
            Console.setObjectName(u"Console")
        Console.resize(400, 100)
        self.gridLayout = QGridLayout(Console)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Console_2 = QLabel(Console)
        self.Console_2.setObjectName(u"Console_2")

        self.gridLayout.addWidget(self.Console_2, 0, 0, 1, 1)

        self.Close = QDialogButtonBox(Console)
        self.Close.setObjectName(u"Close")
        self.Close.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        self.Close.setCenterButtons(True)

        self.gridLayout.addWidget(self.Close, 1, 0, 1, 1)


        self.retranslateUi(Console)

        QMetaObject.connectSlotsByName(Console)
    # setupUi

    def retranslateUi(self, Console):
        Console.setWindowTitle(QCoreApplication.translate("Console", u"Console", None))
        self.Console_2.setText(QCoreApplication.translate("Console", u"Initializing, please wait", None))
    # retranslateUi