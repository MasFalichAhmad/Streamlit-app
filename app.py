import streamlit as st


def main():
    st.sidebar.title("Navigation")
    home_button = st.sidebar.button("Home")
    how_it_works_button = st.sidebar.button("How It Works")
    instructions_button = st.sidebar.button("Instructions")

    if home_button:
        show_home()
    elif how_it_works_button:
        show_how_it_works()
    elif instructions_button:
        show_instructions()
    else:
        show_home()  

if __name__ == "__main__":
    main()
