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

    rotte = []
    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    nodi,camion = LeggiIstanze("Istanze/" + nomeFile + ".txt")
    Saving = calcolaMatriceSavings(nodi)
    capacita = nodi[0].getBackhaul()

    tripleLinehaul, tripleBackhaul, tripleMiste = creazioneTriple(Saving, nodi)
    tripleLinehaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleBackhaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleMiste.sort(key=operator.itemgetter(0), reverse=True)

    for j in range(camion):
        nuovaRotta = Rotta(capacita, nodi[0])
        rotte.append(nuovaRotta)

"""
    for i in range(len(tripleLineh)):

        indNodAtt = triple[i][1]
        indNodAtt2 = triple[i][2]
        nodoAtt = Nodi[indNodAtt]
        nodoAtt2 = Nodi[indNodAtt2]




    #TODO for backhaul

    #elimino i nodi già presi e segnato con -1
    nuovoT = []
    for m in range(len(triple)):
        if not (triple[m][0] == -1):
            nuovoT.append(triple[m])

    triple = nuovoT

    Rotte.append(nuovaRotta)

"""




