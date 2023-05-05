import streamlit as st
import requests
import pandas as pd
st.title("Edit Form")
st.write("On this page you can edit an item already on your list")

response = requests.get(url="http://project-backend-1:8000/budget_item/id").json()
index_list = []
name_list = []
for item in response:
    index_list.append(item)
    name_list.append(response[item])
df = pd.DataFrame({"index":index_list,"name":name_list})
st.dataframe(df)

with st.form("Edit Form"):
    index = st.text_input("please enter the index of item")
    st.write("please provide the information about the purchased item")
    name = st.text_input("please enter item name")
    price = st.text_input("please enter item price")
    tag = st.text_input("please enter item tag",placeholder="untagged")
    submitted = st.form_submit_button("submit")
    if submitted:
        response = requests.put(url=f"http://project-backend-1:8000/budget_item/{index}",json={"name":name,'price':price,'tag':tag}).json()
        st.table(response)
