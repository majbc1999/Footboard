import random

########################################### ~ POMOŽNE FUNKCIJE ~ ###########################################
kocka = [1,2,3,4,5,6]


def met_kock():
    met1 = random.choice(kocka)
    met2 = random.choice(kocka)
    return [met1, met2]


########################################### ~ FIGURA ~ ###########################################
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


########################################### ~ POLJE ~ ########################################### 

def ustvari_polja(maxx, maxy):
    sez = []
    for i in range(maxx):
        for j in range(maxy):
            sez.append([i,j])
    return sez


########################################### ~ STADION ~ ###########################################
class Stadion:
    def __init__(self, maxx, maxy):
        self.polja = ustvari_polja(maxx, maxy)


########################################### ~ IGRALEC ~ ###########################################
class Igralec:
    def __init__(self, ime, figure):
        self.ime = ime
        self.figure = figure


########################################### ~ IGRA ~ ###########################################
class Game:
    def __init__(self, igralca, stadion):
        self.igralca = igralca # Igralca je seznam igralcev
        self.stadion = stadion # Stadion je seznam vseh polj

    def stanje(self):
        for igralec in self.igralca:
            for figura in igralec.figure:
                if [figura.x, figura.y] not in self.stadion: return False
        return True
                    

    def premik_figure(self, igralec, figura, x, y):
        igralec.figure[figura].premakni(x, y)

    def poteza(self, igralec, figuri, premika):
        # Najprej je met kocke
        kocke = met_kock()
        # Po metu kock izbere potezi
        met1, met2 = kocke[0], kocke[1]
        self.premik_figure(igralec, figura[0], premika[0][0], premika[0][1])
        self.premik_figure(igralec, figura[1], premika[1][0], premika[1][1])



