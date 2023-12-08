class NoeudBinomial:
    def __init__(self, cle):
        self.cle = cle
        self.degre = 0
        self.enfants = []

def fusionner_arbres(arbre1, arbre2):
    if arbre1.cle > arbre2.cle:
        arbre1, arbre2 = arbre2, arbre1
    new_arbre=arbre1
    new_arbre.enfants.append(arbre2)
    new_arbre.degre += 1
    return new_arbre

class FileBinomiale:
    def __init__(self):
        self.liste_arbres = []

    def ajout(self, cle):
        nouvel_arbre = NoeudBinomial(cle)
        autre_file = FileBinomiale()
        autre_file.liste_arbres.append(nouvel_arbre)
        self.union(autre_file)

    def union(self, autre_file):
        self.liste_arbres.extend(autre_file.liste_arbres)
        self.construction()

    def construction(self):
        modification=False
        i = 0
        while i < len(self.liste_arbres):
            actuel = self.liste_arbres[i]
            degre_actuel = actuel.degre
            j = i + 1  
            while j < len(self.liste_arbres):
                suivant = self.liste_arbres[j]
                if degre_actuel == suivant.degre:
                    self.liste_arbres[i]=fusionner_arbres(actuel, suivant)
                    del self.liste_arbres[j]
                    modification=True
                else:
                    j += 1

            i += 1
        if modification:
            self.construction()

    def suppr_min(self):
        if not self.liste_arbres:
            return None
        min_arbre = min(self.liste_arbres, key=lambda x: x.cle)
        self.liste_arbres.remove(min_arbre)
        nouvelle_file = FileBinomiale()
        nouvelle_file.liste_arbres = min_arbre.enfants
        self.union(nouvelle_file)
        return min_arbre.cle

    def afficher(self):
        for arbre in self.liste_arbres:
            self.afficher_arbre(arbre)

    def afficher_arbre(self, arbre):
        if arbre is not None:
            print(f"Arbre de degré {arbre.degre}: {arbre.cle}")
            for enfant in arbre.enfants:
                self.afficher_arbre(enfant)

# file_binomiale = FileBinomiale()

# file_binomiale.ajout(1)
# file_binomiale.ajout(3)
# file_binomiale.ajout(7)
# file_binomiale.ajout(8)
# file_binomiale.ajout(5)
# file_binomiale.ajout(9)
# file_binomiale.ajout(11)

# print("File binomiale après construction:")
# file_binomiale.afficher()

# for arbre in file_binomiale.liste_arbres:
#     print(arbre.cle, " / ", arbre.degre)

# min_val = file_binomiale.suppr_min()
# print(f"\nMinimum supprimé: {min_val}")

# print("\nFile binomiale après suppression du minimum:")
# file_binomiale.afficher()

# for arbre in file_binomiale.liste_arbres:
#     print(arbre.cle, " / ", arbre.degre)