import random
from main import Figura, Stadion, Igralec, Game, ustvari_polja, ustvari_gol, met_kock, okolica_tocke

# Koordinate je treba še spremeniti
a1 = Figura(0,0, 'igralec')
a2 = Figura(2,1, 'igralec')
a3 = Figura(0,3, 'igralec')
a4 = Figura(0,0, 'igralec')
a0 = Figura(2,1, 'golman')

b1 = Figura(0,3, 'igralec')
b2 = Figura(0,0, 'igralec')
b3 = Figura(2,1, 'igralec')
b4 = Figura(0,3, 'igralec')
b0 = Figura(3,2, 'golman')

# Nastavitve igralcev
igralec1 = Igralec('P1', [a0, a1, a2, a3, a4])
igralec2 = Igralec('P2', [b0, b1, b2, b3, b4])

# Nastavitve igrišča
igrisce = Stadion(15, 20, 7, [9,4])
postave = [[5,5], [9,5], [3,8], [11,8], [3,11], [11,11], [5, 14], [9, 14], [7,19]]
golman = [[7,0], [7,19]]
igrisce.doloci_postave(postave, golman)
