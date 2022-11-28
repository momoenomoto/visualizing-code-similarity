import streamlit as st
import streamlit.components.v1 as components


st.title('Visualizing Moss Output Using Graph Theory')

st.sidebar.title('Choose settings')


HtmlFile = open("nx.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=900, width=801)
