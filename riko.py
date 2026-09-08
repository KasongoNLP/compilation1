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
fenetre.resizable(False, False)

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

    titre = ctk.CTkLabel(
        modal,
        text="Connexion",
        font=ctk.CTkFont(
            size=24,
            weight="bold"
        )
    )

    titre.pack(pady=(25, 15))


    # ========================================================
    # NOM UTILISATEUR
    # ========================================================

    utilisateur = ctk.CTkEntry(
        modal,
        width=260,
        height=35,
        placeholder_text="Nom d'utilisateur"
    )

    utilisateur.pack(pady=5)


    # ========================================================
    # MOT DE PASSE
    # ========================================================

    mot_de_passe = ctk.CTkEntry(
        modal,
        width=260,
        height=35,
        placeholder_text="Mot de passe",
        show="*"
    )

    mot_de_passe.pack(pady=5)


    # ========================================================
    # MESSAGE D'ERREUR
    # ========================================================

    erreur = ctk.CTkLabel(
        modal,
        text="",
        text_color="red"
    )

    erreur.pack(pady=3)


    # ========================================================
    # FONCTION DE CONNEXION
    # ========================================================

    def connecter():

        user = utilisateur.get()
        password = mot_de_passe.get()

        if user == "admin" and password == "1234":

            print("Connexion réussie")

            modal.grab_release()
            modal.destroy()

        else:

            erreur.configure(
                text="Identifiants incorrects"
            )


    # ========================================================
    # BOUTON
    # ========================================================

    bouton = ctk.CTkButton(
        modal,
        text="Se connecter",
        width=150,
        height=35,
        fg_color="red",
        command=connecter
    )

    bouton.pack(pady=8)


# ============================================================
# OUVRIR LE POPUP AUTOMATIQUEMENT
# ============================================================
fenetre.after(100,ouvrir_connexion)
# ============================================================






# LANCEMENT
# ============================================================
fenetre.mainloop()
