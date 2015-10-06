# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazCompilador.ui'
#
# Created: Mon Oct  5 22:22:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_compilador(object):
    def setupUi(self, compilador):
        compilador.setObjectName(_fromUtf8("compilador"))
        compilador.resize(800, 600)
        compilador.setAutoFillBackground(False)
        self.textEditar = QtGui.QTextEdit(compilador)
        self.textEditar.setGeometry(QtCore.QRect(10, 10, 781, 351))
        self.textEditar.setObjectName(_fromUtf8("textEditar"))
        self.textErrores = QtGui.QTextEdit(compilador)
        self.textErrores.setEnabled(False)
        self.textErrores.setGeometry(QtCore.QRect(10, 380, 781, 141))
        self.textErrores.setObjectName(_fromUtf8("textErrores"))
        self.botonCompilar = QtGui.QPushButton(compilador)
        self.botonCompilar.setGeometry(QtCore.QRect(10, 530, 141, 51))
        self.botonCompilar.setObjectName(_fromUtf8("botonCompilar"))
        self.botonCancelar = QtGui.QPushButton(compilador)
        self.botonCancelar.setGeometry(QtCore.QRect(650, 530, 141, 51))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))

        self.retranslateUi(compilador)
        QtCore.QObject.connect(self.botonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), compilador.close)
        QtCore.QMetaObject.connectSlotsByName(compilador)

    def retranslateUi(self, compilador):
        compilador.setWindowTitle(_translate("compilador", "Compilador", None))
        self.botonCompilar.setText(_translate("compilador", "Compilar", None))
        self.botonCancelar.setText(_translate("compilador", "Cancelar", None))
