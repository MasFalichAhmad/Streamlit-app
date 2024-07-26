import streamlit as st

def show_instructions():
    st.markdown("""
    ## Instructions
    - Follow the bar on the top. Use it to understand when to go down and when to go up during push-ups.
    - To make sure the program works effectively, please make sure you are in push-up position and the camera is an appropriate distance away.
    - You will be given 30 seconds to complete as many push-ups as you can, and based on your results, the program will provide an AI-generated plan of action that will help you further your workout goals.
    """)

    st.markdown("Having trouble? [Contact Us](mailto:kotagirianshul@gmail.com)")
    st.image("final.png", caption="Finished workout", use_column_width=True)

