#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyuic4 interfazCompilador.ui -o interfazCompilador.py

import sys
from warnings import catch_warnings
from weakref import finalize
from PyQt4 import QtCore, QtGui

from interfazCompilador import *

ui_interfaz = Ui_compilador()


class interfazCompilador(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        ui_interfaz.setupUi(self)

        QtCore.QObject.connect(ui_interfaz.botonCompilar, QtCore.SIGNAL("clicked()"), self.eventoCompilar)

        self.recorridoLineas=0
        self.recorridoLineasOtro=0

        self.compilo=False

        self.numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.operadores = ['+', '-', '*', '/']
        self.caracteres = [",", "¡", "<", ">", "", "&", "."]
        self.letras = ["I", "N", "C", "O", "F", "M",
                       "P", "T", "R", "m", "y", "n",
                       "f", "r", "s", "i", "p", "d", "f", "e"]
        self.palabrasClave = ['mtr', 'si', 'sn', 'pr',
                              'ent', 'rea', 'imp', 'etr',
                              'may', 'men', 'dif', 'es',
                              'my', 'mn']
        self.variables = ['v1', 'v2', 'v3', 'v4',
                          'v5', 'v6', 'v7', 'v8', 'v9']

        self.finales = ['f_pr']

    def eventoCompilar(self):
        self.cadenaPrincipal = ui_interfaz.textEditar.toPlainText()#Obtiene el texto a compilar
        self.cadenaPrincipal=self.cadenaPrincipal.replace('.','.\n')#reemplazar el . por un . y un espacio para mejor manejo
        self.cadenaLineas = self.cadenaPrincipal.splitlines()#Separa el texto por lineas

        contEspacios=0
        while(contEspacios<self.cadenaLineas.__len__()):#Quitar espacios espacios sobrantes
            if self.cadenaLineas[contEspacios] == "":
                self.cadenaLineas.pop(contEspacios)
                contEspacios-=1
            else:
                contEspacios+=1

        if (self.cadenaLineas[0]=="INICIO" and self.cadenaLineas[self.cadenaLineas.__len__()-1]=="FIN"):#Verifica si inicio y fin estan bien
            #del self.cadenaLineas[0]
            #del self.cadenaLineas[self.cadenaLineas.__len__()-1]
        #if (True):#activar para probar sin INICIO y sin FIN
            self.recorridoLineas=1
            while self.recorridoLineas<self.cadenaLineas.__len__():
                self.cadenaPalabras = self.cadenaLineas[self.recorridoLineas].split(' ')#Separa el texto por palabras

                contEspacios=0
                while(contEspacios<self.cadenaPalabras.__len__()):#Quitar espacios espacios sobrantes
                    if self.cadenaPalabras[contEspacios] == "":
                        self.cadenaPalabras.pop(contEspacios)
                        contEspacios-=1
                    else:
                        contEspacios+=1
                if self.cadenaPalabras[0]=="FIN":
                    if self.compilo==True:
                        ui_interfaz.textErrores.setText("Compilo sin problemas :)")
                    return

                if self.cadenaPalabras[self.cadenaPalabras.__len__()-1] != '.':
                    ui_interfaz.textErrores.setText("Error de Sintaxis (Falta . al final de la linea )"+str(self.recorridoLineas))
                    self.compilo=False
                    return

                if ((self.cadenaPalabras[0] in self.finales) == True):
                    ui_interfaz.textErrores.setText("Existe un cierre de mas")
                    self.compilo=False
                    return

                if self.cadenaPalabras[0]=="pr":
                    if (self.eventoPara(self.envBloques("pr"))==True):
                        self.compilo=True
                    else:
                        return False

                ##########################################################
                # Aqui agregar la condicion para cada uno de los metodos #
                ##########################################################

                self.recorridoLineas+=1

        else:
            ui_interfaz.textErrores.setText("Error de Sintaxis (Se debe dar un INCIO y un FIN)")
            self.compilo=False

    def envBloques(self, funcion):#Metodo para enviar bloques de cada funcion
        cadenaBloque=[]
        cadenaFinBloque=self.cadenaLineas[self.recorridoLineas].split(' ')
        cadenaBloque.append(cadenaFinBloque)
        finalCade="f_"+funcion

        contRep= - 1

        while self.recorridoLineas < self.cadenaLineas.__len__():
            cadenaFinBloque=self.cadenaLineas[self.recorridoLineas].split(' ')

            contEspacios=0
            while(contEspacios<cadenaFinBloque.__len__()-1):#Quitar espacios espacios sobrantes
                if cadenaFinBloque[contEspacios] == "":
                    cadenaFinBloque.pop(contEspacios)
                    contEspacios-=1
                else:
                    contEspacios+=1

            if self.cadenaLineas[self.recorridoLineas]=="FIN":
                cadenaBloque.pop(0)
                ui_interfaz.textErrores.setText("Error de Sintaxis (Falta "+str(finalCade)+" al final de un bloque "+str(funcion)+")")
                self.compilo=False
                return cadenaBloque

            if cadenaFinBloque[0]==funcion:
                contRep+=1

            if cadenaFinBloque[cadenaFinBloque.__len__()-1] != '.':
                cadenaBloque.pop(0)
                ui_interfaz.textErrores.setText("Error de Sintaxis (Falta . al final de la linea )"+str(self.recorridoLineas))
                self.compilo=False
                return cadenaBloque

            if(cadenaFinBloque[0]==finalCade and contRep==0):
                if (cadenaFinBloque[1]!='.' or cadenaFinBloque.__len__()>2):
                    cadenaBloque.pop(0)
                    ui_interfaz.textErrores.setText("Error de Sintaxis (El final para "+str(funcion)+" no corresponde")
                    self.compilo=False
                    return cadenaBloque
                cadenaBloque.append(cadenaFinBloque)
                cadenaBloque.pop(0)
                ui_interfaz.textErrores.clear()
                self.compilo=True
                return cadenaBloque

            else:
                if contRep>0 and cadenaFinBloque[0]==finalCade:
                    contRep-=1
                    if (cadenaFinBloque[1]!='.' or cadenaFinBloque.__len__()>2):
                        cadenaBloque.pop(0)
                        ui_interfaz.textErrores.setText("Error de Sintaxis (El final para "+str(funcion)+" no corresponde")
                        self.compilo=False
                        return cadenaBloque
                cadenaBloque.append(cadenaFinBloque)
            self.recorridoLineas += 1


    def eventoPara(self, cadenaPara):
        if self.compilo == True:
            # pr < v1 = 0 , 5 , + 1 > .
            print("<------------------------------------------------->")

            for i in cadenaPara:
                print(i)


            if (cadenaPara[0][0]=="pr"):
                if (cadenaPara[0][1]=="<"):
                    if ((cadenaPara[0][2] in self.variables)==True):
                        if (cadenaPara[0][3]=="="):
                            if ((cadenaPara[0][4] in self.numeros)==True):
                                if (cadenaPara[0][5]==","):
                                    if ((cadenaPara[0][6] in self.numeros)==True):
                                        if (cadenaPara[0][7]==","):
                                            if (cadenaPara[0][8]=="+" or cadenaPara[0][8]=="-"):
                                                if ((cadenaPara[0][9] in self.numeros)==True):
                                                    if (cadenaPara[0][10]==">"):
                                                        if (cadenaPara[0][11]=="."):
                                                            self.compilo = True
                                                        else:
                                                            self.compilo = False
                                                    else:
                                                        self.compilo = False
                                                else:
                                                    self.compilo = False
                                            else:
                                                self.compilo = False
                                        else:
                                            self.compilo = False
                                    else:
                                        self.compilo = False
                                else:
                                    self.compilo = False
                            else:
                                self.compilo = False
                        else:
                            self.compilo = False
                    else:
                        self.compilo = False
                else:
                    self.compilo = False
            else:
                self.compilo = False

            if self.compilo == True:

                self.recorridoLineasOtro=1
                while self.recorridoLineasOtro<cadenaPara.__len__()-1:

                    if cadenaPara[self.recorridoLineasOtro][0]=="pr":
                        if (self.eventoPara(self.enviarOtroBloque("pr", cadenaPara))==True):
                            return True
                        else:
                            return False
                    ##########################################################
                    # Aqui agregar la condicion para cada uno de los metodos #
                    ##########################################################

                    self.recorridoLineasOtro+=1
                return True


            else:
                ui_interfaz.textErrores.setText("Error, la gramatica de pr no consiste")

                return False


    def enviarOtroBloque(self, funcion, cadenaOtra):

        finalCade="f_"+funcion
        cadenaFinal=[]
        contRep= - 1

        self.compilo=False

        while(self.recorridoLineasOtro<cadenaOtra.__len__()-1):

            if cadenaOtra[self.recorridoLineasOtro][0] == funcion:
                contRep+=1
            if(cadenaOtra[self.recorridoLineasOtro][0]==finalCade and contRep==0):
                cadenaFinal.append(cadenaOtra[self.recorridoLineasOtro])
                ui_interfaz.textErrores.clear()
                self.compilo=True
                return cadenaFinal

            else:
                if contRep>0 and cadenaOtra[self.recorridoLineasOtro][0]==finalCade:
                    contRep-=1
                cadenaFinal.append(cadenaOtra[self.recorridoLineasOtro])

            self.recorridoLineasOtro+=1

    #############################################################
    # Aqui agregar los metodos para cada uno de las condiciones #
    #############################################################

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = interfazCompilador()
    myapp.setFixedSize(800, 600)
    myapp.show()
    sys.exit(app.exec_())
