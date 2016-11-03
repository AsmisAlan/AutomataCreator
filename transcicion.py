# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:03:36 2016

@author: alan
"""
from PyQt4 import QtGui, QtCore

class Transicion():
    
    def __init__(self,x,y):
        self.IDInicial = None
        self.IDFinal = None
        self.simbol = []
        self.x = x
        self.y = y
        self.xFinal = x
        self.yFinal = y
        self.trazo = None
        self.element = None
        self.element = QtGui.QLabel()
        
    def setElement(self,txt,padre):
        self.element = QtGui.QLabel(padre)
        self.element.show()
        self.element.setText(txt)
        self.element.move(QtCore.QPoint(self.x+(self.xFinal-self.x)//2,self.y))
    
    def getElement(self):
        return self.element.text()
        
    def getIds(self):
        return self.IDInicial , self.IDFinal
    
    def setEstadoInicial(self,ID):
        self.IDInicial = ID
        
    def setEstadoFinal(self,ID):
        self.IDFinal = ID
        
    def setFinalPos(self,x,y):
        self.xFinal = x
        self.yFinal = y
        self.element.move(QtCore.QPoint(self.x+(self.xFinal-self.x)//2,self.y))
        
    def setInicialPos(self,x,y):
        self.x = x
        self.y = y
        self.element.move(QtCore.QPoint(self.x+(self.xFinal-self.x)//2,self.y))
        
    def startConecction(self,posValida):
        if posValida: 
            self.trazo = QtGui.QPen(QtCore.Qt.green, 2, QtCore.Qt.DashLine)
        else:
            self.trazo = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.DashLine)
    
    def establecido(self):
        self.trazo = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        
        
    def drawSelection(self, paint):
        paint.setPen(self.trazo)
        if self.IDInicial == self.IDFinal:
            self.bucle(paint)
        elif self.x > self.xFinal: 
            self.curva(self.xFinal ,self.yFinal,self.x -50,self.y,-40,paint)
        else:
            self.curva(self.x,self.y,self.xFinal,self.yFinal,40,paint)
        
    def draw(self, paint):
        paint.setPen(self.trazo)
        if self.IDInicial == self.IDFinal:
            self.bucle(paint)
        elif self.x > self.xFinal: 
            #self.curva(self.xFinal + 50,self.yFinal,self.x -50,self.y,-40,paint)
            self.curva(self.x -50,self.y,self.xFinal + 50,self.yFinal,-40,paint)
        else:
            self.curva(self.x,self.y,self.xFinal,self.yFinal,40,paint)
            
        
    def curva(self,x,y,xf,yf,onda,paint):
        """
        if (self.yFinal - self.y) < 5 or (self.yFinal - self.y) > -5:
            paint.drawLine(self.x, self.y, self.xFinal,self.yFinal)"""
        path=QtGui.QPainterPath(QtCore.QPointF(x, y)) #Punto de inicio
        centro = (xf - x)//2 + x  #busca el centro entre los nodos
        cc1 = QtCore.QPointF(centro, centro +onda)
        cc2 = QtCore.QPointF(centro, centro +onda)
        path.cubicTo(cc1, cc2, QtCore.QPointF(xf,yf))
        paint.drawPath(path)
        #esto esta en desarrollo 
        #self.flecha(path.angleAtPercent(0),paint)
        
    def flecha(self,angulo,paint):
        line1 = QtCore.QLineF()
        line2 = QtCore.QLineF()
        line1.setP1(QtCore.QPointF(self.xFinal,self.yFinal))
        line2.setP1(QtCore.QPointF(self.xFinal,self.yFinal))
        line1.setLength(30)
        line2.setLength(30)
        print(angulo," : ",angulo + 30,"  ",angulo-30)
        line1.setAngle(angulo + 30)
        line2.setAngle(angulo - 30)
        paint.drawLine(line1)
        paint.drawLine(line2)
        
    def bucle (self,paint):
        path=QtGui.QPainterPath(QtCore.QPointF(self.xFinal, self.yFinal)) #Punto de inicio
        #centro = (xf - x)//2 + x  #busca el centro entre los nodos
        cc1 = QtCore.QPointF(self.xFinal + (self.xFinal - self.x), self.yFinal - 100)
        cc2 = QtCore.QPointF(self.xFinal - (self.xFinal - self.x), self.yFinal - 100)
        path.cubicTo(cc1, cc2, QtCore.QPointF(self.xFinal,self.yFinal))
        paint.drawPath(path)
            
            
        