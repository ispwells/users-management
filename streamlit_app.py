import streamlit as st
import pandas as pd
import datetime

def login():
    st.title("login")
    st.write("this app allows you to add and remove users")
    st.write("please try it out, remember to click Check User")
    st.write("username = Dave")
    st.write("password = p1")
    enterusername = st.text_input("please enter username to update system")
    enterpassword = st.text_input("please enter password", type="password")
    if st.button("check user"):
login()
