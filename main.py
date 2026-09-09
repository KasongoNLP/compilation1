import customtkinter as ctk
from PIL import Image

# ============================================================
# CONFIGURATION De l'affichage
# ============================================================

ctk.set_appearance_mode("light")
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

        if user == "steve" and password == "steve":

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







# ================================================================================
# OUVRIR LE POPUP AUTOMATIQUEMENT
# ================================================================================
fenetre.after(100,ouvrir_connexion)
# ================================================================================


#........... Gestion de frame .................................................
conteneur = ctk.CTkFrame(fenetre,fg_color="#F3F4F6",corner_radius=20)
conteneur.place(x=0,y=0,relheight=1)
#..............................................................................


conteneur1 = ctk.CTkFrame(fenetre,fg_color="#F3F4F6",corner_radius=20, width=1500)
conteneur1.place(x=200,y=0,relheight=1)

def afficher_accueil():

    # Nettoyer le conteneur principal
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
        width=190,
        corner_radius=18,
        fg_color="white"
    )

    menu.place(
        x=0,
        y=0,
        relheight=1
    )
    menu.pack_propagate(False)

    # ========================================================
    # TITRE
    # ========================================================

    titre_menu = ctk.CTkLabel(
        menu,
        text="DAILLY\nCHECKING",
        text_color="#1F2937",
        font=ctk.CTkFont(
            size=19,
            weight="bold"
        )
    )

    titre_menu.pack(
        pady=(22, 12)
    )

    # ========================================================
    # PHOTO DE PROFIL
    # ========================================================

    try:

        image_profil = Image.open("profil.png")
        image_profil = image_profil.resize((70, 70))

        photo_profil = ctk.CTkImage(
            light_image=image_profil,
            dark_image=image_profil,
            size=(70, 70)
        )

        label_photo = ctk.CTkLabel(
            menu,
            text="",
            image=photo_profil
        )

    except Exception:

        label_photo = ctk.CTkLabel(
            menu,
            text="S",
            width=70,
            height=70,
            corner_radius=35,
            fg_color="#E5E7EB",
            text_color="#374151",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

    label_photo.pack(
        pady=(5, 5)
    )

    # ========================================================
    # NOM UTILISATEUR
    # ========================================================

    nom_utilisateur = ctk.CTkLabel(
        menu,
        text="Steve",
        text_color="#1F2937",
        font=ctk.CTkFont(
            size=14,
            weight="bold"
        )
    )

    nom_utilisateur.pack(
        pady=(2, 18)
    )

    # ========================================================
    # SÉPARATION
    # ========================================================

    separation = ctk.CTkFrame(
        menu,
        height=1,
        fg_color="#E5E7EB"
    )

    separation.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    # ========================================================
    # BOUTONS
    # ========================================================

    bouton_profil = ctk.CTkButton(
        menu,
        text="Profil",
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#374151"
    )

    bouton_profil.pack(
        fill="x",
        padx=12,
        pady=3
    )

    bouton_compilation = ctk.CTkButton(
        menu,
        text="Compilation",
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="#EFF6FF",
        hover_color="#DBEAFE",
        text_color="#2563EB",
        command=afficher_compilation
    )

    bouton_compilation.pack(
        fill="x",
        padx=12,
        pady=3
    )

    bouton_historyque = ctk.CTkButton(
        menu,
        text="Historique",
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#374151"
    )

    bouton_historyque.pack(
        fill="x",
        padx=12,
        pady=3
    )

    bouton_setting = ctk.CTkButton(
        menu,
        text="Setting",
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#374151"
    )

    bouton_setting.pack(
        fill="x",
        padx=12,
        pady=3
    )

    bouton_email = ctk.CTkButton(
        menu,
        text="Email",
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="transparent",
        hover_color="#F1F5F9",
        text_color="#374151"
    )

    bouton_email.pack(
        fill="x",
        padx=12,
        pady=3
    )

    # ========================================================
    # ESPACE FLEXIBLE
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
        height=38,
        corner_radius=10,
        anchor="w",
        fg_color="#FEF2F2",
        hover_color="#FEE2E2",
        text_color="#DC2626"
    )

    bouton_deconnexion.pack(
        fill="x",
        padx=5,
        pady=(3, 18)
    )



#Gestion de fenêtre affichage de compilation 
def afficher_compilation():
    # Nettoyer le conteneur principal
    for widget in conteneur1.winfo_children():
        widget.destroy()


    titre_menu = ctk.CTkLabel(
        conteneur1,
        text="Compilation ",
        text_color="#1F2937",
        font=ctk.CTkFont(
            size=19,
            weight="bold"
        )
    )

    titre_menu.pack()

    



# LANCEMENT
# ============================================================
fenetre.mainloop()
