
#coefficient de français
COEFFR = 4
COEFANG = 2
COEMATHS = 5
COECHINOIS =4
coesvt=6
m_francais = float(input('Français, entrez votre moyenne: '))
m_maths = float(input("Maths, entrez votre moyenne: "))
m_anglais = float(input("Anglais, entrez votre moyenne: ")  )
mCHINOIS=float(input("chinois, entrez votre moyenne:"))
m_svt=float(input("SVT, entrez votre moyenne:"))
moyenne_g = (m_francais * COEFFR  + m_anglais * COEFANG + m_maths * COEMATHS+mCHINOIS*COECHINOIS+m_svt*coesvt) /19

print("la moyenne general est :", moyenne_g)
if moyenne_g < 10:
    print("Votre mention est  Médiocre !")
elif moyenne_g >= 10 and moyenne_g < 12:
    print(" Votre mention est Passable !")
elif moyenne_g >= 12 and moyenne_g < 14:
    print(" Votre mention est Assez bien !")
elif moyenne_g >= 14 and moyenne_g < 16:
    print("Votre mention est Bien !")  
elif moyenne_g >= 14 and moyenne_g < 18:
    print("Votre mention est Très Bien !")



"""
Pas de mention : entre 10 et 12/20
Assez bien : entre 12 et 14/20
Bien : entre 14 et 16/20
Mention très bien : 16/20 et plus

"""

## EXO 1
#  AJOUTER  SVT coef 2 et HISTOIRE coef 1

##  EXO 2
#  AJOUTER  la mention  Excellent  moyenne > 18




