# -*- coding: utf-8 -*-
'''
Created on 29 mag 2019

@author: paola
'''

from MyLib import *
from __builtin__ import raw_input, True
import numpy
import operator
from Rotta import *


if __name__ == '__main__':

    Rotte = []
    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    Nodi,camion = LeggiIstanze("Istanze/" + nomeFile + ".txt")
    Saving = calcolaMatriceSavings(Nodi)
    capacita = Nodi[0].getBackhaul()

    triple = creazioneTriple(Saving, Nodi)
    triple.sort(key=operator.itemgetter(0), reverse=True)
    triple = triple[:len(triple)-len(Nodi)+1]
    for j in range(camion):
        nuovaRotta = Rotta(capacita, Nodi[0])

        print len(triple)

        for i in range(len(triple)):

            indNodAtt = triple[i][1]
            indNodAtt2 = triple[i][2]
            nodoAtt = Nodi[indNodAtt]
            nodoAtt2 = Nodi[indNodAtt2]

            if nodoAtt.getLinehaul() > 0 and nodoAtt2.getLinehaul() > 0:
                if not (nodoAtt2.getIndice() == 0) and not (nodoAtt.getIndice() == 0):
                    if (nodoAtt.getIndice() not in nuovaRotta.getIndiciNodi()) and (nodoAtt2.getIndice() not in nuovaRotta.getIndiciNodi()):
                        cond1 = nuovaRotta.appendiNodoLinehaul(nodoAtt)
                        cond2 = nuovaRotta.appendiNodoLinehaul(nodoAtt2)
                        if cond1 or cond2:
                            triple[i] = [-1, -1, -1]

        #TODO for backhaul

        #elimino i nodi già presi e segnato con -1
        nuovoT = []
        for m in range(len(triple)):
            if not (triple[m][0] == -1):
                nuovoT.append(triple[m])
        triple = nuovoT

        nuovaRotta.removeDuplicate()

        Rotte.append(nuovaRotta)





