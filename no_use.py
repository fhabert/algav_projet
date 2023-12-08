
# #--------------------------
# class TasMin:
#     def __init__(self):
#         self.racine = None

#     def ajouter(self, val):
#         nouveau_noeud = Noeud(val)
#         if self.racine is None:
#             self.racine = nouveau_noeud
#         else:
#             dernier_noeud = self._trouver_dernier_noeud()
#             if dernier_noeud.enfantGauche is None:
#                 dernier_noeud.enfantGauche = nouveau_noeud
#             else:
#                 dernier_noeud.enfantDroit = nouveau_noeud
#             nouveau_noeud.parent = dernier_noeud
#             self._monter(nouveau_noeud)

#     def supprimer_min(self):
#         if not self.racine:
#             raise IndexError("Le tas est vide")

#         min_val = self.racine.val

#         # Trouver le dernier nœud
#         dernier_noeud = self._trouver_dernier_noeud()

#         # Échanger la valeur du minimum avec la valeur du dernier nœud
#         self.racine.val = dernier_noeud.val

#         # Supprimer le dernier nœud
#         if dernier_noeud.parent:
#             if dernier_noeud.parent.enfantGauche == dernier_noeud:
#                 dernier_noeud.parent.enfantGauche = None
#             else:
#                 dernier_noeud.parent.enfantDroit = None

#         # Faire redescendre la nouvelle racine à sa position correcte
#         self._descendre(self.racine)

#         return min_val

#     def ajouts_iteratifs(self, iterable):
#         for val in iterable:
#             self.ajouter(val)

#     def _monter(self, noeud):
#         while noeud.parent is not None and noeud.parent.val > noeud.val:
#             # Échanger les valeurs des nœuds
#             noeud.val, noeud.parent.val = noeud.parent.val, noeud.val
#             # Déplacer vers le parent
#             noeud = noeud.parent

#     def _descendre(self, noeud):
#         while True:
#             enfant_min = noeud
#             if (noeud.enfantGauche is not None and
#                     noeud.enfantGauche.val < enfant_min.val):
#                 enfant_min = noeud.enfantGauche
#             if (noeud.enfantDroit is not None and
#                     noeud.enfantDroit.val < enfant_min.val):
#                 enfant_min = noeud.enfantDroit

#             if enfant_min == noeud:
#                 break

#             # Échanger les valeurs des nœuds
#             noeud.val, enfant_min.val = enfant_min.val, noeud.val
#             # Déplacer vers l'enfant
#             noeud = enfant_min

#     def _trouver_dernier_noeud(self):
#         queue = [self.racine]
#         dernier_noeud = None
#         while queue:
#             dernier_noeud = queue.pop(0)
#             if dernier_noeud.enfantGauche is not None:
#                 queue.append(dernier_noeud.enfantGauche)
#             if dernier_noeud.enfantDroit is not None:
#                 queue.append(dernier_noeud.enfantDroit)
#         return dernier_noeud


# #--------------------



## Fonctions sur une structure d'arbre binaire

def AjoutAB(root, key):
    if root is None:
        root = Noeud(key)
    else:
        nouveau_noeud = AjoutABrecursif(root, key)
        while nouveau_noeud.parent is not None and nouveau_noeud.val < nouveau_noeud.parent.val:
            if nouveau_noeud.parent.enfantGauche == nouveau_noeud:
                nouveau_noeud.enfantGauche, nouveau_noeud.parent.enfantGauche = nouveau_noeud.parent, \
                      nouveau_noeud
            elif nouveau_noeud.parent.enfantDroit == nouveau_noeud:
                nouveau_noeud.enfantDroit, nouveau_noeud.parent.enfantDroit = nouveau_noeud.parent, \
                      nouveau_noeud
            nouveau_noeud = nouveau_noeud.parent
    return root

def AjoutABrecursif(node, key):
    if node.enfantGauche is None:
        node.enfantGauche = Noeud(key)
        node.enfantGauche.parent = node
        return node.enfantGauche
    elif node.enfantDroit is None:
        node.enfantDroit = Noeud(key)
        node.enfantDroit.parent = node
        return node.enfantDroit
    else:
        return AjoutABrecursif(node.enfantGauche, key)


def AjoutABBIs(cle: list, tas: list) -> list:
    tas.append(Noeud(val=cle))
    indice_nouveau_noeud = len(tas) - 1
    while indice_nouveau_noeud > 0:
        indice_parent = (indice_nouveau_noeud - 1) // 2
        nouveau_noeud = tas[indice_nouveau_noeud]
        parent_noeud = tas[indice_parent]
        if parent_noeud.val > nouveau_noeud.val:
            tas[indice_nouveau_noeud], tas[indice_parent] = tas[indice_parent], tas[indice_nouveau_noeud]
            parent_noeud.parent, nouveau_noeud.parent = nouveau_noeud.parent, parent_noeud

            if parent_noeud.enfantGauche == nouveau_noeud:
                parent_noeud.enfantGauche, nouveau_noeud.enfantGauche, nouveau_noeud.enfantDroit = \
                    nouveau_noeud.enfantGauche, parent_noeud, nouveau_noeud.enfantDroit
                if parent_noeud.enfantGauche:
                    parent_noeud.enfantGauche.parent = parent_noeud

            elif parent_noeud.enfantDroit == nouveau_noeud:
                parent_noeud.enfantDroit, nouveau_noeud.enfantGauche, nouveau_noeud.enfantDroit = \
                    nouveau_noeud.enfantGauche, parent_noeud, nouveau_noeud.enfantDroit
                if parent_noeud.enfantDroit:
                    parent_noeud.enfantDroit.parent = parent_noeud
            indice_nouveau_noeud = indice_parent
        else:
            break
    return tas


