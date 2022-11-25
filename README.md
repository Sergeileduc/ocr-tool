# OCR tool pour windows (utilisant Google vision)

## Présentation des outils

Il y a 2 outils :

### ocr

Vous pouvez faire de la reconnaissance de texte dans une image seule, ou sur un dossier d'image.

### ocrtrad

Vous pouvez faire de la reconnaissance de texte dans une image seule, ou sur un dossier d'image, et traduire le texte en français.

### Exemple  

![demo](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/Animation.gif)  

- 1 image (formats *.jpg*, *.png* et *.webp*)
- 1 dossier (sans la 1ère image de cover)

## Prérequis

### Google Vision

Il vous faut une clé API pour l'API Google Vision (il faut mettre un numéro de CB, rassurez-vous, 1000 images par mois sont gratuites.  
PS : heu quand je dis qu'il faut mettre la CB, c'est pas pour moi hein ! 😂, c'est pour Google).  
C'est juste l'API Google, après, c'est VOTRE compte API (vous avez 1000 pages gratuites par mois) sur l'API.
Je n'ai évidemment pas accès à votre compte (ni vous au mien).
C'est donc sécurisé.

Je ne peux pas vous fournir ma clé API pour des raisons évidentes (c'est lié à MA CB), donc il vous faudra suivre le tutoriel de Google ici :

<https://cloud.google.com/vision/docs/ocr>

(Vous n'avez besoin de faire que les étapes 1 et 2.)

![Google API](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/google.png)

En gros les étapes sont :

- aller sur la console Google : [Console Google](https://console.cloud.google.com/) et créer un nouveau Projet.
- sélectionner le projet en question.
- dans le menu hamburger (en haut à gauche, les 3 traits horizontaux) -> IAM et Admin -> Comptes de Service
- Créer un compte de Service
- Etape 1 y a que le nom à remplir, puis `Créer` (les étapes 2 et 3 sont facultatives), donc `OK`
- Cliquer sur le nom de votre nouveau *compte de service*
- Onglet `Clés` : Ajouter une clé -> Créer une clé -> Type de clé : `JSON` -> Télécharger votre clé
- Toujours dans le menu Hamburger : API et Services
- `+ Activer les API et les services`
- Google Vision API -> Activer
- Et pour la facturation (même si on a 1000 images gratuites/mois, un compte de facturation est quand même demandé, c'est dans le menu hamburger, encore une fois -> Facturation)

Alors ça vous demande un carte bancaire, mais vous avez le droit à 1000 images gratuites par mois (donc ça va).

Quand vous aurez récupérer votre clé au format .json, il faudra la placer dans le dossier `.config` de votre repertoir utilisateur, et la nommer `google.json` (si le dossier `.config` de votre répertoire utilisateur n'existe pas, créez le (donc chez moi, j'ai donc le dossier `C:\Users\sergei\.config`), puis collez-y votre fichier `google.json`)

Et enfin, si ça vous énerve de voir ce dossier `.config` à cotés de vos dossiers "Mes Documents" "Vidéos", etc..., vous pouvez totalement le cacher (clic droit -> Propriétés -> Caché) (d'ailleurs, le `.` en début de nom dans `.config`, ça vient du monde Linux ou par convention, les trucs qui commencent par `.` sont automatiquement cachés...)

### DeepL API

Pour l'outil `ocrtrad` de reconnaissance de texte + la traduction DeepL, il vous faudra récupérer une clé d'API Deepl.

[DeepL API](https://www.deepl.com/fr/pro-api?cta=header-pro-api/)

Prendre la version gratuite. (Il vous faut quand même une CB, il me semble).

Récupérer la clé d'API. (ça ressmeble à 5d954132-g0tt-6b7d......)

## Installation

- Télécharger la dernière release (En haut à droite : [Releases](https://github.com/Sergeileduc/ocr-tool/releases))  
  - Télécharger le fichier `ocr.zip` pour la reconnaissance de caractère seulement.
  - Télécharger le fichier `ocrtrad.zip` pour la reconnaissance ET la traduction.

- Dézippez le fichier à l'endroit de votre choix. (`D:\bin`, `C:\mes-scripts`, etc...)

- Créer le raccourci dans `Clic-droit -> Envoyer vers` :  
`Win + R`  
`shell:SendTo` -> OK  
![SenTO](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/shellsend.png)
Clic-droit "Nouveau raccourci"  
Parcourir jusqu'à `ocr.exe` ou `ocrtrad.exe`
Nommer le raccourci comme on veut.  
![Browser](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/parcourir.jpg)

### Pour ocrtrad seulement

Enfin, dans le dossier qui contient le porgramme .exe, vous trouverez un fichier nommé `.env`

Ouvrez le avec un éditeur de texte (bloc note, etc...)

Editez le fichier en mettant votre clé d'API DeepL
(donc `DEEPL=5d954132-g0tt-6b7d......`)

## En cas de problème

Le programme n'étant pas signé par éditeur, Windows Smart Screen peut s'activer :
![smartscreen](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/smartscreen.jpg)

Vous pouvez forcer l'éxecution :
![smartscreen2](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/smartscreen2.jpg)

## :exclamation:  Attention

Dûe au sens de lecture parfois un peu alambiqué (en zig-zag) des BD et comics, il se peut que l'ordre de certaines bulles soit inversé (ou que des bulles se retrouvent collées, etc...)... Donc il faut vérifier.

## Enjoy
