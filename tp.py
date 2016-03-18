# -*- coding: utf-8 -*-
"""
SVL 2016
TP1 Méthodes formelles avec contracts.py
Auteur: Honore Nintunze, antonin Durey

Classes
"""

class Disque:

    """
    inv[self.taille]:
        self.taille > 0
    """
    def __init__(self,taille):
        self.taille = taille

class Tour:
    """
    Une tour pour contenir les disques ordonnées

    inv[self.disques]:
        # array is ordered
        forall([self.disques[i-1].taille > self.disques[i].taille for i in range(1, len(self.disques))])
    """


    def __init__(self, disques):
        """
        post:
            len(self.disques) == len(disques)
        """
        self.disques = disques

    def pop(self):
        """
        Retourne le sommet

        post[self.disques]:
            len(self.disques) == len(__old__.self.disques) - 1
            __return__ == __old__.self.disques[-1]
        """
        return self.disques.pop()

    def push(self,disque):
        """
        Dépose un disque sur la tour
        pre[self.disques]:
            len(self.disques) == 0 or disque.taille < self.disques[-1].taille

        post[self.disques]:
            self.disques[-1].taille == disque.taille

            len(self.disques) == len(__old__.self.disques) + 1
        """
        self.disques.append(disque)

class Hanoi:
    """
    Jeu des Tours de Hanoi

    """

    def __init__(self,tours):
        """
        Un jeu de Hanoi initialisé avec une seule tour possédant des disques
        pre:
            len(filter(lambda t: len(t.disques) > 0,tours)) == 1
        post:
            len(self.tours) == len(tours)
        """
        self.tours = tours

    def deplacer(self,source,dest):
        """
        Deplacer un disque d'une tour à une autre
        pre[self.tours]:
            source >= 0 and source < len(self.tours)
            dest >= 0 and dest < len(self.tours)
        post[self.tours]:
            __old__.self.tours[source].disques[-1] == self.tours[dest].disques[-1]
        """
        self.tours[dest].push(self.tours[source].pop())

    def jeu(self,n, D, A, I):
        """
        Execute le jeu de Hanoi

        """
        if n > 0:
            jeu(n-1,D,I,A)
            self.deplacer(D,A)
            jeu(n-1,I,A,D)




import contract
contract.checkmod(__name__)

if __name__ == "__main__":
    # Initialisation d'un jeu à 3 disques
    tour0 = Tour([Disque(i) for i in range(3, 0, -1)]) # si une autre tour contient des disques ça ne passe plus
    tour0.pop()
    tour0.push(Disque(1)) # avec 2 ou 0 ça ne passe plus


    tour1 = Tour([])
    tour2 = Tour([])

    hanoi = Hanoi([tour0, tour1,tour2])
    hanoi.deplacer(0, 1)

    # hanoi.jeu(len(tour0),0,2,1)
