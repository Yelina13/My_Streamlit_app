import streamlit as st
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

# link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
# df_weather = pd.read_csv(link)

# # Here we use "magic commands":
# df_weather

st.line_chart(df_weather['MAX_TEMPERATURE_C'])


# Conversion de la colonne 'date' en datetime (si nécessaire)
df_weather['DATE'] = pd.to_datetime(df_weather['DATE'])

# Suppression de la colonne 'quality'
df_weather = df_weather.drop(columns=['OPINION'])

# Sélection des colonnes numériques uniquement
df_numeric = df_weather.select_dtypes(include='number')

# Création de la figure et des axes pour la heatmap

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)


# APPLICATION DYNAMIQUE

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

st.link_button("Go to gallery", "https://streamlit.io/gallery")

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)


# CHALLENGE



# Charger le dataset
mpg = sns.load_dataset('mpg')

# Titre de l'application
st.title("Analyse de Corrélation et de Distribution des Voitures")

# Filtrer par région
region = st.radio("Filtrer par région", ("Tous", "US", "Europe", "Japon"))

if region == "US":
    mpg = mpg[mpg['origin'] == "usa"]
elif region == "Europe":
    mpg = mpg[mpg['origin'] == "europe"]
elif region == "Japon":
    mpg = mpg[mpg['origin'] == "japan"]

# Analyse de Corrélation
st.header("Analyse de Corrélation")
numeric_cols = mpg.select_dtypes(include=['float64', 'int64'])
corr = numeric_cols.corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)
st.write("""
Les corrélations montrent la relation entre les différentes variables. Une valeur de corrélation proche de 1 ou -1 indique une forte relation positive ou négative respectivement, tandis qu'une valeur proche de 0 indique une faible relation.
""")

# Analyse de Distribution
st.header("Analyse de Distribution")
fig, ax = plt.subplots()
sns.histplot(mpg['mpg'], kde=True, ax=ax)
st.pyplot(fig)
st.write("""
La distribution des miles par gallon (mpg) indique l'efficacité énergétique des voitures. Une distribution plus à droite indique des voitures plus économes en carburant.
""")

# Distribution par région
st.header("Distribution par Région")
fig, ax = plt.subplots()
sns.boxplot(x='origin', y='mpg', data=mpg, ax=ax)
st.pyplot(fig)
st.write("""
Cette boîte à moustaches montre la répartition des miles par gallon (mpg) pour chaque région. Elle permet de comparer l'efficacité énergétique des voitures entre les régions.
""")
