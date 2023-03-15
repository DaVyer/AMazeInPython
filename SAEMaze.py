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
            self.neighbors[c1].add(c2)
            self.neighbors[c2].add(c1)         # on le retire
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
                reachable.append(c1)
        return reachable

    def get_cells(self):
        cells = []

        for i in range(0, self.height):
            for j in range(0, self.width):
                cells.append((i, j))
        
        return cells


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

    @classmethod
    def gen_wilson(cls, h, w):
        """
        Cette fonction génère un labyrinthe en utilisant l’algorithme de Wilson

        Paramètres: h : Hauteur du labyrinthe.
                    w: Largeur du labyrinthe.

        Valeur de retour : La fonction retourne une instance de labyrinthe générée avec l'algorithme de Wilson.
        """
        #Initialisation : création d’un labyrinthe plein
        laby = cls(h, w, empty=False)
        #Choisir une cellule au hasard sur la grille et la marquer
        randomCell = choice(laby.get_cells())
        mark = {randomCell}
        #Tant qu’il reste des cellules non marquées :
        while len(mark) != len(laby.get_cells()):
            #Choisir une cellule de départ au hasard, parmi les cellules non marquées
            startCell = choice(list(set(laby.get_cells()) - mark))
            #Effectuer une marche aléatoire jusqu’à ce qu’une cellule marquée soit atteinte
            path = [startCell]
            while startCell not in mark:
                startCell = choice(laby.get_contiguous_cells(startCell))
                if startCell in path:
                    path = path[:path.index(startCell)+1]
                else:
                    path.append(startCell)
            #Marquer chaque cellule du chemin, et casser tous les murs rencontrés, jusqu’à la cellule marquée
            for j in range(len(path)-1):
                laby.remove_wall(path[j], path[j+1])
            mark.update(path)
        return laby

    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, 
        d'un labyrinthe avec du contenu dans les cellules
        Argument:
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour:
            string
        """
        if content is None:
            content = {(i,j):' ' for i in range(self.height) for j in range(self.width)}
        else:
            # Python >=3.9
            #content = content | {(i, j): ' ' for i in range(
            #    self.height) for j in range(self.width) if (i,j) not in content}
            # Python <3.9
            new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i,j) not in content}
            content = {**content, **new_content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += " "+content[(0,j)]+" ┃" if (0,j+1) not in self.neighbors[(0,j)] else " "+content[(0,j)]+"  "
        txt += " "+content[(0,self.width-1)]+" ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " "+content[(i+1,j)]+" ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else " "+content[(i+1,j)]+"  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt

    def solve_dfs(self, start, stop):
        """
        Cette fonction renvoie le chemin reliant deux cellules du labyrinthe en utilisant l'algorithme de parcours en profondeur DFS.

        Paramètres: self (Labyrinth): Instance du labyrinthe.
                    start (tuple): Coordonnées de la cellule de départ.
                    stop (tuple): Coordonnées de la cellule d'arrivée.

        Valeur de retour : pathCell (list): La liste de coordonnées représentant le chemin entre les deux cellules.
        """
        #Placer D dans la struture d’attente (file ou pile) et marquer D
        pile=[start]
        mark=[start]
        #Mémoriser l’élément prédécesseur de D comme étant D
        pred={start : start}
        nbCell = len(self.get_cells())
        #Tant qu’il reste des cellules non-marquées :
        while len(mark) != nbCell:
            #Prendre la « première » cellule et la retirer de la structure (appelons c, cette cellule)
            cell = pile.pop()
            #Si c correspond à A :
            if cell == stop:
                #C’est terminé, on a trouvé un chemin vers la cellule de destination
                break
            #Sinon
            else:
                #Pour chaque voisine de c :
                for neighbor in self.get_reachable_cells(cell):
                    #Si elle n’est pas marquée :
                    if neighbor not in mark:
                        #La marquer
                        mark.append(neighbor)
                        #La mettre dans la structure d’attente
                        pile.append(neighbor)
                        #Mémoriser son prédécesseur comme étant c
                        pred[neighbor] = cell
        # Reconstruction du chemin à partir des prédécesseurs
        pathCell = []
        #Initialiser c à A
        cell = stop
        #Tant que c n’est pas D :
        while cell != start:
            #ajouter c au chemin
            pathCell.append(cell)
            #mettre le prédécesseur de c dans c
            cell = pred[cell]
        #Ajouter D au chemin
        pathCell.append(start)
        return pathCell

    def solve_bfs(self,start, stop):
        """
        Cette fonction renvoie le chemin reliant deux cellules du labyrinthe en utilisant l'algorithme de parcours en largeur BFS.

        Paramètres: self (Labyrinth): Instance du labyrinthe.
                    start (tuple): Coordonnées de la cellule de départ.
                    stop (tuple): Coordonnées de la cellule d'arrivée.

        Valeur de retour : pathCell (list): La liste de coordonnées représentant le chemin entre les deux cellules.
        """
        #Placer D dans la struture d’attente (file ou pile) et marquer D
        pile=[start]
        mark=[start]
        #Mémoriser l’élément prédécesseur de D comme étant D
        pred={start : start}
        nbCell = len(self.get_cells())
        #Tant qu’il reste des cellules non-marquées :
        while len(mark) != nbCell:
            #Prendre la « première » cellule et la retirer de la structure (appelons c, cette cellule)
            cell = pile.pop()
            #Si c correspond à A :
            if cell == stop:
                #C’est terminé, on a trouvé un chemin vers la cellule de destination
                break
            #Sinon
            else:
                #Pour chaque voisine de c :
                for neighbor in self.get_reachable_cells(cell):
                    #Si elle n’est pas marquée :
                    if neighbor not in mark:
                        #La marquer
                        mark.append(neighbor)
                        #La mettre dans la structure d’attente
                        pile.append(neighbor)
                        #Mémoriser son prédécesseur comme étant c
                        pred[neighbor] = cell

        # Reconstruction du chemin à partir des prédécesseurs
        pathCell = []
        #Initialiser c à A
        cell = stop
        #Tant que c n’est pas D :
        while cell != start:
            #ajouter c au chemin
            pathCell.append(cell)
            #mettre le prédécesseur de c dans c
            cell = pred[cell]
        #Ajouter D au chemin
        pathCell.append(start)
        return pathCell
    
    #Pour l'algorithme de la main droite, voilà jusqu'ou je suis arrivé, j'arrive à récupéré chaque cellule de droite puis d'en bas etc... mais en cas de cul-de-sac je ne vois pas
    #comment retourner en arrière. J'avais bien comme idée de créer une liste pointage et à chaque fois qu'on arrivait à un carrefour, rajouter la cellule à la liste et en cas de 
    #cul-de-sac revenir sur ce pointage et condamné le chemin emprunté, mais je ne vois pas comment l'implémenter.

    """
    def solve_rhr(self, start, stop):
        #initialiser le chemin à start
        chemin = [start]
        culDeSac = []
        cell = chemin[0]
        marquee = [cell]
        pointage = []
        while len(chemin) != len(self.get_cells()):
        for i in range(20):
            c = self.get_coord(cell)
            if self.get_reachable_cells(cell) not in culDeSac:
                if len(self.get_reachable_cells(cell)) >= 2:
                        pointage.append(cell)

                if (c[0], c[1]-1) in self.get_reachable_cells(cell) and (c[0], c[1]-1) not in culDeSac and (c[0], c[1]-1) not in marquee: #Pour aller sur la case de gauche
                    cell = (c[0], c[1]-1)
                    marquee.append(cell)
                    
                    print("je passe dans le premier", marquee, cell)

                elif (c[0]+1, c[1]) in self.get_reachable_cells(cell) and (c[0]+1, c[1]) not in culDeSac and (c[0]+1, c[1]) not in marquee: #Pour aller sur la case d'en bas
                    
                    cell = (c[0]+1, c[1])
                    marquee.append(cell)
                    print("je passe dans le deuxième", marquee, cell, pointage)

                elif (c[0], c[1]+1) in self.get_reachable_cells(cell) and (c[0], c[1]+1) not in culDeSac and (c[0], c[1]+1) not in marquee: #Pour aller sur la case de droite
                    
                    cell = (c[0], c[1]+1)
                    marquee.append(cell)
                    print("je passe dans le troisième", marquee, cell)

                elif (c[0]-1, c[1]) in self.get_reachable_cells(cell) and (c[0]-1, c[1]) not in culDeSac and (c[0]-1, c[1]) not in marquee: #Pour aller sur la case en haut
                    
                    cell = (c[0]-1, c[1])
                    marquee.append(cell)
                    print("je passe dans le quatrième", marquee, cell)

            else:
                culDeSac+=marquee
                while marquee[:-1] != pointage[:-1]:
                    
                    print(marquee.pop())
                    marquee.pop()
                    pointage.pop()
                print("je passe dans le else", marquee, len(marquee)-1, cell, culDeSac, pointage)
        print(marquee, ",",culDeSac)
        chemin += marquee    
        return chemin
    """                

    def distance_geo(self, c1, c2):
        """
        Cette fonction calcule la distance géodésique entre deux cellules `c1` et `c2` dans le labyrinthe.
        
        Paramètres: self: l'instance de la classe Labyrinthe
                    c1 (tuple): les coordonnées de la première cellule
                    c2 (tuple): les coordonnées de la deuxième cellule
            
        Valeur de retour :  str : une chaîne de caractères décrivant la distance géodésique entre `c1` et `c2`.
                            La distance géodésique est calculée en utilisant l'algorithme de parcours en profondeur
                            pour trouver le chemin le plus court entre `c1` et `c2`.
        """
        distGeo = len(self.solve_dfs(c1, c2))
        res = f"La distance Géodésique du labyrinthe est : {distGeo}"
        return res

    def distance_man(self, c1, c2):
        """
        Cette fonction calcule la distance de Manhattan entre deux cellules dans le labyrinthe.

        Paramètres: self: instance de la classe Labyrinthe
                    c1 (tuple): coordonnées (x, y) de la première cellule
                    c2 (tuple): coordonnées (x, y) de la seconde cellule

        Valeur de retour : res (str): la distance de Manhattan du labyrinthe entre les deux cellules données `c1` et `c2`.
        """
        #Calcul des distances horizontale et verticale séparant c1 et c2
        distHori = abs(c1[0] - c2[0])
        distVerti = abs(c1[1] - c2[1])
        # Calcul de la distance de Manhattan en additionnant les distances horizontale et verticale
        distMan = distHori + distVerti 
        res = f"La distance de Manhattan du labyrinthe est : {distMan}"
        return res
    