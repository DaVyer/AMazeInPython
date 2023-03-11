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
    
        


