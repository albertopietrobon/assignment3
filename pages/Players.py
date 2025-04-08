import streamlit as st
import pandas as pd

data={
    "players": ['Thuram', 'Lookman', 'Martinez', 'Paz', 'Calhanoglu'],
    "goals": [14,13,11,6,5],
    "assists": [4,5,3,5,4],
    "matches": [26,23,28,24,21],
    "average distance": [9.11,10.30,9.74,10.33,11.26],
    "pass accuracy": [74.5,78.6,76.9,83.8,90.7]
}

df=pd.DataFrame(data)

st.title(":red[Player stats]")

st.selectbox("Select a player:",df["players"])