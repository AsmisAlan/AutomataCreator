# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:51:28 2016

@author: alan
"""
from PyQt4 import QtGui
class TableManager():
    
    def __init__(self,table,headers = []):
        self.table = table
        self.headersList= headers
    
    
    
    def addList(self,listData):
        """add tableWidget Item line to your QtalbeWidget"""
        self.table.insertRow(self.table.rowCount())
        colum = 0
        row = self.table.rowCount()
        for data in listData:
            self.table.setItem(row-1,colum,QtGui.QTableWidgetItem(str(data)))
            colum+=1
            
    def addItem(self,item,col = 0):
        """add tableWidget Item line to your QtalbeWidget"""
        self.table.insertRow(self.table.rowCount())
        row = self.table.rowCount()
        self.table.setItem(row-1,col,QtGui.QTableWidgetItem(str(item)))
    
        
    def resetTable(self):
        """clear all the QtableWidgetItem of the table"""
        self.table.clear()
        self.table.setRowCount(0)
        pos = 0
        for header in  self.headersList:
            self.table.setHorizontalHeaderItem(pos,QtGui.QTableWidgetItem(str(header)))
            pos +=1