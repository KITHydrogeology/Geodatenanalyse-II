# Aufgabe 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
data = pd.read_csv("h007b.csv", header=None)

# relevante Spalten in Datum und Zeit konvertieren
data['Datetime'] = pd.to_datetime(data.iloc[:, 0].astype(str) + '-' + data.iloc[:, 1].astype(str) + '-' + data.iloc[:, 2].astype(str) + ' ' + data.iloc[:, 3].astype(str) + ':' + '00')
data

#%
idx = data.iloc[:, 4] < 0

data.loc[idx, 4] = np.nan

#%%

plt.plot(data['Datetime'], data.iloc[:, 4] )

#%%

new_data = pd.DataFrame({'Datetime[GMT]': data['Datetime'].values, 'Sea level [mm]': data.iloc[:, 4].values})

new_data.to_csv('Palau_sea-level.csv', index = False)