import streamlit as st
st.title("Hello this is my first test")
st.write("This is my first try at a webpage")
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