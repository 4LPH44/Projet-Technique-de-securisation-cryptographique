alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere in alphabet:
            index = alphabet.index(caractere)
            nouvel_index = (index + decalage) % len(alphabet)
            resultat += alphabet[nouvel_index]
        else:
            resultat += caractere
    return resultat

if __name__ == "__main__":
    message = input("Entrez le message à chiffrer : ")
    decalage = int(input("Entrez le décalage : "))
    print(cesar(message, decalage))