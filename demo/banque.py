# CDT8 SVL - M. Nebut - 03/2016
# programmation par contrats avec contract.py

class Compte:
    """
    compte non plafonne, avec decouvert autorisable

    >>> compte = Compte()
    >>> compte.autoriser_decouvert(-100.0)

    inv:
        implies(self.decouvert_autorise,
                self.montant >= self.decouvert,
                self.montant >= 0)
    """

    def __init__(self):
        """
        post:
           self.montant == 0.0
           not self.decouvert_autorise
        """
        self.montant = 0.0
        self.decouvert_autorise = False
        self.decouvert = None

    def autoriser_decouvert(self, decouvert):
        """
        autorise le decouvert jusqu'a 'decouvert'

        pre:
            decouvert < 0.0
        post:
            self.decouvert_autorise
            self.decouvert == decouvert
        """
        self.decouvert = decouvert
        self.decouvert_autorise = True

    def debiter(self, somme):
        """
        pre:
            somme > 0
        post[self.montant]:
            self.montant == __old__.self.montant - somme
            # self.decouvert_autorise => self.montant >= self.decouvert
            # (not self.decouvert_autorise) => self.montant >= 0
            implies(self.decouvert_autorise,
                    self.montant >= self.decouvert,
                    self.montant >=0)
        """
        self.montant -= somme

    def crediter(self, somme):
        """
        pre:
           somme > 0
        post[self.montant]:
           self.montant == __old__.self.montant + somme
        """
        self.montant += somme

class ComptePlafonne(Compte):
    """
    ex d'heritage comportemental
    illustration principe de Liskiv viole
    
    ici implicitement invariant de Compte
    inv:
        self.montant <= self.plafond
    """

    def __init__(self, max):
        """
        post:
           max > 0
        """
        self.plafond = max
        self.montant = 0.0
        self.decouvert_autorise = False
        self.decouvert = None

    def crediter(self, somme):
        """
        heritage implicite de la post-condition
        pre:
            somme > 0
            self.montant + somme <= self.plafond
            # precondition invalide !
        """
        self.montant += somme
        
import contract
contract.checkmod(__name__)

if __name__ == '__main__':
    compte = ComptePlafonne(200.0)
    compte.crediter(500)
    
