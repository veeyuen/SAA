import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

df = pd.read_csv("mens_200m.csv")

st.dataframe(df)

st.line_chart(df['MARK'])

#fig, ax = plt.subplots()
#ax = df['MARK'].plot.barh(stacked=True)
#st.pyplot(fig)
