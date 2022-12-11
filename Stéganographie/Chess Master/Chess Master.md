# Chess Master

## Consigne

Juste des parties d'échecs, rien de suspect ici...

## Résolution

Dans le fichier zip on retrouvait plusieurs parties d'échec, plutot que de simplement tester tous les fichiers je vous propose une autre solution.

On sait que le flag sera de la forme CYBN{...}, par conséquent en utilisant un outil de stéganographie d'échec tel que 
[celui-ci](https://incoherency.co.uk/chess-steg/) on peut essayer de cacher CYBN{} et voir si l'on ne trouve pas quelque chose qui sortirait de l'ordinaire .

En cachant CYBN{} dans une partie d'échec, on obtient ce résultat
```
1. h4 g5 2. Nc3 f6 3. Na4 d6 4. Nh3 Bd7 5. Nf4 Bh6 6. Rb1 { Black resigns. } 1-0
```

On remarque une syntaxe qui est unique et que l'on ne retrouve pas dans les premiers fichiers de jeu d'échecs "{ Black resigns. }" il suffit donc de chercher 
quelquechose de similaire dans les fichiers mis a notre disposition.

Dans le fichier Johaness H Donner_vs_Paul Keres_1996...pgn on trouve ceci :
```
1. h3 e5 2. Nf3 h5 3. Ng1 Bc5 4. a3 d5 5. h4 Bd4 6. Nc3 Bxf2+ 7. Kxf2 Na6 8. g3
c5 9. a4 b5 10. e3 Qc7 11. Bd3 Qb6 12. Ke2 Qg6 13. Rh3 f5 14. Nf3 Ne7 15. Bc4
Qd6 16. Bb3 Kf8 17. a5 Be6 18. Ra2 Qd7 19. Qf1 Rg8 20. e4 Ke8 21. Ra3 Kf8 22.
Rh1 Rb8 23. Ra4 Rb7 24. Nxb5 Nc6 25. Ba2 f4 26. gxf4 Bf7 27. Ng1 Ke7 28. Ke1
Ncb4 29. f5 Rh8 30. b3 dxe4 31. Ra3 Bd5 32. d3 Rc7 33. Nh3 Ba8 34. Nd4 Nb8 35.
Nf4 Rg8 36. Rh3 Qa4 37. Rg3 Qxa5 38. Rf3 g5 39. Bb1 Bc6 40. Nd5+ Bxd5 41. Rf4
Rcc8 42. Nb5 Qxa3 43. Ba2 N8c6 44. Bb2 Qxa2 45. Kd2 Ke8 46. Ke3 Na5 47. Kf2 Bc6
48. Qa1 a6 49. hxg5 Nxb3 50. dxe4 Rd8 51. f6 Nc1 52. Kf3 Qa3+ 53. Nxa3 Kf8 54.
Qxc1 Ba4 55. Qg1 Na2 56. Qa1 Be8 57. Qh1 exf4 58. f7 Ra8 59. fxe8=Q+ Kxe8 60.
Kg2 f3+ 61. Kxf3 a5 62. Kf4 Nc1 63. Bxc1 Rg7 64. Qh3 Rd8 65. Qh1 Kf7 66. Qh2
Kg8 67. Qxh5 c4 68. Qh3 Rc8 69. g6 Ra7 70. Qh8+ Kxh8 71. Bd2 Re8 72. Bc1 Raa8
73. Kf5 Rec8 74. Be3 Kg8 75. Nb5 Rcb8 76. Bf2 Rb7 77. Ba7 Rh7 78. Kf6 Rd8 79.
gxh7+ Kf8 80. Nc3 Rd7 81. Bb8 Rd2 82. Bh2 Rd7 83. Ke5 Rg7 { White resigns. } 0-1
```

On y voit la même syntaxe spéciale, mettons-le donc dans l'outil en faisant unsteg et l'on trouve : Bravo, vous êtes super fort aux échecs vous dis donc !
Le flag c'est CYBN{3ch3c_3t_m4t_du_b3rg3r}
