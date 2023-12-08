import matplotlib.pyplot as plt
import time
import numpy as np
import file_bin
import arbre_binaire
import arbre_bin

NB_ENTIERS = 4
TAILLE_BITS  = 32

## Fonctions sur une structure tableau

def AjoutsIteratifsTableau(cles: list) -> list: #prend une liste de int
    if not cles:
        return list()
    tas = []
    for i in range(0, len(cles)):
        tas = AjoutTasTableau(tas, cles[i])
    return tas

def AjoutTasTableau(tas, valeur):
    tas.append(valeur)
    indice_nouveau = len(tas) - 1
    while indice_nouveau > 0:
        indice_parent = (indice_nouveau - 1) // 2
        if tas[indice_nouveau] < tas[indice_parent]:
            tas[indice_nouveau], tas[indice_parent] = tas[indice_parent], tas[indice_nouveau]
            indice_nouveau = indice_parent
        else:
            break
    return tas

def ConstructionTasTableau(cles: list) -> list:
    t = len(cles)
    for i in range(t // 2 - 1, -1, -1):
        cles = entasser(cles, i, t)
    return cles

def entasser(tas, indice, taille):
    plus_petit = indice
    gauche = 2 * indice + 1
    droit = 2 * indice + 2
    if gauche < taille and tas[gauche] < tas[plus_petit]:
        plus_petit = gauche
    if droit < taille and tas[droit] < tas[plus_petit]:
        plus_petit = droit
    if plus_petit != indice:
        tas[indice], tas[plus_petit] = tas[plus_petit], tas[indice]
        entasser(tas, plus_petit, taille)
    return tas

def UnionTasTableau(tas1: list, tas2: list):
    tas_concatene = tas1 + tas2
    union_tas = ConstructionTasTableau(tas_concatene)
    return union_tas

def SupprMinTasTableau(t):
    s = len(t) - 1
    e = t[s]
    t.pop() 
    i = 0
    while (2 * i + 1 < s and e > t[2 * i + 1]) or (2 * i + 2 < s and e > t[2 * i + 2]):
        if 2 * i + 2 < s and t[2 * i + 1] > t[2 * i + 2]:
            t[i] = t[2 * i + 2]
            i = 2 * i + 2
        else:
            t[i] = t[2 * i + 1]
            i = 2 * i + 1
    t[i] = e
    return t

### GRAPH

def analyse_complexite():
    X = ["1000","5000", "10000","20000"]
    time_total = []
    for title in X:
        times = []
        for i in range(1, 6):
            name = f"./cles_alea/jeu_{i}_nb_cles_{title}.txt"
            with open(name) as f:
                keys = []
                for line in f:
                    bin_key = bin(int(line.strip(), 16))[2:]
                    keys.append([int(bin_key[i:i+32],2) for i in range(0, len(bin_key), 32)])
                start = time.time()
                arbre_bin.ajoutsIteratifs(keys)
                end = time.time()
                time_elapsed = end - start
                times.append(time_elapsed)
        time_total.append(times)
        print("Key:", title)
    time_means = [np.mean(time_total[i]) for i in range(len(time_total))]
    plot_graph(X, time_means)
    pass

def analyse_complexite_union():
    # X = ["1000","5000", "10000","20000","50000","80000","120000","200000"]
    test = [["1000","5000"], ["50000", "10000"], ["20000","50000"],["80000","120000"], ["5000", "200000"]]
    time_total = []
    for title in test:
        # times = []
        keys = []
        for i in range(2):
            name = f"./cles_alea/jeu_{1}_nb_cles_{title[i]}.txt"
            # inner_keys = []
            file_binom = file_bin.FileBinomiale()
            with open(name) as f:
                for line in f:
                    bin_key = bin(int(line.strip(), 16))[2:]
                    storing_key = [int(bin_key[i:i+32],2) for i in range(0, len(bin_key), 32)]
                    # inner_keys.append([int(bin_key[i:i+32],2) for i in range(0, len(bin_key), 32)])
                    file_binom.ajout(storing_key)
            keys.append(file_binom)
        start = time.time()
        keys[0].union(keys[0])
        end = time.time()
        print(start, end)
        time_elapsed = end - start
        # times.append(time_elapsed)
        time_total.append(time_elapsed)
        print("Key:", title)
    print(time_total)
    # time_means = [np.mean(time_total[i]) for i in range(len(time_total))]
    # X = ["2000","10000", "20000","40000","100000","160000","240000","400000"]
    test_sum = [sum([int(item[0]), int(item[1])]) for item in test]
    plot_graph(test_sum, time_total)
    pass

def plot_graph(X, Y):
    plt.plot(X, Y, color="b", alpha=0.7)
    plt.scatter(X, Y, color="b", marker="x", alpha=0.9, label="Moyenne effectuée")
    # plt.ylim([0, 0.4])
    plt.xlabel('Nombre de données aléatoires')
    plt.ylabel('Temps écoulé pour obtenir un tas min (s)')
    plt.legend()
    plt.show()
    pass

### FONCTIONS SIMPLES

def inf(cle1: list, cle2: list) -> bool:
    l = len(cle1)
    for i in range(l):
        if cle1[i] > cle2[i]:
            return False
    return True


def eg(cle1: list, cle2: list) -> bool:
    l = len(cle1)
    for i in range(l):
        if cle1[i] != cle2[i]:
            return False
    return True

def afficherTas(tas):
    if tas == []:
        print("Le tas est vide")
        return
    profondeur=0
    ite=0
    fin=False
    while not fin:
        for _ in range(2**profondeur):
            if ite<len(tas):
                if type(tas[ite]) == int:
                    print(tas[ite],end=" ")
                else: 
                    print(tas[ite].val,end=" ")
            else:
                fin=True
            ite+=1
        print("")
        profondeur+=1


cles_originales = [0x298a6eedbec6631579f09930fcf8e175, 0x1573c8d156d03e633c20c36f1b70862, \
                   0x2c15aed1a9eab93338d0348f12ef9a3b, 0x5f003a2587337655af8a166be8439a49, \
                   0xd192acf4c06fe7c7df042f07d290bdd4, 0xdf5d8018d0af5d1a979d449c91282bfc]
cles_binary = [bin(item)[2:] for item in cles_originales]




bin7 = bin(0xdf6943ba6d51464f6b02157933bdd9ad)[2:]
nouveau_noeud = [int(bin7[i:i+32],2) for i in range(0, len(bin7), 32)]


### Liste de int comme parametre d'entre
ordered_tree = [1,5,7,10,16,20,26,34,40]
unordered_tree = [7,40,1,16,10,34,26,20,5]
other_list = [6,8,14,4,18]

### Liste de liste de 4 entiers non signes pour les cles de 128 bits 
cles_4_entiers = [[int(item[i:i+32],2) for i in range(0, len(item), 32)] for item in cles_binary]

#### Test avec la structure tableau

# print("Ajouts Iteratifs Tas Min Tableau:")
# afficherTas(AjoutsIteratifsTableau(ordered_tree)) # prend une liste de int ou une list de liste de int
# print("------")
# print("Min Suppr Tas Min Tableau:")
# afficherTas(SupprMinTasTableau(ordered_tree)) # prend une liste de int
# print("------")
# print("Ajout Tas Min Tableau:")
# afficherTas(AjoutTasTableau(ordered_tree, 2))
# print("------")
# print("Union Tas Min Tableau:")
# afficherTas(UnionTasTableau(ordered_tree, ordered_tree))
# print("------")
# print("Construction Tas Min Tableau:")
# afficherTas(ConstructionTasTableau(unordered_tree))

#### Test complexite
analyse_complexite()
# analyse_complexite_union()

#### Test avec la structure arbre binaire (donc on est plus dans un tas min là vu que l'on compare les valeurs
# avec à droite les valeurs superieurs et a gauche les valeurs inferieurs, où le min sera tout à gauche)

# abr = arbre_binaire.ABR()
# for item in unordered_tree:
#     abr.AjoutIteratif(item)
# abr.Ajout(abr.root, 19)
# abr.SupprMin(abr.root)
# print(abr.Search(1)) ## 1 est le minimum et cela va renvoyer faux car il vient d'être supprimé
# print(abr.NbNoeudsSansRacine(abr.root))

# abr2 = arbre_binaire.ABR()
# for item in other_list:
#     abr2.AjoutIteratif(item)
# tas_concatene = arbre_binaire.ABR().UnionTasAB(abr.root, abr2.root)

# print(abr.NbNoeudsSansRacine(tas_concatene)) # le nombre de noeuds est passé de 8 à 13
