# Python3 module
"""
 module comprenant diverses fonctions pour générer des éléments SVG
 sous forme de chaînes.
 Ces chaînes doivent être écrites dans un fichier en respectant la
 structure SVG pour obtenir une image.
"""
def ouverture_image(largeur, hauteur):
    """
    génère la balise ouvrante pour décrire une image SVG des
    dimensions indiquées. Les paramètres sont des entiers.
    Remarque : l’origine est en haut à gauche et l’axe des Y est
    orienté vers le bas.
    """
    balise = "<svg xmlns='http://www.w3.org/2000/svg' version='{version}' " \
             "stroke='{lignes}' stroke-linecap='round' fill='{remplissage}' " \
             "width='{largeur}' height='{hauteur}'>"
    return balise.format(version="1.1",
                         # par défaut, lignes noires
                         lignes="black",
                         # et pas de remplissage
                         remplissage="none",
                         largeur=largeur,
                         hauteur=hauteur)
def fermeture_image():
    """
    génère la balise svg fermante. Doit être placée après tous les
    éléments de description de l’image, juste avant la fin du fichier.
    """
    return "</svg>"

def couleur(rouge, vert, bleu):
    """
    génère la référence d’une couleur.
    Les arguments doivent être entre 0 et 255
    """
    chaine = "#{R:02X}{V:02X}{B:02X}"
    return chaine.format(R=rouge, V=vert, B=bleu)

def ouverture_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    génère une balise ouvrante définissant un groupe d’éléments avec
    un style particulier.
    Chaque groupe ouvert doit être refermé individuellement et avant
    la fermeture de l’image.

    Les paramètres de couleur sont des chaînes et peuvent avoir les valeurs :
    -- "none" qui signifie rien (invisible) ;
    -- une référence obtenue par svg.couleur(rouge, vert, bleu) ;
    -- un nom de couleur reconnu, par exemple "red" ou "black".

    Le paramètre d’épaisseur est un nombre positif ou nul.
    """
    balise = "<g stroke='{ligne}' fill='{remplissage}' stroke-width='{epaisseur}'>"
    return balise.format(ligne=couleur_ligne,
                         remplissage=couleur_remplissage,
                         epaisseur=epaisseur_ligne)

def ouverture_groupe_transparent(niveau_opacite):
    """
    génère une balise ouvrant un groupe d’éléments qui, dans son
    ensemble, sera partiellement transparent. Les éléments qui
    composent le groupe se masquent les uns les autres dans l’ordre
    d’apparition (ils ne sont pas transparents entre eux).
    niveau_opacite doit être un nombre entre 0 et 1.
    Ce groupe doit être refermé de la même manière que
    les groupes définissant un style.
    """
    balise = "<g opacity='{niveau}'>"
    return balise.format(niveau=niveau_opacite)

def fermeture_groupe():
    """
    génère la balise fermante pour un groupe d’éléments
    """
    return "</g>"

def colorie_zone(x_min, y_min, largeur, hauteur, couleur_remplissage):
    """
    génère un élément qui colorie une zone rectangulaire
    de la couleur indiquée
    """
    balise = "<rect x='{xm}' y ='{ym}' width='{l}' height='{h}'" + \
             " stroke='none' fill='{coul}' />"
    return balise.format(xm=x_min,
                         ym=y_min,
                         l=largeur,
                         h=hauteur,
                         coul=couleur_remplissage)

def segment(x_dep, y_dep, x_arr, y_arr):
    """
    génère un élément SVG représentant un segment. Ce segment relie
    les points de coordonnées (x_dep, y_dep) et (x_arr, y_arr).
    """
    balise = "<line x1='{x1}' x2='{x2}' y1='{y1}' y2='{y2}' />"
    return balise.format(x1=x_dep,
                         y1=y_dep,
                         x2=x_arr,
                         y2=y_arr)

def cercle(x_centre, y_centre, rayon):
    """
    génère un élément SVG représentant un cercle (ou un disque, cela
    dépend de la couleur de remplissage du groupe où l’on se trouve)
    """
    balise = "<circle cx='{x}' cy='{y}' r='{r}' />"
    return balise.format(x=x_centre,
                         y=y_centre,
                         r=rayon)

def polygone(coordonnees_points):
    """
    génère un élément SVG représentant un polygone.
    coordonnees_points est une chaîne qui contient des paires de coordonnées
    séparées par des espaces. Les paires de coordonnées sont deux
    nombres séparés par une virgule.
    Par exemple, pour un triangle, coordonnees_points est de la forme
    "x1,y1 x2,y2 x3,y3"
    """
    balise = "<polygon points='{coordonnees}' />"
    return balise.format(coordonnees=coordonnees_points)

def texte(x_min, y_bas, contenu, hauteur):
    """
    place le texte à la position indiquée.
    x_min est l’abscisse du début du texte.
    y_bas est l’ordonnée de la ligne de base du texte (le bas d’une
    lettre telle que “n”). Attention, ce n’est pas l’ordonnée maximale
    puisque certaines lettres descendent sous cette ligne (g, j, p, q, y).
    Le paramètre hauteur définit la taille de police
    (c’est-à-dire la hauteur d’une ligne de texte)
    """
    balise_ouvrante = "<text x='{x}' y='{y}' font-size='{hauteur}'>"
    balise_fermante = "</text>"
    return (balise_ouvrante.format(x=x_min, y=y_bas, hauteur=hauteur)
            + contenu + balise_fermante)
