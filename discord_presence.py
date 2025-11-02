from pypresence import Presence
import time
import subprocess
# INSTALLER LES DEPENDANCES:
# pip install -U pypresence
# sudo apt install xdotool

CLIENT_ID = "1433922682080067594" # ID du client (application)
descr = "Sa fonctionne pas..."
l_img = "nom" # Nom de la grande image de l'activité (a importer dans le developer portal)
s_img = "nom" # Nom de la petite image de l'activité (a importer dans le developer portal)
# /!\ mettre un nom incorrect affichera la photo de profil de l'application pour la grande image et rien pour la petite image

RPC = Presence(CLIENT_ID)
RPC.connect()

time.sleep(1)  
start_time = int(time.time())
try:
    while True:
        try:
            active_window = subprocess.check_output(
                ["xdotool", "getactivewindow", "getwindowname"],
                text=True
            ).strip()
            if "Visual Studio Code" in active_window:
                filename = active_window.replace(" - Visual Studio Code", "").split(" — ")[0]
                details_text = f"Édition de {filename}"
            else:
                details_text = "Pas dans VSCode"
        except subprocess.CalledProcessError:
            details_text = "Pas dans VSCode"

        RPC.update(
            details=details_text,
            state=descr,
            large_image=l_img,
            small_image=s_img,
            start=start_time
        )

        time.sleep(1)
except KeyboardInterrupt:
    RPC.close()
