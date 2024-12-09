
from datetime import datetime

## Loop
docteurs = ["Dr KOFFI Serge ", "Dr  GRABO  Florent", "DR SANOGO Souleymane", "Dr SEKA  Marie"]
print("Liste des Docteurs de la Clinique Esperance  :")

for docteur in docteurs:
  print(docteur)
  
  

# datetime object containing current date and time
now = datetime.now()

print("La date est : ", datetime.today())
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# If today is Friday (0 = Mon, 1 = Tue, 2 = Wen ...)
if datetime.today().weekday() == 4:
    print("Yes, Today is Friday")
else:
    print("Nope...")
    
    
 