'''
Created on 29 mag 2019

@author: paola
'''

import math
from math import sqrt
import numpy
from Nodo import Nodo


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
    for i in range(1, len(Nodi)):
        rig = []
        for j in range(1, len(Nodi)):
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
    for i in range(1, len(Nodi) - 1):
        for j in range(1, len(Nodi) - 1):
            if  saving[i][j] == 0:
                break
            a = [saving[i][j], i, j]

            if Nodi[i].getLinehaul() > 0 and Nodi[j].getLinehaul() > 0:
                tripleLinehaul.append(a)
            elif Nodi[i].getBackhaul() > 0 and Nodi[j].getBackhaul() > 0:
                tripleBackhaul.append(a)
            else:
                tripleMiste.append(a)


    return tripleLinehaul, tripleBackhaul, tripleMiste




