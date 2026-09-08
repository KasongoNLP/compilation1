import customtkinter as ctk
from PIL import Image


#la convertion de l'image............
#image = Image.open("icone.png")
#image.save("icone.ico", format="ICO")
#lecture de l'image .................

# ============================================================
# FENÊTRE
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
# ============================================================







#creation de la fênetre
fenetre = ctk.CTk()
fenetre.title("Dailly Checking")
fenetre.geometry("800x500")

# Icône de la fenêtre
fenetre.iconbitmap("icone.ico")




#la configuration du mode d'affichage.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ============================================================
# FENÊTRE
# ============================================================



#Partie de connaixion
# ================================================================================================
# TITRE
# ================================================================================================
titre = ctk.CTkLabel(fenetre,text="Connexion",font=ctk.CTkFont(size=24,weight="bold"))
titre.pack(pady=(25, 15))


# =================================================================================================
# NOM UTILISATEUR
# =================================================================================================
utilisateur = ctk.CTkEntry(fenetre,width=260,height=35,placeholder_text="Nom d'utilisateur")
utilisateur.pack(pady=5)

# =================================================================================================
# MOT DE PASSE
# =================================================================================================
mot_de_passe = ctk.CTkEntry(fenetre,width=260,height=35,placeholder_text="Mot de passe",show="*")
mot_de_passe.pack(pady=5)

# =================================================================================================
# MESSAGE D'ERREUR
# =================================================================================================
erreur = ctk.CTkLabel(fenetre,text="",text_color="red")
erreur.pack(pady=3)










# ============================================================
# FONCTION DE CONNEXION
# ============================================================
def connecter():
    user = utilisateur.get()
    password = mot_de_passe.get()

    if user == "admin" and password == "1234":

        print("Connexion réussie")

        fenetre.destroy()

    else:

        erreur.configure(
            text="Identifiants incorrects"
        )











# ============================================================
# BOUTON
# ============================================================
bouton = ctk.CTkButton(fenetre, text="Se connecter", width=150, height=35, fg_color="red", command=connecter)
bouton.pack(pady=8)













fenetre.mainloop()