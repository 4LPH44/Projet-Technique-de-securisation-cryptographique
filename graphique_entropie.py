import math
import matplotlib.pyplot as plt



def entropie_theorique(password_length, alphabet_size):
    if password_length <= 0 or alphabet_size <= 0:
        return 0
    return password_length * math.log2(alphabet_size)



def plot_entropie_vs_longueur(alphabet_size):
    longueurs = list(range(1, 31))  # mots de passe de 1 à 30 caractères
    entropies = [entropie_theorique(l, alphabet_size) for l in longueurs]

    plt.figure(figsize=(10,6))
    plt.plot(longueurs, entropies, marker='o')
    plt.title("Entropie théorique en fonction de la longueur du mot de passe")
    plt.xlabel("Longueur du mot de passe (caractères)")
    plt.ylabel("Entropie (bits)")
    plt.grid(True)
    plt.show()


# Exemple d'utilisation de la fonction d'entropie théorique
longueur = 10  # Mot de passe de 10 caractères
alphabet = 26 + 26 + 10 + 32  # minuscules + majuscules + chiffres + 32 symboles spéciaux

print(f"Entropie théorique : {entropie_theorique(longueur, alphabet):.2f} bits")

# Exemple d'utilisation de la fonction de tracé
# Exemple d'utilisation
alphabet = 26 + 26 + 10 + 32  # minuscules + majuscules + chiffres + 32 symboles spéciaux
plot_entropie_vs_longueur(alphabet)
