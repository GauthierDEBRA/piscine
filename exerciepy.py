import random 
nombre_aleatoire = random.randint(1, 100)
print(nombre_aleatoire)
trouvé = False
while not trouvé:
    proposition = int(input("Proposez un nombre : "))
    if proposition == nombre_aleatoire:
        print("Félicitation, vous avez trouvé")
        trouvé = True
    elif proposition < nombre_aleatoire:
        print("c'est plus !")
    else:
        print("c'est moins !")

