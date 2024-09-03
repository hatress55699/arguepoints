"""
Step 2: Integrate with Streamlit

to run this:
    go to anadomda prompt, or any cmd

activate envsound3    
cd "C:/Users/doya/Desktop/Python_stuff/reddit_visualisation"
streamlit run streamlit_step_2.py

To stop the Streamlit server, return to the Anaconda Prompt and press Ctrl + C.

"""

import streamlit as st

# Define the path to the existing streamlit_network.html file
html_file_path = "C:\\Users\\doya\\Desktop\\Python_stuff\\reddit_visualisation\\streamlit_network.html"

# Read the HTML file and display it in Streamlit
with open(html_file_path, 'r', encoding='utf-8') as HtmlFile:
    source_code = HtmlFile.read()

# Set up the Streamlit app
st.title("Interactive Graph Visualization with Pyvis and Streamlit")

# Embed the HTML file content within the Streamlit app
st.components.v1.html(source_code, height=600, width=800)
