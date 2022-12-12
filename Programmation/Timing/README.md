# Timing

## Consigne

"Dans la vie tout est une question de timing".

nc 10.242.0.1 10003

Vous devez être connecté en VPN pour accéder à ce challenge.

Auteur : Maestran

## Résolution

Lors de la connection au serveur, on nous demande de donner un nombre.

```bash
λ ~ nc 10.242.0.1 10003
    Guess the number !
```

En regardant [le code source du challenge](timing.py), on voit que les 3 nombres à deviner sont générés aléatoirement suivant le temps actuel. Voici les infos qui nous intéressent :

```python
7 : random.seed(int(time.time()))

16: true_num_1 = random.randint(0, 50)

30: true_num_2 = random.randint(0, 50000000000)

44: true_num_3 = random.random()
```

Il nous suffit donc de réutiliser [presque le même code](solution.py) pour retrouver les variables aléatoires et les envoyer au serveur. Il faut donc :

- Seeder le random avec le temps actuel
- Générer les 3 nombres aléatoires
- Les envoyer au serveur (dans l'ordre) - Utilisation du packet [pwntools](https://github.com/Gallopsled/pwntools) dans mon cas

Et le flag est à nous !
![imageflag](https://media.discordapp.net/attachments/972604017261830176/1051920615512219699/image.png)
