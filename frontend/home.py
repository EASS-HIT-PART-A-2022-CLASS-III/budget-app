import streamlit as st
import requests
import json
import pandas as pd


response = requests.get(url="http://127.0.0.1:8000/budget_item").json()
budget_list =[]
st.title("Welcome to Smart Budget")
st.write("On this page you can see your budget list")
for key in response:
    budget_list.append((key,response[key]))
df = pd.DataFrame(columns=["Tag","Price"])
st.write(budget_list)
st.markdown("""# this is a title.

## this is a sub title

this is a normal text example

""")

st.button("this is a button",help="this a button dammit")

with st.form("this is a form"):
    st.write("this is inside the form")
    text = st.text_area("this is paramater 1")
    checkbox_val = st.checkbox("form checkbox")
    submitted = st.form_submit_button("submit")
    if submitted:
        st.write("checkbox val",checkbox_val,text)