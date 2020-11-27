import numpy as np
import pandas as pd
from stop_words import get_stop_words
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# data = pd.read_csv('data/test.csv')
data = pd.read_csv('data/mail.csv')

# # Taille moyenne contenu
# data['count_contenu'] = data['contenu'].str.split().str.len()
# print("--------------- Nombre de mots moyen du contenu ---------------")
# print(int(data['count_contenu'].mean()))

# Les serveurs les + utilisés
# data = data[data['destinataire'].str.contains("@")]
# data['server_mail'] = data['destinataire']
# print(data['server_mail'])
# data['server_mail'] = data['destinataire'].str.split('@').str[-1]
# print("--------------- Serveur email les + utilisés ---------------")
# data['server_mail'] = data['server_mail'].str.replace('>','')
# print(data['server_mail'].value_counts())

# df.loc[df.value_counts() < 2.e6, 'server_mail'] = 'Autres serveurs' # Represent only large countries
# data['server_mail'].value = data['server_mail'].loc[data['server_mail'].value_counts() < 2, 'server_mail'] = 'Autres serveurs'

# labels = data['server_mail'].value_counts().index
# values = data['server_mail'].value_counts().values

# fig_servers = px.pie(data['server_mail'], values=values, labels=labels, names=labels,
#     title='Serveurs de réception les plus fréquents',
#     color_discrete_sequence=px.colors.sequential.RdBu)
# fig_servers.show()

# # # Jour recoit le plus de mails
# data = data[data['date et heure'].str.contains('Mon,|Tue,|Wed,|Thu,|Fri,|Sat,|Sun,')]
# data['jour'] = data['date et heure'].str.split(' ').str[0]
# print("--------------- Jours receptionne le + de mails ---------------")
# data['jour'] = data['jour'].replace(
#     {'Mon,':'Lundi', 'Tue,':'Mardi', 'Wed,':'Mercredi', 'Thu,':'Jeudi', 'Fri,': 'Vendredi', 'Sat,':'Samedi', 'Sun,':'Dimanche'})
# print(data['jour'].value_counts())

# fig_days = px.bar(data['jour'].value_counts(), y='jour', 
#     title="Nombre d'emails reçus par jour",
#     labels={'jour':'Nombre d\'emails reçus', 'index':'Jours de la semaine'})
# fig_days.show()

# # Tranche horaire recoit le plus de mails
# data['heure'] = data['date et heure'].str.split(':').str[0].str.split(' ').str[-1]

# print(data['date et heure'])
# print("--------------- Tranche horaire receptionne le + de mails ---------------")
# df_heure = data['heure'].value_counts()
# df_heure = df_heure.sort_index()
# print(df_heure)

# labels_heure = df_heure.index
# values_heure = df_heure.values

# fig_heure = go.Figure(data=go.Scatter(
#     x=labels_heure, y=values_heure, mode='lines'))

# fig_heure.update_layout(title='Afluence de la réception d\'emails en fonction de l\'heure de la journée',
#                 xaxis_title='Heures de la journée',
#                 yaxis_title='Nombre moyen d\'emails reçus')
# fig_heure.show()

# # # Stop words
# stop_words = get_stop_words('fr')
# stop_words.append('')
# for i in range(10) :
#     stop_words.append(str(i))
    
# words_in_mail = data["contenu"].str.join("").to_string().split(" ")
# words_without_stop_words = [words_in_mail.lower() for words_in_mail in words_in_mail if words_in_mail.lower() not in stop_words]
# most_common = Counter(words_without_stop_words).most_common(10)
# print("--------------- Mots les + recus ---------------")
# print(most_common)

# wordcloud = WordCloud (
#                     background_color = 'white',
#                     width = 512,
#                     height = 384
#                         ).generate(' '.join(words_without_stop_words))
# plt.imshow(wordcloud) # image show
# plt.axis('off') # to off the axis of x and y
# plt.savefig('Plotly-World_Cloud.png')
# plt.show()