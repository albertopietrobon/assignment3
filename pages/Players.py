
import streamlit as st
import pandas as pd
import plotly.express as px


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

choice = st.selectbox("Select a player:",df["players"])
stats=df.query('players==@choice').copy()
#st.dataframe(stats)
fig = px.line_polar(stats,r=stats.iloc[0,1:],theta=stats.columns[1:],
                    line_close=True, markers=True,range_r=(0,100), template="plotly_dark")
st.plotly_chart(fig)

