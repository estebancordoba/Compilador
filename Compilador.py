#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyuic4 interfazCompilador.ui -o interfazCompilador.py

import sys
from PyQt4 import QtCore, QtGui

from interfazCompilador import *

ui_interfaz = Ui_compilador()


class interfazCompilador(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        ui_interfaz.setupUi(self)

        QtCore.QObject.connect(ui_interfaz.botonCompilar, QtCore.SIGNAL("clicked()"), self.eventoCompilar)

    def eventoCompilar(self):
        self.cadenaPrincipal = ui_interfaz.textEditar.toPlainText()#Obtiene el texto a compilar
        self.cadenaLineas = self.cadenaPrincipal.split('\n')#Separa el texto por lineas
        #if (self.cadenaLineas[0]=="INICIO" and self.cadenaLineas[self.cadenaLineas.__len__()-1]=="FIN"):#Verifica si inicio y fin estan bien
         #   del self.cadenaLineas[0]
          #  del self.cadenaLineas[self.cadenaLineas.__len__()-1]
        if (True):
            for i in range(self.cadenaLineas.__len__()):
                self.cadenaPalabras = self.cadenaLineas[i].split(' ')#Separa el texto por palabras

                if self.cadenaPalabras[0]=="pr":
                    cadenaPara=[]
                    cadenaPara.append(self.cadenaPalabras)
                    inicioPara=i
                    i+=1
                    while i < self.cadenaLineas.__len__():
                        cadenaFinPara=self.cadenaLineas[i].split(' ')
                        if(cadenaFinPara[0]=="f_pr"):
                            cadenaPara.append(cadenaFinPara)
                            return self.eventoPara(cadenaPara)
                        else:
                           cadenaPara.append(cadenaFinPara)
                        i += 1

        else:
            ui_interfaz.textErrores.setText("Error de Sintaxis (Se debe dar un INCIO y un FIN)")

    def eventoPara(self, cadenaPara):
        for i in cadenaPara:
            print(i)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = interfazCompilador()
    myapp.setFixedSize(800, 600)
    myapp.show()
    sys.exit(app.exec_())
