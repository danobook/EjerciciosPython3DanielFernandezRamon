# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfacegrafica.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(306, 486)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Estudiante = QGroupBox(self.centralwidget)
        self.Estudiante.setObjectName(u"Estudiante")
        self.Estudiante.setGeometry(QRect(0, 30, 281, 271))
        self.verticalLayoutWidget_6 = QWidget(self.Estudiante)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 16, 251, 165))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.verticalLayoutWidget_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nombre = QLineEdit(self.verticalLayoutWidget_6)
        self.nombre.setObjectName(u"nombre")

        self.verticalLayout_5.addWidget(self.nombre)

        self.correo = QLineEdit(self.verticalLayoutWidget_6)
        self.correo.setObjectName(u"correo")

        self.verticalLayout_5.addWidget(self.correo)

        self.contrasena = QLineEdit(self.verticalLayoutWidget_6)
        self.contrasena.setObjectName(u"contrasena")

        self.verticalLayout_5.addWidget(self.contrasena)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.Registro = QPushButton(self.verticalLayoutWidget_6)
        self.Registro.setObjectName(u"Registro")

        self.verticalLayout_6.addWidget(self.Registro)

        self.pushButton_2 = QPushButton(self.Estudiante)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 190, 249, 23))
        self.pushButton_3 = QPushButton(self.Estudiante)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 220, 249, 23))
        self.Archivo = QGroupBox(self.centralwidget)
        self.Archivo.setObjectName(u"Archivo")
        self.Archivo.setGeometry(QRect(0, 310, 281, 131))
        self.textBrowser = QTextBrowser(self.Archivo)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 20, 241, 101))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tarea5", None))
#if QT_CONFIG(accessibility)
        self.centralwidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.Estudiante.setTitle(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None))
        self.Registro.setText(QCoreApplication.translate("MainWindow", u"IngresarDatos", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MostrsrDatos", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"EliminarDatos", None))
        self.Archivo.setTitle(QCoreApplication.translate("MainWindow", u"Mensajes", None))
    # retranslateUi

