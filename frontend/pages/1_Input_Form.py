import streamlit as st
import requests

st.title("Input Form")
st.write("On this page you can add an item to your list")

with st.form("Input Form"):
    st.write("please provide the information about the purchased item")
    name = st.text_input("please enter item name")
    price = st.text_input("please enter item price")
    tag = st.text_input("please enter item tag",placeholder="untagged")
    if tag == '':
        tag = "untagged"
    submitted = st.form_submit_button("submit")
    if submitted:
        response = requests.post(url="http://project-backend-1:8000/budget_item",json={"name":name,'price':price,'tag':tag}).json()
        st.table(response)
