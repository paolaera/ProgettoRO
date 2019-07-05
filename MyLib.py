'''
Created on 29 mag 2019

@author: paola
'''

import math
from math import sqrt
import numpy
import Nodo


def LeggiIstanze(NomeFile):
    Nodi=[]
    istanza = open(NomeFile, "r")
    numc = istanza.readline()
    istanza.readline()
    istanza.readline()
    for i in range(int(numc) + 1):
        nodoAttuale=Nodo()
        mys = istanza.readline()
        mysplit = pul_split(mys)

        # devo riempire i vettori delle coordinate
        nodoAttuale.setCoordX(int(mysplit[0]))
        nodoAttuale.setCoordY(int(mysplit[1]))

        # riempiamo il vettore della domanda
        if (int(mysplit[2])) == 0:
            nodoAttuale.setBackhaul(int(mysplit[3]))
        else:
            nodoAttuale.setLinehaul(int(mysplit[2]))
        Nodi.append(nodoAttuale)
    return Nodi


def pul_split(l):
    l = l.replace("\r", "")
    l = l.replace("\n", "")

    splitl = l.split(" ")

    splitl = list(filter(lambda x: x != "", splitl))
    return splitl


# Funzione per la creazione e riempimento della matrice delle distanze
def calcolaMatriceDistanze(vecX, vecY):
    matrice = []
    for i in range(len(vecX)):
        rig = []
        for j in range(len(vecX)):
            rig.append(sqrt((vecX[i] - vecX[j]) ** 2 + (vecY[i] - vecY[j]) ** 2))
        matrice.append(rig)
    return matrice


# Funzione per la creazione e riempimento della matrice dei saving
def calcolaMatriceSavings(vecX, vecY):
    matrice = calcolaMatriceDistanze(vecX, vecY)
    saving = []
    for i in range(1, len(vecX)):
        rig = []
        for j in range(1, len(vecX)):
            if i != j:
                rig.append(matrice[0][i] + matrice[0][j] - matrice[i][j])
            else:
                rig.append(0.0)
        saving.append(rig)
    saving = numpy.array(saving)
    # print "matrice =",matrice
    return saving


def creazioneTriple(saving, vecX):
    triple = []
    for i in range(len(vecX) - 1):
        for j in range(len(vecX) - 1):
            a = [saving[i][j], i, j]
            triple.append(a)
    print 'triple=', triple
    return triple


# creazione di tutti i cicli che partono dal deposito e vanno in un solo nodo
def creazioneCicliSingoli(vecX):
    ciclo = []
    for i in range(1, len(vecX)):
        a = [0, i, 0]
        ciclo.append(a)
    print 'ciclo=', ciclo
    return ciclo





