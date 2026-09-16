import streamlit as st

email = st.text_input("Enter Email Here-")
password = st.text_input("Enter Password Here-")

butn = st.button("Click To Login")

if butn:
    if email == "abhinav@gmail.com" and password== "abhinav101101":
        st.success("Login Successfully")
    else:
        st.error("Login Failed!")