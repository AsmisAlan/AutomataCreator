# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:09:27 2016

@author: alan
"""

class Automata():
    
    def __init__(self):
        self.__elementos = ["a","b","c"]
        self.__estados = []
        self.__finales = []
        self.__inicial = None
        self.__transiciones = {}
    
        
    def addElemento(self,elemento):
        self.__elementos.append(elemento)
    
    def addEstado(self,estado):
        self.__estados.append(estado)
    
    def addFinal(self,final):
        self.__finales.append(final)
    
    def setInicial(self,inicial):
        self.__inicial = inicial
    
    def addTransiciones(self,ID,transcicion,ID2):
        self.__transiciones[ID,transcicion] = ID2
        
        
    def esValida(self,cadena):
        estado = self.__inicial
        for a in cadena:
            if(a in self.__elementos):
                estado = self.__transiciones[estado,a]
            else:
                pass
                #estado = self.estadomuerto
        return True if(estado in self.__finales) else False
        
