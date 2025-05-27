import math
from collections import Counter

def entropie_theorique(password):
    # Déterminer l'alphabet utilisé
    alphabet = set()
    for c in password:
        if c.islower():
            alphabet.update('abcdefghijklmnopqrstuvwxyz')
        elif c.isupper():
            alphabet.update('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        elif c.isdigit():
            alphabet.update('0123456789')
        else:
            alphabet.update('!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?`~'
)  # principaux symboles

    alphabet_size = len(alphabet)
    length = len(password)

    if alphabet_size == 0 or length == 0:
        return 0

    entropy = length * math.log2(alphabet_size)
    return entropy

def temps_moyen_craquage(password, tentative_par_seconde):
    entropy = entropie_theorique(password)
    nombre_possibilites = 2 ** entropy

    # En moyenne, un attaquant trouve le mot de passe en testant la moitié des possibilités
    temps_secondes = (nombre_possibilites / 2) / tentative_par_seconde

    return entropy, temps_secondes

def afficher_temps(seconds):
    # Fonction d'affichage lisible (secondes => jours, années...)
    minutes, sec = divmod(seconds, 60)
    heures, minutes = divmod(minutes, 60)
    jours, heures = divmod(heures, 24)
    annees, jours = divmod(jours, 365)

    parts = []
    if annees > 0:
        parts.append(f"{int(annees)} an(s)")
    if jours > 0:
        parts.append(f"{int(jours)} jour(s)")
    if heures > 0:
        parts.append(f"{int(heures)} heure(s)")
    if minutes > 0:
        parts.append(f"{int(minutes)} minute(s)")
    if sec > 0:
        parts.append(f"{int(sec)} seconde(s)")

    return ", ".join(parts)

# Exemple d'utilisation
if __name__ == "__main__":
    mot_de_passe = "P@ssW0rd!"
    essais_par_seconde = 1000000000  # 1 milliard de tentatives/sec

    entropie, temps = temps_moyen_craquage(mot_de_passe, essais_par_seconde)

    print(f"Mot de passe : {mot_de_passe}")
    print(f"Entropie théorique : {entropie:.2f} bits")
    print(f"Temps moyen estimé pour craquer : {afficher_temps(temps)}")
