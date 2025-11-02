# Installation :
> `sudo apt install xdotool`
> `pip install -U pypresence`

/!\ Je vous conseil de lancer le script via un environnement virtuel python
```
python3 -m venv venv
source venv/bin/activate
```
-> Executez maintenant le pip install

# Configurer le script:
## Ajouter des images personnalisées:
https://discord.com/developers/applications/**APPLICATION_ID**/rich-presence/assets
> Importez sur cette page vos images et renommez-les comme voulu
## Configurer le script

Exemple (Visual Studio Code non ouvert) <br>
<img src="capture.png" alt="" width="250" height="100" />

```
CLIENT_ID = "1433922682080067594" # ID du client (application)
descr = "Sa fonctionne pas..."
l_img = "nom" # Image non existante -> photo de profil de l'application affichée
s_img = "image" # Image défini affichée
```

Exemple (Visual Studio Code ouvert sur botinfo.js) <br>
<img src="capture2.png" alt="" width="250" height="100" />

```
CLIENT_ID = "1433922682080067594" # ID du client (application)
descr = "Nouvelle description !"
l_img = "image" # Image défini affichée
s_img = "test" # Image non existante -> rien d'affiché
```
