import streamlit as st 

# This is a simple Streamlit app that demonstrates basic features like navigation, text input, and displaying messages.

def main():
    st.set_page_config(page_title="Simple Streamlit App", layout="centered")
    
    st.title("Welcome to My Simple Streamlit App")
    st.write("This is a basic web app using Streamlit.")
    
    # Sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])
    
    if page == "Home":
        st.header("Home Page")
        st.write("This is the home page content.")
        
    elif page == "About":
        st.header("About")
        st.write("This is a simple Streamlit application demonstrating its basic features.")
        
    elif page == "Contact":
        st.header("Contact")
        name = st.text_input("Enter your name")
        message = st.text_area("Enter your message")
        if st.button("Submit"):
            st.success(f"Thank you, {name}. Your message has been received!")

if __name__ == "__main__":
    main()