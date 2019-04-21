""" Ein Instanz-Attribut wird im Konstruktor durch eine Methode erzeugt.
    Soll der Attribut modifiziert werden, wird er jedes mal durch die Methode
    im Klassen-Konstruktor erneut erzeugt.
 """

import sys  # fuer die Ausgabe auf die Konsole ohne Leerzeichen

class Chestboard:

    def __init__(self, x, y):
        """ Der Konstruktor erzeugt ein Spielbrett mit Laenge x und Breite y """
        self.x = x
        self.y = y
        self.board = []
        """ empty-list wird nur einmal erzeugt d.h. jede Unterliste in board enthält eine 
            Referenz auf empty_list.
            Wird empty-list verändert, verändern sich alle Unterliste von board gleichermaß.
            """
        empty_list = []
        while x > 0:
            while y > 0:    # die Schleife laeuft nur einmal, da wir immer dieselbe empty_list den board hinfuegen
                empty_list.append([])
                y -= 1
            self.board.append(empty_list)
            x -= 1


class Chestboard2:

    def __init__(self, x, y):
        """ Der Konstruktor erzeugt ein Spielbrett mit Laenge x und Breite y """
        self.x = x
        self.y = y
        self.board = []
        while x > 0:
            empty_list = []
            y = self.y
            while y > 0:    #die Schleife muss x-mal laufen, da wir immer neue empty_list mit [] füllen
                empty_list.append([])
                y -= 1
            self.board.append(empty_list)
            x -= 1


b = Chestboard(4, 4)
print('Chestboard (alle Unterliste sind Referenzen auf eine Liste):\n ' + str(b.board))
b.board[1][1].append('K')
print('Chestboard (alle Unterliste sind Referenzen auf eine Liste):\n ' + str(b.board))

b2 = Chestboard2(4, 4)
print('\n\nChestboard2:\n ' + str(b2.board))
b2.board[1][1].append('K')
print('Chestboard2:\n ' + str(b2.board))
