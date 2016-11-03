# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 23:33:41 2016

@author: alan
"""
import constantes
from PyQt4 import QtGui ,QtCore



#crear una variable tam que sea gloval para todos los nodos ???
tamanio = 50

class Nodo():
    
    def __init__(self,ID,esFinal,padre = None,posx = 0, posy = 0,ini = False):
        
        self.id = ID
        #label.setStyleSheet("background-image: url(:/1.png);")
        #label.setText("text") 
        self.inicial = ini
        self.tam = tamanio
        #print(tamanio)
        self.grafica = QtGui.QLabel(str(ID), padre)
        if self.inicial:
            imagen = QtGui.QPixmap(constantes.inicial,'png')
        else:
            imagen = QtGui.QPixmap(constantes.final,'png') if esFinal else QtGui.QPixmap(constantes.nodo ,'png')
        self.esFinal = esFinal
        self.grafica.setPixmap(imagen)
        self.grafica.setGeometry(posx,posy,self.tam,self.tam)
        #self.grafica.setStyleSheet("QWidget#Form {background-image: url("+constantes.nodo+".jpg);}")
        self.grafica.setScaledContents(True)
        self.grafica.show()
        self.entradas = []
        self.salidas = []
        
    
    def cambiarEstado(self):
        self.esFinal = not self.esFinal
        if self.inicial:
            if self.esFinal:
                imagen = QtGui.QPixmap(constantes.inicialFinal,'png')  
            else:
                QtGui.QPixmap(constantes.inicial,'png')
        else:
            if self.esFinal:
                imagen = QtGui.QPixmap(constantes.final,'png')  
            else:
                QtGui.QPixmap(constantes.nodo ,'png')
        self.grafica.setPixmap(imagen)
    
    def getEstado(self):
        return self.esFinal
    
    def addEntrada(self,ID):
        self.entradas.append(ID)
    
    def addSalida(self,ID):
        self.salidas.append(ID)
        
    def getSalidas(self):
        return self.salidas
    
    def getEntradas(self):
        return self.entradas
    
    def setID (self,ID):
        self.id = ID
        self.grafica.setText(ID)
    
    def getID (self):
        return self.id
        
    def modPos(self,x , y):
        self.grafica.move(QtCore.QPoint(x,y))
        
    def getPos(self):
        return self.grafica.pos()
    
    def getX(self):
        return self.grafica.x()
    
    def getY(self):
        return self.grafica.y()
    
    def getXMid(self):
        return self.getX() + (self.tam // 2)
    
    def getYMid(self):
        return self.getY() + (self.tam // 2)
    
    def getXFinal(self):
        return self.grafica.x() + self.tam
    
    def getYFinalMid(self):
        return self.grafica.y() + (self.tam // 2)
    
    def setTam(self,tam):
        tamanio = tam
        self.tam = tam
        self.grafica.setGeometry(self.getX(),self.getY(),self.tam,self.tam)
    
    def aumentarGrafica(self):
        self.setTam(self.tam + 10)
    
    def decrementarGrafica(self):
        self.setTam(self.tam - 10)
    
    def select(self):
        self.grafica.setGeometry(self.getX(),self.getY(),self.tam+10,self.tam+10)
    
    def notSelect(self):
        self.grafica.setGeometry(self.getX(),self.getY(),self.tam,self.tam)
    
    def sobre(self,x,y):
        value = False
        if (self.getX() <= x and self.getX() +self.tam >= x):
            if(self.getY() <= y and self.getY() +self.tam >= y):
                value = True
        return value