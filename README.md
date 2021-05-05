# OCR tool pour windows (utilisant Google vision)

## Présentation de l'outil

Vous pouvez faire de la reconnaissance de texte dans une image seule, ou sur un dossier d'image.

### Exemple :  

![demo](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/Animation.gif)  

- 1 image
- 1 dossier

## Prérequis

Il vous faut une clé API pour l'API Google Vision (il faut mettre un numéro de CB, rassurez-vous, 1000 images par mois sont gratuites.  
PS : heu quand je dis qu'il faut mettre la CB, c'est pas pour moi hein ! 😂, c'est pour Google).  
C'est juste l'API Google, après, c'est VOTRE compte API (vous avez 1000 pages gratuites par mois) sur l'API.
Je n'ai évidemment pas accès à votre compte (ni vous au mien).
C'est donc sécurisé.

Je ne peux pas vous fournir ma clé API pour des raisons évidentes (c'est lié à MA CB), donc il vous faudra suivre le tutoriel de Google ici :

<https://cloud.google.com/vision/docs/ocr>

(Vous n'avez besoin de faire que les étapes 1 et 2.)

![Google API](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/google.png)

Quand vous aurez récupérer votre clé au format .json, il faudra la placer dans le dossier `.config` de votre repertoir utilisateur, et la nommer `google.json` (si le dossier `.config` de votre répertoire utilisateur n'existe pas, créez le, puis collez-y votre fichier `google.json`)

## Installation

- Télécharger la dernière release (En haut à droite : [Releases](https://github.com/Sergeileduc/ocr-tool/releases)  
Télécharger le fichier `ocr.zip`

- Dézippez le fichier à l'endroit de votre choix. (`D:\bin`, `C:\mes-scripts`, etc...)

- Créer le raccourci dans `Clic-droit -> Envoyer vers` :  
`Win + R`  
`shell:SendTo`  
![SenTO](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/shellsend.png)  
Clic-droit "Nouveau raccourci"  
Parcourir jusqu'à `ocr.exe`  
Nommer le raccourci comme on veut.  
![Browser](https://raw.githubusercontent.com/Sergeileduc/ocr-tool/master/ressources/doc/parcourir.jpg) 

## Enjoy
