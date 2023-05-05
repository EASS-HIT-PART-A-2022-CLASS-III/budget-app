import streamlit as st
import requests
import pandas as pd
st.title("Tags Form")
st.write("On this page you can see all the items that were tagged a certain tag")

with st.form("Tag Form"):
    tag = st.text_input("please enter tag")
    submitted = st.form_submit_button("submit")
    if submitted:
        response = requests.get(url=f"http://localhost:8000/budget_item/tag/{tag}").json()
        name_list = []
        price_list = []
        for item in response:
            name_list.append(item)
            price_list.append(response[item])
        df = pd.DataFrame({"name":name_list,"price":price_list})
        st.dataframe(df)
