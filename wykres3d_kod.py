import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

df = pd.read_excel('ceny_stand.xlsx', decimal=',')

df_3 = df[df['Dzien'] == 4.00]
df_3 = df_3.drop(df_3.columns[[2]], axis=1)
df_3 = pd.DataFrame(df_3)
df_3['Data'] = pd.to_datetime(df_3['Data'], format='%d.%m.%Y %H:%M')
df_3['Godzina'] = df_3['Data'].dt.hour
df_3['Dzien'] = df_3['Data'].dt.day

iteracja = []
zmienna = 0
for i in range(len(df_3)):
    if df_3['Dzien'].iloc[i] == df_3['Dzien'].iloc[i-1] :
        
        iteracja.append (zmienna)
    else:
        zmienna += 1
        iteracja.append (zmienna)

df_3['Ieracja'] = iteracja

# Tworzenie wykresu 3D w postaci powierzchniowej
fig = plt.figure(figsize=(40,10), dpi = 1000)                          # figsize=(10,6), dpi = 1000
ax = fig.add_subplot(111, projection='3d')

# Rysowanie wykresu 3D w postaci powierzchniowej z inną mapą kolorów
surf = ax.plot_trisurf(df_3['Ieracja'], df_3['Godzina'], df_3['Ceny energii'], cmap='inferno', linewidth=0.2, antialiased=True)

# Ustalanie etykiet osi
ax.set_xlabel('Numer iteracyjny środy', fontsize=12)
ax.set_ylabel('Godzina', fontsize=12)
ax.set_zlabel('Cena energii', fontsize=12)

#ax.invert_yaxis()
#ax.invert_xaxis()

# Dostosowanie podziałek na osi Y
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Wyświetlenie kolorowej tabeli z legendą
#fig.colorbar(surf, ax=ax, label='Cena energii')

# Zmiana kątów widoku
ax.view_init(elev=34, azim=-58)

#ax.grid(True)

# Wyświetlenie wykresu
plt.show()