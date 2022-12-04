import streamlit as st
import streamlit.components.v1 as components
import requests
import moss_graph

st.title('Visualizing Moss Output Using Graph Theory')

url = st.text_input("Enter Moss URL")

if url:
    res = requests.get(url)

    if ("Not Found" in res.text):
        st.markdown(res.text,unsafe_allow_html=True)
    else:
        data = moss_graph.parse(url)

        st.sidebar.title('Choose settings')

        node_distance = st.sidebar.slider('Change node distance', step=50, value=200, min_value=0, max_value=400)
        spring_length = st.sidebar.slider('Change spring length', step=50, value=200, min_value=0, max_value=400)

        edge_scale = st.sidebar.slider('Change scale of edge weight', step=5, value=10, min_value=0, max_value=40)
        node_size = st.sidebar.slider('Change node size', step=5, value=20, min_value=0, max_value=40)

        node_color = st.sidebar.color_picker("Change node color", value='#97c2fc')
        edge_color = st.sidebar.color_picker("Change edge color", value='#6E8EC4')

        moss_graph.create(data, node_distance, spring_length, edge_scale, node_size, node_color, edge_color)
        
        HtmlFile = open("nx.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code, height=900, width=801)

# streamlit run app.py