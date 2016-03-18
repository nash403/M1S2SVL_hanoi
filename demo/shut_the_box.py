# CDT8 SVL - M. Nebut - 03/2016
# programmation par contrats avec contract.py

class Clapet:

    def __init__(self):
        """
        post:
            not self.ouvert
        """
        self.ouvert = False

    def ouvrir(self):
        """
        post:
           self.ouvert
        """
        self.ouvert = True

    def est_ouvert(self):
        return self.ouvert
        
class Boite:
    """
    illustration forall
    """
    
    def __init__(self, liste_clapets):
        self.clapets = liste_clapets


    def ouvrir(self):
        """
        Ouvre tous les clapets
        post:
            forall(self.clapets, Clapet.est_ouvert)
        """
        for clapet in self.clapets:
            clapet.ouvrir()

    def clapets_ouverts(self):
        """
        retourne la liste des clapets ouverts
        post:
             0 <= len(__return__) <= len(self.clapets)
             forall(__return__, Clapet.est_ouvert)
             # JML (\forall Clapet clapet; clapet in this.clapets;
             #       clapet in __return__ <==> clapet.est_ouvert())
             forall(self.clapets,
                    lambda clapet: not (clapet.ouvert and not clapet in __return__))
        """
        res = []
        for clapet in self.clapets:
            if clapet.est_ouvert():
                res = res + [clapet]
        return res
    
import contract
contract.checkmod(__name__)

if __name__ == '__main__':
    clapet1 = Clapet()
    clapet2 = Clapet()
    clapet1.ouvrir()
    boite = Boite([clapet1, clapet2])
    print boite.clapets_ouverts()
