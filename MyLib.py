'''
Created on 29 mag 2019

@author: paola
'''

import math
from math import sqrt
import numpy
from Nodo import Nodo
from Rotta import *


def LeggiIstanze(NomeFile):
    Nodi=[]
    istanza = open(NomeFile, "r")
    numc = istanza.readline()
    istanza.readline()
    camion = int(istanza.readline())
    for i in range(int(numc) + 1):
        nodoAttuale = Nodo()
        mys = istanza.readline()
        mysplit = pul_split(mys)

        # devo riempire i vettori delle coordinate
        nodoAttuale.setCoordX(int(mysplit[0]))
        nodoAttuale.setCoordY(int(mysplit[1]))
        nodoAttuale.setIndice(i)

        # riempiamo il vettore della domanda
        if (int(mysplit[2])) == 0:
            nodoAttuale.setBackhaul(int(mysplit[3]))
        else:
            nodoAttuale.setLinehaul(int(mysplit[2]))
        Nodi.append(nodoAttuale)
    return Nodi, camion


def pul_split(l):
    l = l.replace("\r", "")
    l = l.replace("\n", "")

    splitl = l.split(" ")

    splitl = list(filter(lambda x: x != "", splitl))
    return splitl


# Funzione per la creazione e riempimento della matrice delle distanze
def calcolaMatriceDistanze(Nodi):
    matrice = []
    for i in range(len(Nodi)):
        rig = []
        for j in range(len(Nodi)):
            rig.append(sqrt((Nodi[i].getCoordX() - Nodi[j].getCoordX()) ** 2 + (Nodi[i].getCoordY() - Nodi[j].getCoordY()) ** 2))
        matrice.append(rig)
    return matrice


# Funzione per la creazione e riempimento della matrice dei saving
def calcolaMatriceSavings(Nodi):
    matrice = calcolaMatriceDistanze(Nodi)
    saving = []
    for i in range(0, len(Nodi)):
        rig = []
        for j in range(0, len(Nodi)):
            if i != j:
                rig.append(matrice[0][i] + matrice[0][j] - matrice[i][j])
            else:
                rig.append(0.0)
        saving.append(rig)
    saving = numpy.array(saving)
    return saving


def creazioneTriple(saving, Nodi):
    tripleLinehaul = []
    tripleBackhaul = []
    tripleMiste = []
    for i in range(0, len(Nodi)):
        for j in range(0, len(Nodi)):
            a = [saving[i][j], i, j]

            if Nodi[i].getLinehaul() > 0 and Nodi[j].getLinehaul() > 0:
                tripleLinehaul.append(a)
            elif Nodi[i].getBackhaul() > 0 and Nodi[j].getBackhaul() > 0:
                tripleBackhaul.append(a)
            else:
                tripleMiste.append(a)

    return tripleLinehaul, tripleBackhaul, tripleMiste

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
                    print presi

    return rotte, presi

def attaccaLinehaul(rotte, tripleLinehaul, nodi, presi):

    while True:
        nonAttaccati = 0
        for i in range(len(rotte)):
            for j in range(len(tripleLinehaul)):

                if rotte[i].getLastNodeIndex() == tripleLinehaul[j][1]:
                    if tripleLinehaul[j][2] not in presi:
                        if rotte[i].appendiNodoLinehaul(nodi[tripleLinehaul[j][2]]):
                            presi.append(tripleLinehaul[j][2])
                            tripleLinehaul[j] = [-1, -1, -1]
                            nonAttaccati = 1
                            break
                elif rotte[i].getLastNodeIndex() == tripleLinehaul[j][2]:
                    if tripleLinehaul[j][1] not in presi:
                        if rotte[i].appendiNodoLinehaul(nodi[tripleLinehaul[j][1]]):
                            presi.append(tripleLinehaul[j][1])
                            tripleLinehaul[j] = [-1, -1, -1]
                            nonAttaccati = 1
                            break
        if nonAttaccati == 0:
            return rotte

def attaccaNodiMisti(rotte, tripleMiste, nodi, presi):
    for i in range(len(rotte)):
        for j in range(len(tripleMiste)):

            if rotte[i].getLastNodeIndex() == tripleMiste[j][1]:
                if tripleMiste[j][2] not in presi:
                    if rotte[i].appendiNodoBackhaul(nodi[tripleMiste[j][2]]):
                        presi.append(tripleMiste[j][2])
                        tripleMiste[j] = [-1, -1, -1]
                        break

            elif rotte[i].getLastNodeIndex() == tripleMiste[j][2]:
                if tripleMiste[j][1] not in presi:
                    if rotte[i].appendiNodoBackhaul(nodi[tripleMiste[j][1]]):
                        presi.append(tripleMiste[j][1])
                        tripleMiste[j] = [-1, -1, -1]
                        break
    return rotte

def attaccaBackHaul(rotte, tripleBackhaul, nodi, presi):

    while True:
        nonAttaccati = 0
        for i in range(len(rotte)):
            for j in range(len(tripleBackhaul)):

                if rotte[i].getLastNodeIndex() == tripleBackhaul[j][1]:
                    if tripleBackhaul[j][2] not in presi:
                        if rotte[i].appendiNodoBackhaul(nodi[tripleBackhaul[j][2]]):
                            presi.append(tripleBackhaul[j][2])
                            tripleBackhaul[j] = [-1, -1, -1]
                            nonAttaccati = 1
                            break
                elif rotte[i].getLastNodeIndex() == tripleBackhaul[j][2]:
                    if tripleBackhaul[j][1] not in presi:
                        if rotte[i].appendiNodoBackhaul(nodi[tripleBackhaul[j][1]]):
                            presi.append(tripleBackhaul[j][1])
                            tripleBackhaul[j] = [-1, -1, -1]
                            nonAttaccati = 1
                            break
        if nonAttaccati == 0:
            print presi

            return rotte



