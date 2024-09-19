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
        file = open("userlist.csv","r", encoding="utf-8-sig")
        user_found = False
        for line in file:
            lines = line.strip().split(",")
            username = lines[0]
            password = lines[1]
            if enterusername == username and enterpassword == password:
                st.session_state.logged_in = True
                st.success("login successful")
                user_found = True
                break
        if not user_found:
            st.error("invalid username or password")
        file.close()
def dashboard():
    st.write("welcome admin")
    if st.button("Sign out"):
        st.session_state.logged_in = False
    st.title("User Management and Login record")
    choice = st.sidebar.radio("please select add or remove",[":rainbow[add]","rainbow[View]"])
    if choice == ":rainbow[add]":
        username = st.text_input("please enter username to add")
        password = st.text_input("please enter password", type="password")
        if st.button("add user"):
            with open("userlist.csv","a", newline='') as file:
                file.write(username+","+password+"\n")
        elif choice == ":rainbow[remove]":
            username = st.text_input("please enter username to remove")
            if st.button("remove user"):
                df = pd.read_csv("userlist.csv")
                if username in df["username"].values:
                    df = df[df["username"] != username]
                    df.to_csv("userlist.csv", index=False)
                    st.succes(f"user {username} removed successfully.")
        else:
            st.error(f"username {username} not found in the data")
    else:
        df = pd.read_csv("userlist.csv")
        st.dataframe(df)
        df = pd.read_csv("userlog.csv")
        st.dataframe(df)
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
if st.session_state.logged_in:
    dashboard()
else:
    login()
