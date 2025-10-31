# Importation du module qrcode
import qrcode

# Message expliquant le lien du site
message = """Voici un site que tout étudiant en informatique dois connaitre 
 https://www.w3schools.com/default.asp"""

# Création de l'objet code sur lequel je vais appeler les différentes méthodes
Code = qrcode.QRCode(version =1, box_size = 5, border = 3)

"""
Explication des paramètre:
- Version : Permet de définir la capacité du code QR 
- box_size : permet de définir la taille de l'image du code QR 
- border : permet de définir la taille de la couleur blanche autour du code QR 
"""
Code.add_data(message) # Ajouetr du message au code QR
Code.make(fit = True)
img = Code.make_image(fill_color = "black", back_color = "white")
img.save("Co.png")
print("Code Qr crée avec succès")