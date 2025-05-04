def chiffrement_hill(message, cle):
   
    message_numerique = [ord(char) - ord('A') for char in message.upper() if char.isalpha()]
    
    taille_matrice = len(cle)

    while len(message_numerique) % taille_matrice != 0:
        message_numerique.append(0)
    
    # Chiffrement
    message_chiffre = []
    for i in range(0, len(message_numerique), taille_matrice):
        bloc = message_numerique[i:i + taille_matrice]
        for j in range(taille_matrice):
            somme = sum(cle[j][k] * bloc[k] for k in range(taille_matrice)) % 26
            message_chiffre.append(somme)
    
    
    return ''.join(chr(num + ord('A')) for num in message_chiffre)