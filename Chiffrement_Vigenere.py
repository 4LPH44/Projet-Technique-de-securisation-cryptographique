from Chiffrement_Cesar import cesar

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenere(message, cle):
    if len(cle) != len(message):
        raise ValueError("La clé doit être de la même longueur que le message.")
    else :
        resultat = ""
        for i in range(len(message)):
            index_cle = alphabet.index(cle[i])
            resultat += cesar(message[i], index_cle)
        return resultat


if __name__ == "__main__":    
    message = input("Entrez le message à chiffrer : ").lower()
    cle = input("Entrez la clé : ").lower()
    print(vigenere(message, cle))

