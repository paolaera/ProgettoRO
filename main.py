# -*- coding: utf-8 -*-
'''
Created on 29 mag 2019

@author: paola
'''

from MyLib import *
from __builtin__ import raw_input, True
import operator
import time




if __name__ == '__main__':

    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    nodi, camion = LeggiIstanze("Istanze/" + nomeFile + ".txt")
    matrice = calcolaMatriceDistanze(nodi)
    Saving = calcolaMatriceSavings(nodi)
    capacita = nodi[0].getBackhaul()
    costi = []

    if nomeFile.startswith("I"):
        #selezione delle triple dalla matrice dei Saving
        tripleLinehaul, tripleBackhaul, tripleMiste = creazioneTriple(Saving, nodi)
        tripleLinehaul.sort(key=operator.itemgetter(0), reverse=True)
        tripleBackhaul.sort(key=operator.itemgetter(0), reverse=True)
        tripleMiste.sort(key=operator.itemgetter(0), reverse=True)

        #Inizio creazione delle rotte con inizio conteggio tempo
        start = time.time()
        rotteLinehaul, presiLinehaul = creazioneRotteInizialiLinehaul(camion, capacita, nodi, tripleLinehaul)
        rotteLinehaul = attaccaLinehaul(rotteLinehaul, tripleLinehaul, nodi, presiLinehaul)
        rotteBackhaul, presiBackhaul = creazioneRotteInizialiBackhaul(camion, capacita, nodi, tripleBackhaul)
        rotteBackhaul = attaccaBackHaul(rotteBackhaul, tripleBackhaul, nodi, presiBackhaul)
        rotte, presina = incollaMentoRotte(rotteLinehaul, rotteBackhaul, tripleMiste,nodi)

        presina = duplicate(presina)
        indiciNodi = getIndiciNodiLista(nodi)

        presina.sort()
        indiciNodi.sort()

        if presina == indiciNodi:
            print 'tutti i nodi sono presenti'
        else:
            print 'stai facendo cagate'

        for i in range(len(rotte)):
            rotte[i].appendiNodoDeposito(nodi[0])


        end = time.time()

        #calcolo del costo di ogni rotta e somma di tutti i costi
        for i in range(len(rotte)):
            costi.append(rotte[i].calcolaCostoRotta(matrice))

        costo = sum(costi)
        tempo = end -start

        # import soluzione ottima
        bestSolution = importBestSolution(
            "/home/paola/PycharmProjects/Progetto/Best__Solutions/RPA_Solutions/Detailed_Solution_" + nomeFile + ".txt")

        # errore relativo e assoluto
        erroreRelativo = calcolaErroreRelativo(costo, bestSolution)
        erroreAssoluto = calcolaErroreAssoluto(costo, bestSolution)

        print 'errore relativo:', erroreRelativo
        print 'errore assoluto:', erroreAssoluto
        print 'tempo in secondi:', tempo

    else:
        tripleLinehaul, tripleBackhaul, tripleMiste = creazioneTriple(Saving, nodi)
        tripleLinehaul.sort(key=operator.itemgetter(0), reverse=True)
        tripleBackhaul.sort(key=operator.itemgetter(0), reverse=True)
        tripleMiste.sort(key=operator.itemgetter(0), reverse=True)

        rotte, presi = creazioneRotteIniziali(camion, capacita, nodi, tripleLinehaul)

        start = time.time()

        rotte = attaccaLinehaul(rotte, tripleLinehaul, nodi, presi)
        rotte = attaccaNodiMisti(rotte, tripleMiste, nodi, presi)
        rotte = attaccaBackHaul(rotte, tripleBackhaul, nodi, presi)

        end = time.time()
        tempo = end - start
        print 'tempo in secondi:', tempo



