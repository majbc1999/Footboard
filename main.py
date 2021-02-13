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

def ustvari_gol(maxx, maxy, gol_velikost): # Če je širina polja soda, mora biti velikost gola soda in obratno
    sez = []
    if maxx % 2 != gol_velikost % 2: return "Niso prave dimenzije."
    for i in range(int(maxx / 2 - gol_velikost / 2), int(maxx / 2 + gol_velikost / 2)):
        sez.append([i, -1])
        sez.append([i, maxy])
    return sez

def okolica_tocke(tocka):
    x, y = tocka[0], tocka[1]
    sez = []
    ok = [-1, 0, 1]
    for k in ok:
        sez.append([x+k, y])
        sez.append([x, y+k])
    return sez

def ustvari_kazenski(maxx, maxy, dimenzije):
    zac = maxx / 2 - dimenzije[0] / 2
    sez = []
    for i in range(dimenzije[0]):
        for j in range(dimenzije[1]):
            sez.append([int(zac + i), j])
            sez.append([int(zac + i), maxx - 1 - j])
    return sez
    

########################################### ~ STADION ~ ###########################################
class Stadion:

    def __init__(self, maxx, maxy, gol_velikost, dimenzijekazenskega):
        self.polja = ustvari_polja(maxx, maxy)
        self.polja.append(ustvari_gol(maxx, maxy, gol_velikost))
        self.kazenski = ustvari_kazenski(maxx, maxy, dimenzijekazenskega)   

    def doloci_postave(self, postave, postavegolman):
        self.postave = postave
        self.postavegolman = postavegolman



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


########################################### ~ DEFAULT NASTAVITVE ZA ZAČETEK ~ ###########################################
