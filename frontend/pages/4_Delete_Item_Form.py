import streamlit as st
import requests
import pandas as pd
from uuid import UUID

st.title("Delete Item Form")
st.write("On this page you can delete an item from your list")


response = requests.get(url="http://budget-app-backend-1:8000/v3/budget_item/id").json()
index_list = []
name_list = []
for item in response:
    index_list.append(item)
    name_list.append(response[item])
df = pd.DataFrame({"index": index_list, "name": name_list})
if df["index"][0] == "error":
    st.write("Budget is currently empty")


else:
    index = st.selectbox(
        "please select the index of the product you would like to delete", index_list
    )
    response = requests.get(
        url=f"http://budget-app-backend-1:8000/v3/budget_item/id/{df['name'][int(index)]}"
    ).json()
    st.table(response)
    with st.form("Delete Form"):
        index = st.text_input("please enter the index of item to confirm")
        submitted = st.form_submit_button("submit")
        if submitted:
            response = requests.delete(
                url=f"http://budget-app-backend-1:8000/v3/budget_item/{df['name'][int(index)]}"
            ).json()
            st.table(response)
