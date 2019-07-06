'''
Created on 29 giu 2019

@author: paola
'''


class Nodo:
    coordX = 0
    coordY = 0
    linehaul = 0
    backhaul = 0
    indice = 0

    def __init__(self):
        pass
    """
    def __init__(self, coordX, coordY, linehaul, backhaul,indice):
        self.coordX = coordX
        self.coordY = coordY
        self.linehaul = linehaul
        self.backhaul = backhaul
        self.indice = indice
    """
    def setCoordX(self,coordX):
        self.coordX = coordX

    def setCoordY(self,coordY):
        self.coordY = coordY

    def setLinehaul(self,linehaul):
        self.linehaul = linehaul

    def setBackhaul(self,backhaul):
        self.backhaul = backhaul

    def setIndice(self,indice):
        self.indice = indice

    def getCoordX(self):
        return self.coordX

    def getCoordY(self):
        return self.coordY

    def getLinehaul(self):
        return self.linehaul

    def getBackhaul(self):
        return self.backhaul

    def getIndice(self):
        return self.indice