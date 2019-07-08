'''
Created on 29 giu 2019

@author: paola
'''


class Rotta():
    caricoAttuale = 0
    nodi = []
    indiciNodi = []

    def __init__(self, capacita, Nodo):
        self.caricoAttuale = capacita
        self.capacitaCamion = capacita
        self.nodi.append(Nodo)
        self.indiciNodi.append(Nodo.getIndice())


    def appendiNodoLinehaul(self,Nodo):
        if Nodo.getLinehaul() > 0 and self.caricoAttuale > Nodo.getLinehaul() and self.caricoAttuale - Nodo.getLinehaul() > 0:
            self.nodi.append(Nodo)
            self.caricoAttuale = self.caricoAttuale - Nodo.getLinehaul()
            self.appendIndiceNodo(Nodo.getIndice())
            return True

        return False

    def appendiNodoBackhaul(self, Nodo):

        if Nodo.getBackhaul() > 0 and self.caricoAttuale + Nodo.getBackhaul() < self.capacitaCamion:
            self.nodi.append(Nodo)
            self.caricoAttuale = self.caricoAttuale + Nodo.getBackhaul()
            self.appendIndiceNodo(Nodo.getIndice())
            return True

        return False

    def removeDuplicate(self):
        unique = []
        for item in self.nodi:
            if item not in unique:
                unique.append(item)
        return unique

    def getIndiciNodi(self):
        return self.indiciNodi

    def appendIndiceNodo(self, indice):
        self.indiciNodi.append(indice)

    