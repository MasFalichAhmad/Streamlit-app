import streamlit as st

def show_how_it_works():
    st.markdown("""
    ## How It Works
    - This application uses the MediaPipe library to detect poses and analyze movements.
    - It can track key points on the body to provide feedback on your form during exercises.
    - The percentage in the middle of the screen indicates the current position in the push-up movement:
        - 0%: Indicates the starting position of the push-up, with arms fully extended.
        - 100%: Indicates the lowest point of the push-up, with elbows bent at approximately 90 degrees.
    """)

    st.markdown("Wanna know more? [Contact Us](mailto:kotagirianshul@gmail.com)")
    st.image("mediapipe.png", caption="Mediapipe detection", use_column_width=True)

