import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get(url="http://budget-app-backend-1:8000/v3/budget_item").json()
if "error" in list(response.keys()):
    st.title("Welcome to :red[Smart Budget] 👋")
    st.write("On this page you can see your budget list")
    st.write("seems like your budget is currently empty, please use the other pages to add budget items  👍 ")
else:
    name_list = []
    price_list = []
    tag_list = []
    for item in response.values():
        name_list.append(item["name"])
        price_list.append(item["price"])
        tag_list.append(item["tag"])
    df = pd.DataFrame({"name": name_list, "price": price_list,"tag":tag_list})

    result = {}
    for item in response.values():
        if item["tag"] not in result:
            result[item["tag"]] = item["price"]
        else:
            result[item["tag"]] = result[item["tag"]] + item["price"]
    tag_list_B = list(result.keys())
    price_list_B = list(result.values())

    df_B = pd.DataFrame({"tag":tag_list_B,"price":price_list_B})



        
    st.title("Welcome to :red[Smart Budget]")
    st.write("On this page you can see your budget list")
    st.dataframe(df)
    st.write("And here you can see the breakdown of the budget by tag")
    st.dataframe(df_B)
    plt.rcParams.update({"text.color": "white"})
    fig, ax = plt.subplots()
    ax.pie(price_list_B, labels=tag_list_B, autopct="%1.1f%%")
    fig.set_facecolor(color="None")
    st.pyplot(fig)
