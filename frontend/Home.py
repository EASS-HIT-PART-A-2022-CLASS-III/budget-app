import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get(url="http://budget-app-backend-1:8000/v2/budget_item").json()
type_list = []
price_list = []
for item in response:
    type_list.append(item)
    price_list.append(response[item])
df = pd.DataFrame({"type": type_list, "price": price_list})

st.title("Welcome to :red[Smart Budget]")
st.write("On this page you can see your budget list")
if df["type"][0] == "error":
    st.write("Budget is currently empty")
else:
    st.dataframe(df)

if "budget is empty" not in price_list:
    plt.rcParams.update({"text.color": "white"})
    fig, ax = plt.subplots()
    ax.pie(price_list, labels=type_list, autopct="%1.1f%%")
    fig.set_facecolor(color="None")
    st.pyplot(fig)
