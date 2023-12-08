import random

class Noeud():
    def __init__(self, val:int, parent=None, enfantGauche=None, enfantDroit=None):
        self.val = val
        self.parent = parent
        self.enfantGauche = enfantGauche
        self.enfantDroit = enfantDroit
        self.generation = 0

def print_noeud(noeud,profondeur=0):
    if noeud.enfantDroit:
        print_noeud(noeud.enfantDroit,profondeur+1)
    for i in range(0,profondeur):
        print(" ",end="")
    print(noeud.val)
    if noeud.enfantGauche:
        print_noeud(noeud.enfantGauche,profondeur+1)

def ajout(noeud, nouveau):
    # Insert the new node at the correct position in the tree
    if not noeud.enfantGauche:
        noeud.enfantGauche = nouveau
        nouveau.parent = noeud
        if noeud.enfantDroit:
            noeud.generation = max(noeud.generation, noeud.enfantDroit.generation)
        else:
            noeud.generation = noeud.generation + 1
    elif not noeud.enfantDroit:
        noeud.enfantDroit = nouveau
        nouveau.parent = noeud
        if noeud.enfantGauche:
            noeud.generation = max(noeud.generation, noeud.enfantGauche.generation)
        else:
            noeud.generation = noeud.generation + 1
    else:
        if noeud.enfantGauche.generation <= noeud.enfantDroit.generation:
            ajout(noeud.enfantGauche, nouveau)
            if noeud.enfantDroit:
                noeud.generation = max(noeud.enfantGauche.generation + 1, noeud.enfantDroit.generation)
            else:
                noeud.generation = noeud.generation + 1
        else:
            ajout(noeud.enfantDroit, nouveau)
            if noeud.enfantGauche:
                noeud.generation = max(noeud.enfantDroit.generation + 1, noeud.enfantGauche.generation)
            else:
                noeud.generation = noeud.generation + 1
    echanger(noeud)
    # Percolate up
    while nouveau.parent and nouveau.val < nouveau.parent.val:
        nouveau.val, nouveau.parent.val = nouveau.parent.val, nouveau.val
        nouveau = nouveau.parent


def SupprMin(tas):
    dernier_noeud = trouver_premier_vide(tas)
    print("Dernier noeud:", dernier_noeud.val)
    if dernier_noeud.enfantDroit is not None:
        node_to_replace = dernier_noeud.enfantDroit
    elif dernier_noeud.enfantGauche is not None:
        node_to_replace = dernier_noeud.enfantGauche
    else:
        node_to_replace = dernier_noeud
    node_to_replace.enfantGauche = tas.enfantGauche
    node_to_replace.enfantDroit = tas.enfantDroit
    tas.enfantGauche.parent = node_to_replace
    tas.enfantDroit.parent = node_to_replace
    tas.enfantDroit, tas.enfantGauche = None, None
    while (node_to_replace.enfantGauche and node_to_replace.val > node_to_replace.enfantGauche.val) or \
        (node_to_replace.enfantDroit and node_to_replace.val > node_to_replace.enfantDroit.val):
        if node_to_replace.val > node_to_replace.enfantGauche.val:
            node_to_replace.enfantGauche, node_to_replace.enfantDroit = \
                node_to_replace.enfantGauche.enfantGauche, node_to_replace.enfantGauche.enfantDroit
            node_to_replace.enfantGauche.enfantGauche = node_to_replace
            node_to_replace.parent = node_to_replace.enfantGauche
            node_to_replace.enfantGauche.parent = None
            # node_to_replace = node_to_replace.enfantGauche
        elif node_to_replace.val > node_to_replace.enfantDroit.val:
            node_to_replace.enfantGauche, node_to_replace.enfantDroit = \
                node_to_replace.enfantDroit.enfantGauche, node_to_replace.enfantDroit.enfantDroit
            node_to_replace.enfantDroit.enfantDroit = node_to_replace
            node_to_replace.parent = node_to_replace.enfantDroit
            node_to_replace.enfantDroit.parent = None
            # node_to_replace = node_to_replace.enfantDroit
    return node_to_replace

def trouver_premier_vide(tas):
    if tas is None:
        return None
    if tas.enfantGauche is None:
        return tas
    result_gauche = trouver_premier_vide(tas.enfantGauche)
    if result_gauche is not None:
        return result_gauche
    if tas.enfantDroit is None:
        return tas
    result_droit = trouver_premier_vide(tas.enfantDroit)
    return result_droit


def echanger(noeud):
    if not noeud.enfantDroit or not noeud.enfantGauche:
        return
    if noeud.enfantDroit.generation > noeud.enfantGauche.generation:
        noeud.enfantDroit, noeud.enfantGauche = noeud.enfantGauche, noeud.enfantDroit
    echanger(noeud.enfantDroit)
    echanger(noeud.enfantGauche)

def ajoutsIteratifs(cles: list) -> list:
    if not cles:
        return list()
    tas = Noeud(val=cles[0])
    for i in range(1, len(cles)):
        ajout(tas, Noeud(val=cles[i]))
    return tas

def afficherTas(tas):
    if tas != None:
        print(tas.val, tas.generation)
    if tas.enfantGauche != None:
        afficherTas(tas.enfantGauche)
    if tas.enfantDroit != None:
        afficherTas(tas.enfantDroit)
    else:
        return
    

def main():
    cles = [4, 5, 2, 3, 6, 7, 1, 15, 20, 22]
    # tas = ajoutsIteratifs(cles)
    # print_noeud(tas)
    # test on a tree with 15 nodes
    # cles = random.sample(range(100), 15)
    tas = ajoutsIteratifs(cles)
    # ajout(tas, Noeud(8))
    new_tas = SupprMin(tas)
    print("Source:", new_tas.val)
    print(new_tas.enfantGauche.val, new_tas.enfantDroit.val)
    # afficherTas(new_tas)

if __name__ == "__main__":
    main()