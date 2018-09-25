#!/usr/bin/env python3
"""
Exemple d’utilisation du module SVG.
Dans cet exemple, on écrit le code SVG sur la sortie standard, qui
doit donc être redirigée vers un fichier pour pouvoir afficher
l’image.
"""
import svg

def main():
    """ fonction de test """
    print(svg.ouverture_image(800, 620))
    # au début on dessine en noir et sans remplissage
    print(svg.polygone("500,500 500,600 600,600 600,500"))
    print(svg.cercle(550, 550, 20))
    print(svg.texte(500, 450, "Sans remplissage", 30))
    orange = svg.couleur(255, 128, 0)
    # lignes oranges et épaisses de 3, remplissage vert :
    print(svg.ouverture_groupe(orange, "green", 3))
    # ce segment orange va masquer ce qui se trouve en-dessous :
    print(svg.segment(510, 510, 700, 600))
    # les objets de ce groupe ne masqueront pas totalement ce qui a
    # été dessiné avant :
    print(svg.ouverture_groupe_transparent(0.3))
    print(svg.cercle(450, 510, 70))
    # groupe pour uniquement colorier sans tracer les traits :
    print(svg.ouverture_groupe("none", "red", 0))
    # du coup ce segment sera invisible
    # (pas d’intérieur, et trait non tracé) :
    print(svg.segment(10, 10, 1000, 1000)) # invisible
    print(svg.texte(300, 500, "Rouge et transparent", 50))
    # les objets appartenant au même groupe transparent se masquent
    # entre eux donc cette zone bleue cache un morceau du rond vert
    # (mais ne masque pas le carré et le cercle noirs du début) :
    print(svg.colorie_zone(450, 500, 100, 100, "blue"))
    print(svg.fermeture_groupe()) # fin du groupe rouge
    # nouveau segment orange mais celui-ci appartient au groupe
    # transparent :
    print(svg.segment(510, 530, 700, 630))
    print(svg.fermeture_groupe()) # fin du groupe transparent
    # ce polygone dépasse de l’image donc on ne le voit pas en entier :
    print(svg.polygone("480,500 500,480 530,540 550,700 520,560"))
    # texte avec contour et remplissage :
    print(svg.texte(10, 100, "Vert à bords orange", 100))
    # on doit fermer tous les groupes avant de refermer l’image :
    print(svg.fermeture_groupe()) # fin du groupe orange et vert
    print(svg.fermeture_image())

main()
