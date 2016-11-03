# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:14:06 2016

@author: alan
"""


from PyQt4 import QtGui, uic

    
plantilla = uic.loadUiType("Element.ui")[0]
class Element(QtGui.QDialog,plantilla):
    
    def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
    
    def getText(self):
        return self.editElement.text()