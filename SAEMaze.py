from random import *

class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """
    def __init__(self, height, width, empty):
        """
        Constructeur d'un labyrinthe de height cellules de haut 
        et de width cellules de large 
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height    = height
        self.width     = width
        self.neighbors = {(i,j): set() for i in range(height) for j in range (width)}
        if empty:
            for i in range(height):
                for j in range(width):
                    if i > 0:
                        self.neighbors[(i,j)].add(((i-1),j))
                    if i < height - 1:
                        self.neighbors[(i,j)].add(((i+1),j))
                    if j > 0:
                        self.neighbors[(i,j)].add((i,(j-1)))
                    if j < width -1:
                        self.neighbors[(i,j)].add((i,(j+1)))
    def info(self):
        """
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = f"{self.height} x {self.width}\n"
        txt += str(self.neighbors)
        return txt

    def __str__(self):
        """
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += "   ┃" if (0,j+1) not in self.neighbors[(0,j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
            0 <= c1[1] < self.width and \
            0 <= c2[0] < self.height and \
            0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:      # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2) # on le retire
        if c1 in self.neighbors[c2]:      # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1) # on le retire
    

    def fill(self):
        """
        Cette fonction initialise l'attribut "neighbors" pour l'objet qui appelle cette fonction. 
        Les voisins sont stockés sous forme d'un dictionnaire où chaque clé représente un tuple (i, j) 
        qui correspond aux coordonnées d'une cellule dans une matrice de dimensions height x width. 
        La valeur associée à chaque clé est un ensemble vide.

        Paramètres: Aucun

        Valeurs de retour: None: Cette fonction ne renvoie rien. 
        Elle met simplement à jour l'attribut "neighbors" de l'objet qui l'appelle.
        """
        self.neighbors = {(i,j): set() for i in range(self.height) for j in range (self.width)}               
        return None


    def remove_wall(self, c1, c2):
        """
        Cette fonction supprime un mur entre deux cellules spécifiées par les coordonnées c1 et c2. 
        Les coordonnées doivent être "valides" (Elles doivent être comprises entre 0 et la hauteur 
        ou la largeur du labyrinthe moins 1 inclus. 
        Si les coordonnées ne sont pas valides, une erreur sera levée avec un message indiquant 
        quelles sont les coordonnées invalides.

        Paramètres:

        c1: Un tuple représentant les coordonnées de la première cellule (c1[0] correspond à la ligne et c1[1] correspond à la colonne).
        c2: Un tuple représentant les coordonnées de la deuxième cellule (c2[0] correspond à la ligne et c2[1] correspond à la colonne).

        Valeurs de retour: None: Cette fonction ne renvoie rien. 
        Elle modifie l'attribut "neighbors" de l'objet qui l'appelle.

        Variables:

        self: L'objet qui appelle cette fonction.
        c1: Un tuple représentant les coordonnées de la première cellule.
        c2: Un tuple représentant les coordonnées de la deuxième cellule.
        """
        assert 0 <= c1[0] < self.height and \
            0 <= c1[1] < self.width and \
            0 <= c2[0] < self.height and \
            0 <= c2[1] < self.width, \
            f"Erreur lors de la suppression d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        if c2 not in self.neighbors[c1]:      # Si c2 est dans les voisines de c1
            self.neighbors[c1].add(c2)        # on le retire
        return None


    def empty(self):
        """
        Cette fonction remplit le dictionnaire de voisins pour toutes les cellules de la grille.
        Pour chaque cellule de la grille, la fonction ajoute tous les voisins possibles 
        (cellules adjacentes) dans le dictionnaire de voisins de cette cellule.
        
        Paramètres: self (obj): L'instance de la classe contenant les attributs de grille à utiliser.

        Variables: Aucune.
            
        Valeurs de retour: None: Cette fonction ne renvoie rien.
        """
        for i in range(self.height):
                for j in range(self.width):
                    if i > 0:
                        self.neighbors[(i,j)].add(((i-1),j))
                    if i < self.height - 1:
                        self.neighbors[(i,j)].add(((i+1),j))
                    if j > 0:
                        self.neighbors[(i,j)].add((i,(j-1)))
                    if j < self.width -1:
                        self.neighbors[(i,j)].add((i,(j+1)))              
        return None


    def get_walls(self):
        """
        Cette fonction retourne une liste de tuples représentant les murs 
        présents entre les cellules de la grille.

        Paramètres: self (obj): l'instance de la classe contenant les attributs de grille à utiliser

        Variables: Aucune.
        
        Valeurs de retour: Une liste de tuples(mark), chaque tuple représentant un mur entre deux cellules de la grille.
        Les éléments de chaque tuple sont des tuples de coordonnées (i, j), où i est la ligne et j est la colonne.   
        """
        mark=[]
        for c1 in self.neighbors.keys():
            if c1[1] < self.width-1 and (c1[0],c1[1]+1) not in self.neighbors[c1]:
                mark.append((c1,(c1[0],c1[1]+1)))
            if c1[0] < self.height-1 and (c1[0]+1,c1[1]) not in self.neighbors[c1]:
                mark.append((c1,(c1[0]+1,c1[1])))           
        return mark

    def get_contiguous_cells(self, c):
        """
        Cette fonction prend en entrée une coordonnée c et retourne une liste de coordonnées adjacentes à c 
        dans une grille de dimensions self.height x self.width.

        Paramètres: self (obj): l'instance de la classe contenant les attributs de grille à utiliser
                    c: Une coordonnée dans la grille, sous la forme d'un tuple (x, y).

        Variables: Aucune.

        Valeurs de retour: La fonction retourne une liste de tuples 
        représentant les coordonnées adjacentes à c dans la grille.
        """
        contigues = []
        if c[0]-1 >= 0:
            contigues.append((c[0]-1, c[1]))
        if c[0]+1 < self.height:
                contigues.append((c[0]+1, c[1]))
        if c[1]-1 >= 0:
                contigues.append((c[0], c[1]-1))
        if c[1]+1 < self.width:
                contigues.append((c[0], c[1]+1))
        return contigues

    def get_reachable_cells(self, c):
        """
        Cette fonction prend en entrée une coordonnée c et retourne une liste de coordonnées adjacentes à c 
        dans une grille de dimensions self.height x self.width qui sont également accessibles à partir de c.

        Paramètres: self (obj): l'instance de la classe contenant les attributs de grille à utiliser
                    c: Une coordonnée dans la grille, sous la forme d'un tuple (x, y).

        Variables: Aucune.

        Valeurs de retour: La fonction retourne une liste de tuples représentant les coordonnées 
        adjacentes à c dans la grille qui sont également accessibles à partir de c.
        """
        reachable=[]
        for c1 in self.get_contiguous_cells(c):
            if c1 in self.neighbors[c]:
                reachable.append(c)
        return reachable


    @classmethod
    def gen_btree(cls, h, w):
        """
        Cette fonction génère un labyrinthe en utilisant l'algorithme de l'arbre binaire.

        Paramètres: h : Hauteur du labyrinthe.
                    w: Largeur du labyrinthe.
        
        Variables: Aucune.

        Valeurs de retour: La fonction retourne une instance de labyrinthe générée avec l'algorithme de l'arbre binaire.
        """
        #Initialisation : un labyrinthe plein (contenant tous les murs possibles) Pour chaque cellule du labyrinthe :
        #Supprimer aléatoirement le mur EST ou le mur SUD (s’il n’en possède qu’un, supprimer ce mur ; s’il n’en possède aucun des deux, ne rien faire)
        laby = cls(h, w, empty=False)
        for i in range(h-1):
            for j in range(w-1):
                res = randint(0,1)
                #supprime le mur EST si on est pas sur la derniere colonne
                if res == 0 and i < h-1:
                    laby.remove_wall((i,j),(i+1,j))
                #supprime le mur SUD si on est pas sur la derniere ligne
                elif res == 1 and j < w-1:
                    laby.remove_wall((i,j),(i,j+1))
                else:
                    continue
        for x in range(0, w):
            if x+1 < w:
                laby.remove_wall((x, w-1), (x+1, w-1))
        for y in range(0, h):
            if y+1 < h :
                laby.remove_wall((h-1, y), (h-1, y+1))
        return laby

    @classmethod
    def gen_sidewinder(cls, h, w):
        """
        Cette fonction génère un labyrinthe en utilisant l'algorithme Sidewinder.

        Paramètres: h : Hauteur du labyrinthe.
                    w: Largeur du labyrinthe.

        Valeurs de retour: La fonction retourne une instance de labyrinthe générée avec l'algorithme Sidewinder.
        """
        #Initialisation : création d’un labyrinthe plein
        laby = cls(h, w, empty=False)
        #Pour i allant de 0 à hauteur-2 :
        for i in range(h-1):
            #Initialiser une variable séquence comme liste vide
            sequence=[]
            #Pour j allant de 0 à largeur-2 :
            for j in range(w-1):
                #Ajouter la cellule (i, j) à la séquence
                sequence.append((i,j))

                #Tirer à pile ou face :
                res = randint(0,1)

                #Si c’est pile : Casser le mur EST de la cellule (i, j)
                if res == 0:
                    laby.remove_wall((i,j),(i,j+1))

                 #Si c’est face :
                else:
                    #Casser le mur SUD d’une des cellules (choisie au hasard) qui constituent le séquence qui vient d’être terminée.
                    cell = choice(sequence)
                    laby.remove_wall((cell[0], cell[1]), (cell[0]+1, cell[1]))

                    #Réinitialiser la séquence à une liste vide
                    sequence = []

            #Ajouter la dernière cellule à la séquence
            sequence.append((i, w-1))

            #Tirer une cellule au sort dans la séquence et casser son mur SUD
            randCell = choice(sequence)
            laby.remove_wall((randCell[0], randCell[1]), (randCell[0]+1, randCell[1]))

        #Casser tous les murs EST de la dernière ligne
        for y in range(0, h):
            if y+1 < h :
                laby.remove_wall((h-1, y), (h-1, y+1))
        #Retourner le labyrinthe
        return laby

    @classmethod
    def gen_fusion(cls, h, w):
        """
        Cette fonction génère un labyrinthe n utilisant l'algorithme de génération de labyrinthe par fusion.

        Paramètres : h : Hauteur du labyrinthe.
                    w: Largeur du labyrinthe.

        Valeur de retour : La fonction retourne une instance de labyrinthe générée avec l'algorithme de fusion.

        laby : un objet Labyrinth représentant le labyrinthe généré.
        """
        #Initialisation : création d’un labyrinthe plein
        laby = cls(h, w, empty=False)

        #on labélise les cellules de 1 à n
        compteur = 1
        labelle_cellule = {}
        for i in laby.neighbors.keys():
            labelle_cellule[i] = compteur
            compteur+=1

        #on extrait la liste de tous les murs et on les « mélange » (on les permute aléatoirement)
        walls = laby.get_walls()
        shuffle(walls)

        #Si les deux cellules séparées par le mur n’ont pas le même label :
        for tupleWall in walls:
            if labelle_cellule[tupleWall[0]] != labelle_cellule[tupleWall[1]]:
                laby.remove_wall(tupleWall[0], tupleWall[1])
                
                #affecter le label de l’une des deux cellules, à l’autre, et à toutes celles qui ont le même label que la deuxième
                sameLabel = []
                for cell in labelle_cellule.keys():
                    if labelle_cellule[cell] == labelle_cellule[tupleWall[1]]:
                        sameLabel.append(cell)
                for cell in sameLabel:
                    labelle_cellule[cell] = labelle_cellule[tupleWall[0]]               

        return laby

    @classmethod
    def gen_exploration(cls, h, w):
        """
        Cette fonction génère un labyrinthe en utilisant l’algorithme d’exploration exhaustive

        Paramètres: h : Hauteur du labyrinthe.
                    w: Largeur du labyrinthe.

        Valeur de retour : La fonction retourne une instance de labyrinthe générée avec l'algorithme d’exploration exhaustive.
        """
        #Initialisation : création d’un labyrinthe plein
        laby = cls(h, w, empty=False)

        #Choisir une cellule au hasard
        randomCell = choice(list(laby.neighbors.keys()))

        #Marquer cette cellule comme étant visitée
        estVisiter = [randomCell]

        #Mettre cette cellule sur une pile
        pile = [randomCell]

        #Tant que la pile n’est pas vide :
        while len(pile) != 0: 

            #Prendre la cellule en haut de la pile et l’en retirer
            currentCell = pile[0]
            del pile[0]

            #Prendre les cellules contigues de la cellule actuelle et si elle sont pas visitées, les mettres dans une liste.
            notVisited = []
            for cell in laby.get_contiguous_cells(currentCell):
                if cell not in estVisiter:
                    notVisited.append(cell)
            
            #Si cette cellule a des voisins qui n’ont pas encore été visités :
            if notVisited:

                #La remettre sur la pile
                pile.insert(0, currentCell)

                #Choisir au hasard l’une de ses cellules contigües qui n’a pas été visitée
                contiguousNotVisited = choice(notVisited)

                #Casser le mur entre la cellule (celle qui a été dépilée) et celle qui vient d’être choisie
                laby.remove_wall(currentCell, contiguousNotVisited)
                laby.remove_wall(contiguousNotVisited, currentCell)

                #Marquer la cellule qui vient d’être choisie comme visitée et la mettre sur la pile
                estVisiter.append(contiguousNotVisited)
                pile.insert(0, contiguousNotVisited)


        return laby


    


    
        


