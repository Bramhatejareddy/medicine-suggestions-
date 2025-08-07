import streamlit as st
import sqlite3
from database import authenticate_user
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()
# Add this function to handle the "Forgot Password" page
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


def login_page():
    # Center the login form using Streamlit form layout
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url("https://img.freepik.com/premium-photo/scientific-molecule-background-with-flow-waves-medicine-science-technology-chemistry-wallpaper-o_230610-906.jpg");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .my-login-card {
        max-width: 200px; /* Adjust width here */
        margin: auto; /* Center horizontally */
        background-color: rgba(255, 255, 255, 0.8); /* Optional: semi-transparent background */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown('<div class="my-login-card">', unsafe_allow_html=True)
    with st.form(key="login_form"):
        st.markdown("<h3 style='text-align:center;'>Login</h3>", unsafe_allow_html=True)
        # Title
        

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # Submit button inside the form
        col1,col2,col3,col4=st.columns([1,2,1,1])
        with col1:
            if st.form_submit_button("Login 🔐"):
                if authenticate_user(email, password):
                    st.success(f"Login successful.")
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = email

                    navigate_to_page("user_home")
                else:
                    st.error("Invalid email or password.")
        with col2:
            if st.form_submit_button("Create account👤"):
                navigate_to_page("signup")
        with col3:
                if st.form_submit_button("Forgot Password?"):
                    navigate_to_page("forgot_password")