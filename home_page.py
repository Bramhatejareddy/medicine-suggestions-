import streamlit as st
from database import authenticate_user

# Navigation function
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()
def home_page():
    # Add info about the eye disease detection system in the sidebar
    st.sidebar.markdown(
        """
        <h2 style='color: black ; text-align: center; color: red;'>Personalized Medicine Suggestions</h2>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.image('https://static.vecteezy.com/system/resources/previews/024/585/326/non_2x/3d-happy-cartoon-doctor-cartoon-doctor-on-transparent-background-generative-ai-png.png')
    st.sidebar.markdown(
        """
        <p style='color: green; text-align: center;'>This web application is designed to recommend the drugs for various problems using machine learning algorithms.</p>
        """,
        unsafe_allow_html=True
    )
    # Type of eye diseases
    st.sidebar.markdown(
        """
        <h3 style='color: maroon; text-align: center;'>Types of Problems</h3>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <ul>
            <li>Fever</li>
            <li>Cold</li>
            <li>Headache</li>
            <li>Stomach Pain</li>
            <li>Diabetes</li>
            <li>Heart Problems</li>
            <li>Eye Problems</li>
            <li>Ear Problems</li>
            <li>Throat Problems</li>
            <li>Others</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url("https://media.istockphoto.com/id/1210316719/vector/the-team-of-doctors.jpg?s=612x612&w=0&k=20&c=IYaEXKkU11b4GnkkU1uKHrpkgMf_YjziURKkIYHwYsM=");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.8);
        background-blend-mode: fill;
        scrollbar=none;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center; padding: 1px; background-color: rgba(78, 78, 6, 0.8); border-radius: 70px;">
            <p style="color: white; font-size: 28px;"><b>Personalized Medicine Suggestions & Reminder System</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

   

    
            
    # Add custom CSS for form and button hover effects
    st.markdown("""
        <style>
        
        
        div.stButton > button {
            background: #fff;
            color: #6e6e16;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            font-size: 1rem;
            transition: background 0.2s, transform 0.2s;
            margin-bottom: 8px;
        }
        div.stButton > button:hover {
            background: #6e6e16;
            transform: scale(1.07);
        }
        
        </style>
    """, unsafe_allow_html=True)

    # Only this container and Streamlit form
    st.markdown('<div class="my-login-card">', unsafe_allow_html=True)
    with st.form(key="login_form"):
        st.markdown("<h3 style='text-align:center;'>Login</h3>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        col1, col2, col3 = st.columns([1, 1, 1])
        login = col1.form_submit_button("Login 🔐")
        signup = col2.form_submit_button("Create account👤")
        forgot = col3.form_submit_button("Forgot Password?")
        if login:
            if authenticate_user(email, password):
                st.success(f"Login successful.")
                st.session_state["logged_in"] = True
                st.session_state["current_user"] = email
                navigate_to_page("user_home")
            else:
                st.error("Invalid email or password.")
        if signup:
            navigate_to_page("signup")
        if forgot:
            navigate_to_page("forgot_password")
    st.markdown('</div>', unsafe_allow_html=True)