import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('note.csv', sep=';')

X = data['nb heure'].values  
y = data['note'].values  

n = len(X)

sum_x = np.sum(X)
sum_y = np.sum(y)
sum_xy = np.sum(X * y)
sum_x_squared = np.sum(X ** 2)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)

b = (sum_y - a * sum_x) / n

print("Coefficient de la pente (a) :", a)
print("Intercept (b) :", b)

#prédire leq notes en fonction de nombres d'heures
try:
    nouvelles_heures = float(input("Entrez le nombre d'heures d'étude pour prédire la note : "))
    nouvelle_note = a * nouvelles_heures + b
    nouvelle_note = np.clip(nouvelle_note, 0, 100)
    print(f"Prédiction de la note pour {nouvelles_heures} heures d'étude : {nouvelle_note:.2f}")
except ValueError:
    print("Veuillez entrer un nombre valide.")

#Dessiner la droite de régression
plt.scatter(X, y, label='Données réelles')
plt.plot(X, y, color='red', label='droite de régression')
plt.title('Régression Linéaire ')
plt.xlabel('Nombre d\'heures d\'étude')
plt.ylabel('Note')
plt.legend()
plt.show()





