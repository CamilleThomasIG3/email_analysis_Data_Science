import numpy as np
import pandas as pd
from stop_words import get_stop_words
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = pd.read_csv('data/mail.csv')

# ---- Les serveurs les + utilisés
# Récupération de la donnée du serveur email dans le champ 'destinataire'
data = data[data['destinataire'].str.contains("@")]
data['server_mail'] = data['destinataire'].str.split('@').str[-1]
data['server_mail'] = data['server_mail'].str.replace('>','')

# Colonnes pour le graphique
labels = data['server_mail'].value_counts().index
values = data['server_mail'].value_counts().values

# Création du graphique (Camembert)
fig_servers = px.pie(data['server_mail'], values=values, labels=labels, names=labels,
    title='Serveurs de réception les plus fréquents',
    color_discrete_sequence=px.colors.sequential.RdBu)
# Sauvegarde du graphique au format png
fig_servers.write_image('results/serveurs_reception_emails.png')


# ---- Jours recoit le plus de mails
# Récupération de la donnée de jour dans le champ 'date et heure'
data = data[data['date et heure'].str.contains('Mon,|Tue,|Wed,|Thu,|Fri,|Sat,|Sun,')]
data['jour'] = data['date et heure'].str.split(' ').str[0]

# Traduction des jours en français
data['jour'] = data['jour'].replace(
    {'Mon,':'Lundi', 'Tue,':'Mardi', 'Wed,':'Mercredi', 'Thu,':'Jeudi', 'Fri,': 'Vendredi', 'Sat,':'Samedi', 'Sun,':'Dimanche'})

# Création du graphique (en barres)
fig_days = px.bar(data['jour'].value_counts(), y='jour', 
    title="Nombre d'emails reçus par jour",
    labels={'jour':'Nombre d\'emails reçus', 'index':'Jours de la semaine'})
# Sauvegarde du graphique au format png
fig_days.write_image('results/jours_affluence_emails.png')


# ---- horaires recoit le plus de mails
# Récupération de la donnée de l'heure dans le champ 'date et heure'
data['heure'] = data['date et heure'].str.split(':').str[0].str.split(' ').str[-1]
df_heure = data['heure'].value_counts()
df_heure = df_heure.sort_index()

# Colonnes pour le graphique
labels_heure = df_heure.index
values_heure = df_heure.values

# Création du graphique (linéaire)
fig_heure = go.Figure(data=go.Scatter(
    x=labels_heure, y=values_heure, mode='lines'))

fig_heure.update_layout(title='Afluence de la réception d\'emails en fonction de l\'heure de la journée',
                xaxis_title='Heures de la journée',
                yaxis_title='Nombre moyen d\'emails reçus')
# Sauvegarde du graphique au format png
fig_heure.write_image('results/horaires_affluence_emails.png')


# ---- Mots les plus utilisés
# Récupération des stop words en français
stop_words = get_stop_words('fr')

# Récupération des mots du contenu du mail dans le champ 'contenu'
words_in_mail = data["contenu"].str.join("").to_string().split(" ")
# Supression des stop words dans le contenu
words_without_stop_words = [words_in_mail.lower() for words_in_mail in words_in_mail if words_in_mail.lower() not in stop_words]

# Supression des mots contenant des caractères non alphabétiques
words_only_alpha = []
for w in words_without_stop_words :
    if(w.isalpha()) :
        words_only_alpha.append(w) 

# Création du graphique (nuage de mots)
wordcloud = WordCloud (
                    background_color = 'white',
                    width = 512,
                    height = 384
                        ).generate(' '.join(words_only_alpha))
plt.imshow(wordcloud)
plt.axis('off')
# Sauvegarde du graphique au format png
plt.savefig('results/mots_les_plus_recus.png')