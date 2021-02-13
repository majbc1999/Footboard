import random
from main import Figura, Stadion, Igralec, Game

kmet11 = Figura(0,0, 'kmet')
kmet12 = Figura(2,1, 'kmet')
kmet21 = Figura(0,3, 'kmet')
kmet22 = Figura(3,2, 'kralj')

igralec1 = Igralec('Marjan', [kmet11, kmet12])
igralec2 = Igralec('Tomaž', [kmet21, kmet22])

igrisce = Stadion(4,4,2)

igraa = Game([igralec1, igralec2], igrisce)

def tip(igra):
    for igralec in igra.igralca:
        for figura in igralec.figure:
            print(igralec.ime) 
            print(figura.tip)

def mesta(igra):
    for igralec in igra.igralca:
        for figura in igralec.figure:
            print(igralec.ime, ': ', figura.tip, ' ~ ', figura.x, ',', figura.y)


igraa.premik_figure(igralec1, 1, -1, 1)

