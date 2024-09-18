# ASCII art pour "Météo"
ascii_art_meteo = """
  __  __      _            
 |  \/  |    (_)           
 | \  / | ___ _ _ __   __ _ 
 | |\/| |/ _ \ | '_ \ / _` |
 | |  | |  __/ | | | | (_| |
 |_|  |_|\___|_|_| |_|\__,_|
"""

# Définir les jours de la semaine et les températures associées
jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
temperatures = [10, 12, 3, 9, 1, 34, 15]

# Définir les seuils de température pour les différents types de vêtements
seuil_chaud = 25
seuil_neutre_bas = 14
seuil_neutre_haut = 24
seuil_froid = 13

print(ascii_art_meteo)  # Affiche l'art ASCII "Météo"

# Demander à l'utilisateur pour quel jour il s'habille
while True:
    jour_semaine = input("Pour quel jour de la semaine vous habillez-vous ? (Lundi à Dimanche) : ").capitalize()
    if jour_semaine in jours_semaine:
        index = jours_semaine.index(jour_semaine)
        temperature = temperatures[index]
        break
    else:
        print("❌ Jour de la semaine invalide. Veuillez entrer un jour valide (Lundi à Dimanche).")

# Demander à l'utilisateur comment il est habillé
while True:
    habillement = input("Comment êtes-vous habillé ? (chaud, neutre, froid) : ").lower()
    if habillement in ['chaud', 'neutre', 'froid']:
        break
    else:
        print("❌ Réponse invalide. Veuillez entrer 'chaud', 'neutre', ou 'froid'.")

# Vérifier si l'habillement correspond à la température
if habillement == 'chaud':
    if temperature >= seuil_chaud:
        print(f"✅ Vous êtes bien habillé pour le {jour_semaine} avec une température de {temperature}°C. 🌞")
    elif temperature < seuil_froid:
        print(f"❄️ Il fait trop froid pour être habillé en 'chaud' aujourd'hui. Température : {temperature}°C.")
    else:
        print(f"🌡️ Il fait plutôt frais pour être habillé en 'chaud'. Température : {temperature}°C.")
elif habillement == 'neutre':
    if seuil_neutre_bas <= temperature <= seuil_neutre_haut:
        print(f"✅ Vous êtes bien habillé pour le {jour_semaine} avec une température de {temperature}°C. 🌤️")
    elif temperature < seuil_froid:
        print(f"❄️ Il fait trop froid pour être habillé en 'neutre' aujourd'hui. Température : {temperature}°C.")
    else:
        print(f"🔥 Il fait trop chaud pour être habillé en 'neutre'. Température : {temperature}°C.")
elif habillement == 'froid':
    if temperature <= seuil_froid:
        print(f"✅ Vous êtes bien habillé pour le {jour_semaine} avec une température de {temperature}°C. 🧥")
    elif temperature > seuil_chaud:
        print(f"☀️ Il fait trop chaud pour être habillé en 'froid' aujourd'hui. Température : {temperature}°C.")
    else:
        print(f"🌡️ Il fait plutôt chaud pour être habillé en 'froid'. Température : {temperature}°C.")
