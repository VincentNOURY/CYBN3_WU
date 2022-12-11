# J'ai pas ROTé.

## Consigne

votre collègue, adepte de blagues plus que de cryptographie, vous envoie la phrase suivante dans la conversation d'équipe: "j'vous promets les gars, cette fois, j'ai pas ROTé: 871 1157 858 1014 1599 1287 507 663 1508 1261 1365 1508 1235 1456 676 1495 1235 637 1235 1287 663 1495 1261 1482 1625"


## Résolution

Pour ce challenge, tout le monde à pensé au ROT-13, cependant ce n'était pas utile pour résoudre ce challenge. Où était-ce ?

En effet, il fallait remarquer que chacun de ces chiffres étaient un multiple de 13.

Donc en divisant chacun par 13, on obtient la suite suivante : 67 89 66 78 123 99 39 51 116 97 105 113 95 112 52 115 95 49 95 99 51 115 97 114 125

En utilisant le conversion de la table ASCII, on obtient donc : CYBN{c'3taiq_p4s_1_c3sar}
