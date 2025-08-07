import streamlit as st
import sqlite3
from database import authenticate_user
import login_page

def forgot_password_page():
     
     st.title("Forgot Password")
     email = st.text_input("Enter your email address")
     new_password = st.text_input("Enter new password", type="password")
     confirm_password = st.text_input("Confirm new password", type="password")

     if st.button("Update Password"):
        if new_password == confirm_password:
            # Update the password in the database
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
            conn.commit()
            conn.close()
            st.success("Password updated successfully! Please login with your new password.")
            navigate_to_page("login")
        else:
            st.error("Passwords do not match.")

