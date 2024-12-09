
def calculImc(poids, taille):
    return poids / (taille**2)


def poidStatus():
    
    poids = int(input("Entrez votre poids: "))
    taille = float(input("Entrez votre taille: "))

    imc = calculImc(poids, taille)

    print(imc)
    
    if imc < 18.5:
        return "Insuffisance pondérale (maigreur)"
    elif imc >= 18.5 and imc < 25:
        return "Corpulence normale"
    elif imc >= 25 and imc < 30:
        return "Surpoids"
    elif imc >= 30 and imc < 35:
        return "Obésité modérée"
    elif imc >= 35 and imc < 40:
        return "Obésité sévère"
    else:
        return "Obésité morbide ou massive" 


def tension():
    pression_ar = float(input("Entrez la pression arterielle: "))
    if pression_ar < 12:
        return "Normal"
    elif pression_ar >= 12 and pression_ar < 13:
        return "Elevée"
    elif pression_ar >= 13 and pression_ar < 140:
        return "Hypertension artérielle (stade 1)"
    elif pression_ar >= 14:
        return "Hypertension artérielle (stade 2)"
    else:
        return "Crise hypertensive"

def main():
   print(poidStatus()) 
   #print(tension())

if __name__ == "__main__":
    main()