def SupprMin(tas: list) -> int: # prend une liste de int
    if not tas:
        raise IndexError("Le tas est vide")
    dernier_element = tas.pop()
    if tas:
        tas[0] = dernier_element
        indice_element_courant = 0
        while True:
            indice_enfant_gauche = 2 * indice_element_courant + 1
            indice_enfant_droit = 2 * indice_element_courant + 2
            enfant_min = indice_element_courant
            if (indice_enfant_gauche < len(tas) and tas[indice_enfant_gauche] < tas[enfant_min]):
                enfant_min = indice_enfant_gauche
            if (indice_enfant_droit < len(tas) and tas[indice_enfant_droit] < tas[enfant_min]):
                enfant_min = indice_enfant_droit
            if enfant_min == indice_element_courant:
                break
            tas[indice_element_courant], tas[enfant_min] = tas[enfant_min], tas[indice_element_courant]
            indice_element_courant = enfant_min
    return tas

def UnionTasAB(tas1, tas2):
    if not tas1:
        return tas2
    if not tas2:
        return tas1
    if tas1.val > tas2.val:
        tas1, tas2 = tas2, tas1
    tas1.enfantDroit = UnionTasAB(tas1.enfantDroit, tas2)
    if tas1.enfantGauche is None or (tas1.enfantDroit is not None and tas1.enfantDroit.val < tas1.enfantGauche.val):
        tas1.enfantGauche, tas1.enfantDroit = tas1.enfantDroit, tas1.enfantGauche
    return tas1


def AfficherAB(tas, niveau=0):
    if tas:
        print(tas.val, end=' ')
        if tas.enfantGauche or tas.enfantDroit:
            if tas.enfantGauche:
                print(tas.enfantGauche.val)
            if tas.enfantDroit:
                print(" ", tas.enfantDroit.val)
            # if niveau 
            # print("\n" + "   " * niveau, end='')  # Retour à la ligne pour les niveaux suivants
        AfficherAB(tas.enfantGauche, niveau + 1)
        AfficherAB(tas.enfantDroit, niveau + 1)


        
##### FONCTION AVEC ARBRE BINAIRE

tas1 = Noeud(1)
tas1.enfantGauche = Noeud(4)
tas1.enfantDroit = Noeud(5)

tas2 = Noeud(10)
tas2.enfantGauche = Noeud(11)
tas2.enfantDroit = Noeud(15)

# print("Union Tas Tableau:")
# tas_construit = AfficherAB(UnionTasAB(tas1, tas2))

tas = Noeud(1)
tas.parent = None
tas.enfantGauche = Noeud(4)
tas.enfantGauche.parent = tas
tas.enfantDroit = Noeud(5)
tas.enfantDroit.parent = tas

# tas.enfantGauche.enfantGauche = Noeud(10)
# tas.enfantGauche.enfantGauche.parent = tas.enfantGauche
# tas.enfantGauche.enfantGauche.enfantGauche = None
# tas.enfantGauche.enfantGauche.enfantDroit = None

# tas.enfantGauche.enfantDroit = Noeud(11)
# tas.enfantGauche.enfantDroit.parent = tas.enfantGauche
# tas.enfantGauche.enfantDroit.enfantGauche = None
# tas.enfantGauche.enfantDroit.enfantDroit = None

# tas.enfantDroit.enfantGauche = Noeud(15)
# tas.enfantDroit.enfantGauche.parent = tas.enfantDroit
# tas.enfantDroit.enfantGauche.enfantGauche = None
# tas.enfantDroit.enfantGauche.enfantDroit = None

# tas.enfantDroit.enfantDroit = Noeud(20)
# tas.enfantDroit.enfantDroit.parent = tas.enfantDroit
# tas.enfantDroit.enfantDroit.enfantGauche = None
# tas.enfantDroit.enfantDroit.enfantDroit = None

# print("------")
# print("Ajout AB:")
# tas_construit = AjoutAB(tas, 2)

# print(tas_construit.enfantGauche.val)


# analyse_complexite()
# analyse_complexite_union()
# analyse_union()

class Noeud():
    def __init__(self, val:list, parent=None, enfantGauche=None, enfantDroit=None):
        self.val = val
        self.parent = parent
        self.enfantGauche = enfantGauche
        self.enfantDroit = enfantDroit

def print_cles(tas_min):
    for noeud in tas_min:
        print(noeud.val)

def NoeudsToCles(tas: list) -> list:
    cles=[]
    for n in tas:
        n.val
        cles.append(n.val)
    return cles