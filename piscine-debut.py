liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))
        continue
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")
        continue
    
    if commande == 'exit' :
        tmp = input ("en etes-vous sur ? (o)ui/(n)on")
        if tmp == 'o' :
            isAlive = False
        continue
    print(f"commande {commande} inconnue")
            
