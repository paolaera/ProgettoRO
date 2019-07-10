'''
Created on 29 giu 2019

@author: paola
'''


class Rotta():

    def __init__(self, capacita, Nodo):
        self.nodi = []
        self.indiciNodi = []
        self.caricoAttualeLinehaul = capacita
        self.caricoAttualeBackhaul = 0
        self.capacitaCamion = capacita
        self.nodi.append(Nodo)
        self.indiciNodi.append(Nodo.getIndice())
        self.costoTotale = 0



    def appendiNodoLinehaul(self,Nodo):
        if Nodo.getLinehaul() > 0 and self.caricoAttualeLinehaul > Nodo.getLinehaul() and self.caricoAttualeLinehaul - Nodo.getLinehaul() > 0:
            self.nodi.append(Nodo)
            self.caricoAttualeLinehaul = self.caricoAttualeLinehaul - Nodo.getLinehaul()
            self.appendIndiceNodo(Nodo.getIndice())
            return True

        return False

    def appendiNodoBackhaul(self, Nodo):

        if Nodo.getBackhaul() > 0 and self.caricoAttualeBackhaul + Nodo.getBackhaul() < self.capacitaCamion:
            self.nodi.append(Nodo)
            self.caricoAttualeBackhaul = self.caricoAttualeBackhaul + Nodo.getBackhaul()
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

    def getLastNodeIndex(self):
        return self.nodi[-1].getIndice()

    def appendiNodoDeposito(self, Nodo):
        self.nodi.append(Nodo)
        self.appendIndiceNodo(0)

    def calcolaCostoRotta(self, matrice):
        costo = 0
        for i in range(0, len(self.nodi)-1):
            costo = costo + matrice[self.nodi[i].getIndice()][self.nodi[i+1].getIndice()]
        return costo

    def getRimanenza(self):
        return self.caricoAttualeLinehaul