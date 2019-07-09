# -*- coding: utf-8 -*-
'''
Created on 29 mag 2019

@author: paola
'''

from MyLib import *
from __builtin__ import raw_input, True
import operator



if __name__ == '__main__':

    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    nodi, camion = LeggiIstanze("Istanze/" + nomeFile + ".txt")
    matrice = calcolaMatriceDistanze(nodi)
    Saving = calcolaMatriceSavings(nodi)
    capacita = nodi[0].getBackhaul()
    costi = []


    tripleLinehaul, tripleBackhaul, tripleMiste = creazioneTriple(Saving, nodi)
    tripleLinehaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleBackhaul.sort(key=operator.itemgetter(0), reverse=True)
    tripleMiste.sort(key=operator.itemgetter(0), reverse=True)

    rotte, presi = creazioneRotteIniziali(camion, capacita, nodi, tripleLinehaul)

    rotte = attaccaLinehaul(rotte, tripleLinehaul, nodi, presi)
    rotte = attaccaNodiMisti(rotte, tripleMiste, nodi, presi)
    rotte = attaccaBackHaul(rotte, tripleBackhaul, nodi, presi)

    for i in range(len(rotte)):
        rotte[i].appendiNodoDeposito(nodi[0])

    for i in range(len(rotte)):
        costi.append(rotte[i].calcolaCostoRotta(matrice))

    costo = sum(costi)




