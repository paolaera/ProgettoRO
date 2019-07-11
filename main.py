# -*- coding: utf-8 -*-
'''
Created on 29 mag 2019

@author: paola
'''

from MyLib import *
from __builtin__ import raw_input, True
import operator
import time
import os




if __name__ == '__main__':
    directory = 'Istanze'
    #Risultati = open('Risultati.txt', 'w')
    fileImportati = os.listdir(directory)
    fileImportati.sort()
    listaErrori = []

    risutati = open("risultati_CW.txt", "a")

    for nomeFile in fileImportati:
        #nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
        nodi, camion = LeggiIstanze("Istanze/" + nomeFile)
        matrice = calcolaMatriceDistanze(nodi)
        Saving = calcolaMatriceSavings(nodi)
        capacita = nodi[0].getBackhaul()
        costi = []

        # import soluzione ottima
        bestSolution = importBestSolution("/home/paola/PycharmProjects/Progetto/Best__Solutions/RPA_Solutions/Detailed_Solution_" + nomeFile)

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
                print 'stai facendo cagate', nomeFile

            for i in range(len(rotte)):
                rotte[i].appendiNodoDeposito(nodi[0])


            end = time.time()

            #calcolo del costo di ogni rotta e somma di tutti i costi
            for i in range(len(rotte)):
                costi.append(rotte[i].calcolaCostoRotta(matrice))

            costo = sum(costi)
            tempo = end -start



            # errore relativo e assoluto
            erroreRelativo = calcolaErroreRelativo(costo, bestSolution)
            erroreAssoluto = calcolaErroreAssoluto(costo, bestSolution)

            listaErrori.append(erroreRelativo)


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

            for i in range(len(rotte)):
                rotte[i].appendiNodoDeposito(nodi[0])


            end = time.time()

            # calcolo del costo di ogni rotta e somma di tutti i costi
            for i in range(len(rotte)):
                costi.append(rotte[i].calcolaCostoRotta(matrice))
            costi = numpy.array(costi)


            costo = sum(costi)

            indiciNodi = getIndiciNodiLista(nodi)

            presi.sort()
            indiciNodi.sort()
            presi = [0] + presi
            if presi == indiciNodi:
                print 'tutti i nodi sono presenti'
            else:
                print 'stai facendo cagate', nomeFile


            tempo = end - start

            # errore relativo e assoluto
            erroreRelativo = calcolaErroreRelativo(costo, bestSolution)
            erroreAssoluto = calcolaErroreAssoluto(costo, bestSolution)
            listaErrori.append(erroreRelativo)


        risutati.write(nomeFile  + "\n")
        risutati.write("Errore relativo: " + str(erroreRelativo) + "\n")
        risutati.write("Errore assoluto: " + str(erroreAssoluto) + "\n")
        risutati.write("Tempo: " + str(erroreRelativo) + "\n")
        risutati.write("\n")

    erroreMedio = sum(listaErrori) / len(listaErrori)
    risutati.write("Errore medio: " + str(erroreMedio) + "\n")

    powdev = 0
    for u in range(len(listaErrori)):
        powdev += pow((listaErrori[i] - erroreMedio), 2)

    deviazioneStandard = sqrt(powdev / len(listaErrori))

    risutati.write("Deviazione standard: " + str(deviazioneStandard) + "\n")

    risutati.close()


