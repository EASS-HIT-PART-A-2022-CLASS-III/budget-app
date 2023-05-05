import streamlit as st
import requests
import pandas as pd
st.title("Delete Form")
st.write("On this page you can delete an item from your list")

response = requests.get(url="http://localhost:8000/budget_item/id").json()
index_list = []
name_list = []
for item in response:
    index_list.append(item)
    name_list.append(response[item])
df = pd.DataFrame({"index":index_list,"name":name_list})
st.dataframe(df)

with st.form("Delete Form"):
    index = st.text_input("please enter the index of item")
    submitted = st.form_submit_button("submit")
    if submitted:
        response = requests.delete(url=f"http://localhost:8000/budget_item/{index}").json()
        st.table(response)