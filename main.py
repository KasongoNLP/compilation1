import customtkinter as ctk
from PIL import Image

# ============================================================
# CONFIGURATION De l'affichage
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ============================================================
# FENÊTRE PRINCIPALE
# ============================================================

fenetre = ctk.CTk()

fenetre.title("Dailly Checking")
fenetre.geometry("800x500")
fenetre.resizable(True, True)

# Icône de la fenêtre
fenetre.iconbitmap("icone.ico")

# ============================================================
# FONCTION CONNEXION
# ============================================================

def ouvrir_connexion():
    # ========================================================
    # FENÊTRE POPUP
    # ========================================================
    modal = ctk.CTkToplevel(fenetre)
    modal.title("Connexion")
    modal.geometry("400x300")
    modal.resizable(False, False)

    # Popup au-dessus de la fenêtre principale
    modal.transient(fenetre)

    # Bloquer la fenêtre principale
    modal.grab_set()



    # ========================================================
    # TITRE
    # ========================================================
    titre = ctk.CTkLabel(modal,text="Connexion",font=ctk.CTkFont(size=24,weight="bold"))
    titre.pack(pady=(25, 15))


    # ========================================================
    # NOM UTILISATEUR
    # ========================================================
    utilisateur = ctk.CTkEntry(modal,width=260,height=35,placeholder_text="Nom d'utilisateur")
    utilisateur.pack(pady=5)


    # ========================================================
    # MOT DE PASSE
    # ========================================================

    mot_de_passe = ctk.CTkEntry(modal,width=260,height=35,placeholder_text="Mot de passe",show="*")
    mot_de_passe.pack(pady=5)


    # ========================================================
    # MESSAGE D'ERREUR
    # ========================================================
    erreur = ctk.CTkLabel(modal,text="",text_color="red")
    erreur.pack(pady=3)


    # ========================================================
    # FONCTION DE CONNEXION
    # ========================================================

    def connecter():

        user = utilisateur.get()
        password = mot_de_passe.get()

        if user == "admin" and password == "1234":

            print("Connexion réussie")
            afficher_accueil()

            modal.grab_release()
            modal.destroy()

        else:

            erreur.configure(
                text="Identifiants incorrects"
            )


    # ========================================================
    # BOUTON
    # ========================================================
    bouton = ctk.CTkButton(modal,text="Se connecter",width=150,height=35,fg_color="red",command=connecter)
    bouton.pack(pady=8)







# ============================================================
# OUVRIR LE POPUP AUTOMATIQUEMENT
# ============================================================
fenetre.after(100,ouvrir_connexion)
# ============================================================

conteneur = ctk.CTkFrame(fenetre,fg_color="transparent")
conteneur.pack(fill="both",expand=True,padx=20,pady=20)


def afficher_accueil():

    for widget in conteneur.winfo_children():
        widget.destroy()

    # ========================================================
    # STRUCTURE PRINCIPALE
    # ========================================================
    frame_accueil = ctk.CTkFrame(
        conteneur,
        fg_color="transparent"
    )

    frame_accueil.pack(
        fill="both",
        expand=True
    )

    # ========================================================
    # MENU GAUCHE
    # ========================================================

    menu = ctk.CTkFrame(
        frame_accueil,
        width=180,
        corner_radius=0
    )

    menu.pack(
        side="left",
        fill="y"
    )

    menu.pack_propagate(False)

    # ========================================================
    # ZONE DE CONTENU
    # ========================================================

    contenu = ctk.CTkFrame(
        frame_accueil,
        fg_color="transparent"
    )

    contenu.pack(
        side="left",
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ========================================================
    # TITRE DU MENU
    # ========================================================

    titre_menu = ctk.CTkLabel(
        menu,
        text="DAILLY\nCHECKING",
        font=ctk.CTkFont(
            size=20,
            weight="bold"
        )
    )

    titre_menu.pack(
        pady=(30, 40)
    )

    # ========================================================
    # BOUTONS DU MENU
    # ========================================================

    bouton_profil = ctk.CTkButton(
        menu,
        text="Profil",
        height=40
    )

    bouton_profil.pack(
        fill="x",
        padx=15,
        pady=5
    )

    bouton_tableau = ctk.CTkButton(
        menu,
        text="Tableau de bord",
        height=40
    )

    bouton_tableau.pack(
        fill="x",
        padx=15,
        pady=5
    )

    bouton_verification = ctk.CTkButton(
        menu,
        text="Vérifications",
        height=40
    )

    bouton_verification.pack(
        fill="x",
        padx=15,
        pady=5
    )

    bouton_historique = ctk.CTkButton(
        menu,
        text="Historique",
        height=40
    )

    bouton_historique.pack(
        fill="x",
        padx=15,
        pady=5
    )

    bouton_parametres = ctk.CTkButton(
        menu,
        text="Paramètres",
        height=40
    )

    bouton_parametres.pack(
        fill="x",
        padx=15,
        pady=5
    )

    # ========================================================
    # ESPACE AVANT DÉCONNEXION
    # ========================================================

    espace = ctk.CTkFrame(
        menu,
        fg_color="transparent"
    )

    espace.pack(
        fill="both",
        expand=True
    )

    # ========================================================
    # DÉCONNEXION
    # ========================================================
    bouton_deconnexion = ctk.CTkButton(
        menu,
        text="Déconnexion",
        height=40,
        fg_color="#C0392B",
        hover_color="#922B21"
    )

    bouton_deconnexion.pack(
        fill="x",
        padx=15,
        pady=(5, 20)
    )

    # ========================================================
    # CONTENU PAR DÉFAUT
    # ========================================================

    titre = ctk.CTkLabel(
        contenu,
        text="Bienvenue dans Dailly Checking",
        font=ctk.CTkFont(
            size=28,
            weight="bold"
        )
    )

    titre.pack(
        pady=40
    )







# LANCEMENT
# ============================================================
fenetre.mainloop()
