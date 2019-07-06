# -*- coding: utf-8 -*-
'''
Created on 29 mag 2019

@author: paola
'''

from MyLib import *
from __builtin__ import raw_input, True
import numpy
import operator


if __name__ == '__main__':

    vecX = []
    vecY = []
    triple = []
    ciclo = []
    nomeFile = raw_input("Inserire il nome dell'istanza che si vuole utilizzare da A1 a N6 \n")
    vecX, vecY = LeggiIstanze("./Istanze/" + nomeFile + ".txt")
    print "vecX =", vecX
    print "vecY =", vecY

    saving = calcolaMatriceSavings(vecX, vecY)
    print "saving =", saving
    print "size =", numpy.shape(saving)


    triple = creazioneTriple(saving, vecX)
    print 'Triple prima =', triple
    triple.sort(key=operator.itemgetter(0), reverse=True)
    print 'triple dopo =', triple
    # ciclo=creazioneCicliSingoli(vecX)

