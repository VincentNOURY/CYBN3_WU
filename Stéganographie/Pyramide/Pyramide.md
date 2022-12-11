# Pyramide

## Consigne


## Résolution

En utilisant l'outil binwalk, on peu observer que cette image en contient en réalité autre chose.

On utilisera donc la commande suivant pour extraire tout ce qui pourrait se trouver dedans
```
binwalk -e triforce.png
```

On retrouve dans le dossier d'extraction une autre image cette fois-ci avec des cases rouges.

En notant les lettres correspondant aux cases rouges, on obtient VOUS NE SORTIREZ JAMAIS D.

Maintenant 2 options :
 1. Vous connaissez vos classiques et vous reconnaissez la phrase "Vous ne sortirez jamais d'ici, étrangers! Ce tombeau sera votre tombeau".
 2. Vous ne conaissez pas vos classiques

Dans le cas 1 vous cherchez la phrase sur google et vous trouvez 2 noms Tournevis et Nexusis (/!\ Attention c'est le second qui est le flag).

Dans le cas 2 vous pouvez chercher le bout de phrase que vous avez cela suffira, cependant il existe une rotation de l'image permettant de trouver la suite de la citation.


TODO : Illustrer
