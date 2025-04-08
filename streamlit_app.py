import streamlit as st

st.set_page_config(
    page_title= "Serie A",
    layout= "centered",
    initial_sidebar_state= "collapsed"
)

import pandas as pd
import numpy as np

#Dataset

data={
    "players": ['Thuram', 'Lookman', 'Martinez', 'Paz', 'Calhanoglu'],
    "goals": [14,13,11,6,5],
    "assists": [4,5,3,5,4],
    "matches": [26,23,28,24,21],
    "average distance": [9.11,10.30,9.74,10.33,11.26],
    "pass accuracy": [74.5,78.6,76.9,83.8,90.7]
}

df=pd.DataFrame(data)
#st.dataframe(df)

#Application
st.title(":red[Serie A: top 5 players]")

st.write(">**Goal bar chart**")
st.bar_chart(df,x="players",y="goals",color="#44c544")

st.write(">**Matches and assists line chart**")
st.line_chart(df,x="players",y=["matches","assists"],color=["#44c544","#ff4035"])

st.write(">**Pass accuracy and average distance covered area chart**")
st.area_chart(df,x="players",y="pass accuracy", color="#44c544")
st.area_chart(df,x="players",y="average distance", color="#44c544")