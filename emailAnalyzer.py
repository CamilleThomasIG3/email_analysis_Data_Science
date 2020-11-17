import numpy as np
import pandas as pd
from stop_words import get_stop_words

data = pd.read_csv('test.csv')

# Taille moyenne contenu
data['count_contenu'] = data['contenu'].str.split().str.len()
print(data['count_contenu'].mean())

# Les serveurs les + utilisés
data['server_mail'] = data['destinataire'].str.split('@').str[-1]
print(data['server_mail'].value_counts())

# Jour recoit le plus de mails
data['jour'] = data['date et heure'].str.split(' ').str[0]
print(data['jour'].value_counts())

# Tranche horaire recoit le plus de mails
data['heure'] = data['date et heure'].str.split(' ').str[-2].str.split(':').str[0]
print(data['heure'].value_counts())

# Stop words
stop_words = get_stop_words('fr')
#print(stop_words)