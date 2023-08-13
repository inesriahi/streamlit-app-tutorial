import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
  return pd.read_csv(file)
  
file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
  df = load_data(file)
  
  n_rows = st.slider('Choose number of rows to display', min_value=5, max_value=len(df), step=1)
  
  columns_to_show = st.multiselect("Select columns to show", df.columns.to_list(), default=df.columns.to_list())
  numerical_columns = df.select_dtypes(include=np.number).columns.to_list()
  
  st.write(df[:n_rows][columns_to_show])
  
  tab1, tab2 = st.tabs(["Scatter plot", "Histogram"])
  
  with tab1:
    col1, col2, col3 = st.columns(3)
    
    with col1:
      x_column = st.selectbox('Select column on x axis:', numerical_columns)
    with col2:
      y_column = st.selectbox('Select column on y axis', numerical_columns)
    with col3:
      color = st.selectbox('Select column to be color', df.columns)
    
    fig_scatter = px.scatter(df, x = x_column, y=y_column, color=color)
    
    st.plotly_chart(fig_scatter)
  
  with tab2:
    histogram_feature = st.selectbox('Select feature to histogram', numerical_columns)
    fig_hist = px.histogram(df, x=histogram_feature)
    st.plotly_chart(fig_hist)