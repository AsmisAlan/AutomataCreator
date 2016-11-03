# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:36:26 2016

@author: alan
"""

import sys
from  TableManager import  TableManager
import Element
import Automata
import nodo
import constantes
import transcicion
from PyQt4 import QtGui, uic

    
plantilla = uic.loadUiType("Menu.ui")[0]
class Menu(QtGui.QMainWindow,plantilla):
    
    def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
         self.TablaTransiciones = TableManager(self.TablaTransiciones,[])
         self.tablaEstadosFinales = TableManager(self.tablaEstadosFinales,["ESTADO FINAL"])
         self.tablaSaliente = TableManager(self.tablaSaliente,["ELEMENTO","ESTADO"])
         self.tablaEntrante = TableManager(self.tablaEntrante,["ESTADO","ELEMENTO"])
         self.selected = None #????????
         self.transicion = None #???????????
         self.diccionarioEstado = {}
         self.diccionarioTransicion = {}  
         self.automata = Automata.Automata()
         self.crearInicial()
         self.estadoMode()
         self.checkLabel.setPixmap(QtGui.QPixmap(constantes.Check,'png'))
         self.cadenaEdit.textChanged.connect(self.validar)
         self.nuevoEstado.clicked.connect(self.addEstado)
         self.nuevoFinal.clicked.connect(self.addFinal)
         self.botonTransicion.clicked.connect(self.transicionMode)
         self.botonEstado.clicked.connect(self.estadoMode)
         self.botonZoomMas.clicked.connect(self.zoomMas)
         self.botonZoomMenos.clicked.connect(self.zoomMenos)
         
    def zoomMas(self):
        for ID in self.diccionarioEstado.keys():
            self.diccionarioEstado[ID].aumentarGrafica()
            self.resetPosLines(self.diccionarioEstado[ID])
            #self.update
        
    def zoomMenos (self):
        for ID in self.diccionarioEstado.keys():
            self.diccionarioEstado[ID].decrementarGrafica()
            self.resetPosLines(self.diccionarioEstado[ID])
            #self.update
         
    def transicionMode(self):
        #self.botonTranscicion.setText("Modo Normal")
        #self.mode = not self.mode
        self.pressMode = self.transicionModePress
        self.releaseMode = self.transicionModeRelease
        self.moveMode = self.transicionModeMove
        #seteo el cursor QtGui.QCursor.
        
    def estadoMode(self):
        self.pressMode = self.estadoModePress
        self.releaseMode = self.estadoModeRelease
        self.moveMode = self.estadoModeMove
        
         
    def addEstado(self):
        ID = len(self.diccionarioEstado.keys())
        self.automata.addEstado(ID)
        self.diccionarioEstado[ID] = nodo.Nodo(ID,False,self.widgetAutomata)
    
    def addFinal(self):
        ID = len(self.diccionarioEstado.keys())
        self.automata.addEstado(ID)
        self.automata.addFinal(ID)
        self.diccionarioEstado[ID] = nodo.Nodo(ID,True,self.widgetAutomata)
        self.tablaEstadosFinales.addItem(ID)
    
    def validar(self):
        text = self.cadenaEdit.text()
        image = None
        if self.automata.esValida(text):
            image = QtGui.QPixmap(constantes.positiveCheck,'png')
        else:
            image = QtGui.QPixmap(constantes.negativeCheck,'png')
        self.checkLabel.setPixmap(image)
        
    def mousePressEvent(self, QMouseEvent):
        self.pressMode(QMouseEvent)
        
    def mouseMoveEvent(self,  QMouseEvent):
        self.moveMode(QMouseEvent)
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.releaseMode()
        
    """
            
    def mousePressEvent(self, QMouseEvent):
        for ID in self.diccionarioEstado.keys():
            if(self.diccionarioEstado[ID].sobre(QMouseEvent.x() - 20,QMouseEvent.y() - 80)):
                self.selected = self.diccionarioEstado[ID]
        if self.selected != None:
            if self.mode : 
                self.transcicion = transcicion.Transcicion(self.selected.getXFinal()+20,self.selected.getYFinalMid()+80)
                self.transcicion.setEstadoInicial(self.selected.getID())
                self.transcicion.startConecction(False)
            self.selected.select()
    
    def mouseMoveEvent(self,  QMouseEvent):
        if(self.transcicion != None):
            for ID in self.diccionarioEstado.keys():
                if(self.diccionarioEstado[ID].sobre(QMouseEvent.x() - 20,QMouseEvent.y() - 80)):
                    nodo = self.diccionarioEstado[ID]
                    self.transcicion.setFinalPos(nodo.getX()+20,nodo.getYMid()+80)
                    self.transcicion.startConecction(True)
                    self.transcicion.setEstadoFinal(ID)
                    break
                else:
                    self.transcicion.setFinalPos(QMouseEvent.x(),QMouseEvent.y())
                    self.transcicion.startConecction(False)
                    self.transcicion.setEstadoFinal(None)
            self.update()
        else:
            if (self.selected != None):
                if (QMouseEvent.x() -20 >= 0 and QMouseEvent.y() -80 >= 0):
                    self.selected.modPos(QMouseEvent.x() -20,QMouseEvent.y() -80) #camviar 
                    if (self.selected.getSalidas() != []):
                        for salida in self.selected.getSalidas():
                            self.diccionarioTranscicion[(self.selected.getID(),salida)].setInicialPos(self.selected.getXFinal()+20,self.selected.getYFinalMid()+80)
                        self.update()
                    if (self.selected.getEntradas() != []):
                        for entrada in self.selected.getEntradas():
                            self.diccionarioTranscicion[(entrada,self.selected.getID())].setFinalPos(self.selected.getX()+20,self.selected.getYMid()+80)
                        self.update()
    
    def mouseReleaseEvent(self, QMouseEvent):
        if (self.selected != None):
            self.selected.notSelect()
            self.selected = None
        if(self.transcicion != None):
            if(self.transcicion.getIds()[1] != None):
                self.transcicion.establecido()
                ids = self.transcicion.getIds()
                self.e = Element.Element(self)
                self.e.show()
                self.e.exec()
                self.diccionarioTransicion[ids] = self.transicion
                self.transicion.setElemnt(self.e.getText(),self)
                self.automata.addElemento(self.e.getText())
                self.automata.addTransciciones(ids[0],self.e.getText(),ids[1])
                self.diccionarioEstado[ids[0]].addSalida(ids[1])
                self.diccionarioEstado[ids[1]].addEntrada(ids[0])
                self.transcicion = None
            else:
                self.transcicion = None
            self.update()
    """
            
    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setTransform
        self.drawTransiciones(painter)
        if self.transicion != None:
            self.transicion.drawSelection(painter)
        painter.end()
        
    def drawTransiciones(self,painter):
        #print(self.diccionarioTranscicion.keys())
        for ID in self.diccionarioTransicion.keys():
            self.diccionarioTransicion[ID].draw(painter)
    
    def crearInicial(self):
        self.automata.addEstado(0)
        self.automata.setInicial(0)
        self.diccionarioEstado[0] = nodo.Nodo(0,False,self.widgetAutomata,ini =True)
        
        
    #funciones creadas para mejorar el rendimiento del programa?
        
    def transicionModePress(self,QMouseEvent):
        for ID in self.diccionarioEstado.keys():
            if(self.diccionarioEstado[ID].sobre(QMouseEvent.x() - 20,QMouseEvent.y() - 80)):
                self.selected = self.diccionarioEstado[ID]
        if self.selected != None:
            self.transicion = transcicion.Transicion(self.selected.getXFinal()+20,self.selected.getYFinalMid()+80)
            self.transicion.setEstadoInicial(self.selected.getID())
            self.transicion.startConecction(False)
            self.selected.select()
    
    def estadoModePress(self,QMouseEvent):
        for ID in self.diccionarioEstado.keys():
            if(self.diccionarioEstado[ID].sobre(QMouseEvent.x() - 20,QMouseEvent.y() - 80)):
                self.selected = self.diccionarioEstado[ID]
        if self.selected != None:
            self.estadoDescripData(self.selected) #muestra la descripcion de los datos
            self.selected.select()
    
    def estadoDescripData(self,estado):
        self.labelEstado.setText("ESTADO ID : "+str(estado.getID()))
        self.tablaSaliente.resetTable()
        self.tablaEntrante.resetTable()
        if (estado.getEntradas() != []):
            for entrada in estado.getEntradas():
                self.tablaEntrante.addList([entrada,self.diccionarioTransicion[entrada,estado.getID()].getElement()])
        if (estado.getSalidas() != []):
            for salida in estado.getSalidas():
                self.tablaSaliente.addList([self.diccionarioTransicion[estado.getID(),salida].getElement(),salida])
       
    
    def transicionModeMove(self,QMouseEvent):
        if(self.transicion != None):
            for ID in self.diccionarioEstado.keys():
                if(self.diccionarioEstado[ID].sobre(QMouseEvent.x() - 20,QMouseEvent.y() - 80)):
                    nodo = self.diccionarioEstado[ID]
                    if self.transicion.IDInicial == ID:
                        self.transicion.setFinalPos(nodo.getXMid()+20,nodo.getY()+80)
                    else:
                        self.transicion.setFinalPos(nodo.getX()+20,nodo.getYMid()+80)
                    self.transicion.startConecction(True)
                    self.transicion.setEstadoFinal(ID)
                    break
                else:
                    self.transicion.setFinalPos(QMouseEvent.x(),QMouseEvent.y())
                    self.transicion.startConecction(False)
                    self.transicion.setEstadoFinal(None)
            self.update()
    
    def estadoModeMove(self,QMouseEvent):
        if (self.selected != None):
            if (QMouseEvent.x() -20 >= 0 and QMouseEvent.y() -80 >= 0):
                self.selected.modPos(QMouseEvent.x() -20,QMouseEvent.y() -80) #cambiar
                self.resetPosLines(self.selected)
                self.update()
                """if (self.selected.getSalidas() != []):
                    for salida in self.selected.getSalidas():
                        self.diccionarioTransicion[(self.selected.getID(),salida)].setInicialPos(self.selected.getXFinal()+20,self.selected.getYFinalMid()+80)
                    self.update() #???????????????
                if (self.selected.getEntradas() != []):
                    for entrada in self.selected.getEntradas():
                        self.diccionarioTransicion[(entrada,self.selected.getID())].setFinalPos(self.selected.getX()+20,self.selected.getYMid()+80)
                    self.update() #??????????????
                if self.selected.getID() in self.selected.getSalidas() or  self.selected.getID() in self.selected.getEntradas():
                    self.diccionarioTransicion[(self.selected.getID(),self.selected.getID())].setFinalPos(self.selected.getXMid()+20,self.selected.getY()+80)
                    self.update() #??????????????"""
                    
    def resetPosLines(self,estado):
        if (estado.getSalidas() != []):
            for salida in estado.getSalidas():
                self.diccionarioTransicion[(estado.getID(),salida)].setInicialPos(estado.getXFinal()+20,estado.getYFinalMid()+80)
                self.update() #???????????????
        if (estado.getEntradas() != []):
            for entrada in estado.getEntradas():
                self.diccionarioTransicion[(entrada,estado.getID())].setFinalPos(estado.getX()+20,estado.getYMid()+80)
            self.update() #??????????????
        if estado.getID() in estado.getSalidas() or  estado.getID() in estado.getEntradas():
            self.diccionarioTransicion[(estado.getID(),estado.getID())].setFinalPos(estado.getXMid()+20,estado.getY()+80)
            self.update() #??????????????
    
    def transicionModeRelease(self):
        if(self.transicion != None):
            self.selected.notSelect()
            self.selected = None
            if(self.transicion.getIds()[1] != None):
                self.transicion.establecido()
                ids = self.transicion.getIds()
                self.e = Element.Element(self)
                self.e.show()
                self.e.exec()
                self.diccionarioTransicion[ids] = self.transicion
                self.transicion.setElement(self.e.getText(),self)
                self.automata.addElemento(self.e.getText())
                self.automata.addTransiciones(ids[0],self.e.getText(),ids[1])
                self.TablaTransiciones.addList([ids[0],self.e.getText(),ids[1]])
                self.diccionarioEstado[ids[0]].addSalida(ids[1])
                self.diccionarioEstado[ids[1]].addEntrada(ids[0])
                self.transicion = None
            else:
                self.transicion = None
            self.update()
    
    def estadoModeRelease(self):
        if (self.selected != None):
            self.selected.notSelect()
            self.selected = None
            
    #funciones creadas para mejorar el rendimiento del programa?

app = QtGui.QApplication(sys.argv)
menu = Menu()
menu.show()
app.exec_()

