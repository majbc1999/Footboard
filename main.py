import random

kocka = [1,2,3,4,5,6]


def met_kock():
    met1 = random.choice(kocka)
    met2 = random.choice(kocka)
    return [met1, met2]


class Figura:
    def __init__(self, x, y, tip):
        self.x = x
        self.y = y
        self.tip = tip
    
    def premakni(self, a, b):
        self.x += a
        self.y += b

    def ponastavi(self, a, b):
        self.x = a
        self.y = b
    
class Polje:
    def __init__(self, sez):
         self.x = sez[0]
         self.y = sez[1]
    
#    def tip(self):
#        if self.x == 0  and (self.y in 2:5):
#            return "Gol"
#        elif self.x == 2  and self.y == 15:
#            return "Zacetno polje"
#        else: return "Navadno"


def ustvari_polja(maxx, maxy):
    sez = []
    for i in range(maxx):
        for j in range(maxy):
            sez.append(Polje([i,j]))
    return sez

class Stadion:
    def __init__(self, maxx, maxy):
        self.polja = ustvari_polja(maxx, maxy)



