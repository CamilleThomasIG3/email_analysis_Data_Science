import numpy as np
import pandas as pd
from stop_words import get_stop_words
from collections import Counter

# data = pd.read_csv('data/test.csv')
data = pd.read_csv('data/mail.csv')

# Taille moyenne contenu
data['count_contenu'] = data['contenu'].str.split().str.len()
print("--------------- Nombre de mots moyen du contenu ---------------")
print(int(data['count_contenu'].mean()))

# Les serveurs les + utilisés
data['server_mail'] = data['destinataire'].str.split('@').str[-1]
print("--------------- Serveur email les + utilisés ---------------")
print(data['server_mail'].value_counts())

# Jour recoit le plus de mails
data['jour'] = data['date et heure'].str.split(' ').str[0]
print("--------------- Jours receptionne le + de mails ---------------")
print(data['jour'].value_counts())

# Tranche horaire recoit le plus de mails
data['heure'] = data['date et heure'].str.split(' ').str[4].str.split(':').str[0]
print("--------------- Tranche horaire receptionne le + de mails ---------------")
print(data['heure'].value_counts())

# Stop words
stop_words = get_stop_words('fr')
stop_words.append('')
for i in range(10) :
    stop_words.append(str(i))
    
words_in_mail = data["contenu"].str.join("").to_string().split(" ")
words_without_stop_words = [words_in_mail.lower() for words_in_mail in words_in_mail if words_in_mail.lower() not in stop_words]
most_common = Counter(words_without_stop_words).most_common(10)
print("--------------- Mots les + recus ---------------")
print(most_common)