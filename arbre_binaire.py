class ABNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class ABR:
    def __init__(self):
        self.root = None

    def AjoutIteratif(self, key):
        if self.root is None:
            self.root = ABNode(key)
        else:
            self.Ajout(self.root, key)

    def Ajout(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = ABNode(key)
                node.left.parent = node
            else:
                self.Ajout(node.left, key)
        else:
            if node.right is None:
                node.right = ABNode(key)
                node.right.parent = node
            else:
                self.Ajout(node.right, key)
        

    def Search(self, key):
        return self.SearchRecursif(self.root, key)

    def SearchRecursif(self, node, key):
        if node is None or node.key == key:
            return node is not None
        elif key < node.key:
            return self.SearchRecursif(node.left, key)
        else:
            return self.SearchRecursif(node.right, key)
        
    def SupprMin(self, node):
        if node.left is not None: 
            self.SupprMin(node.left)
        else:
            node.parent.left = None
            node.parent = None
        pass

    def UnionTasAB(self, tas1, tas2):
        if not tas1:
            return tas2
        if not tas2:
            return tas1
        if tas1.key > tas2.key:
            tas1, tas2 = tas2, tas1
        tas1.right = self.UnionTasAB(tas1.right, tas2)
        if tas1.left is None or (tas1.right is not None and tas1.right.key < tas1.left.key):
            tas1.left, tas1.right = tas1.right, tas1.left
        return tas1

    def NbNoeudsSansRacine(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.NbNoeudsSansRacine(node.left) + self.NbNoeudsSansRacine(node.right)


