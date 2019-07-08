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


def creazioneRotteIniziali(camion, capacita, nodi,tripleLinehaul):
    tripleLinehaul2 = []
    rotte = []
    presi = []
    for j in range(camion):
        nuovaRotta = Rotta(capacita, nodi[0])
        rotte.append(nuovaRotta)

    for i in range(camion):
        condizione = True
        while condizione:
            if i != 0:
                j +=1
            else:
                j = 0
            if tripleLinehaul[j][1] not in presi:
                if tripleLinehaul[j][2] not in presi:
                    rotte[i].appendiNodoLinehaul(nodi[tripleLinehaul[j][1]])
                    rotte[i].appendiNodoLinehaul(nodi[tripleLinehaul[j][2]])
                    presi.append(tripleLinehaul[j][1])
                    presi.append(tripleLinehaul[j][2])
                    tripleLinehaul[j] = [-1, -1, -1]
                    condizione = False

    return rotte


if __name__ == '__main__':

    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    nodi, camion = LeggiIstanze("Istanze/" + nomeFile + ".txt")
    Saving = calcolaMatriceSavings(nodi)
    capacita = nodi[0].getBackhaul()

    tripleLinehaul, tripleBackhaul, tripleMiste = creazioneTriple(Saving, nodi)
    tripleLinehaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleBackhaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleMiste.sort(key=operator.itemgetter(0), reverse=True)

    rotte = creazioneRotteIniziali(camion, capacita, nodi,tripleLinehaul)


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



