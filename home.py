import streamlit as st
import cv2
from pose_detector import poseDetector
from app_helpers import process_frame 
import time

def show_home():
    st.markdown("<h1 style='color: #4CAF50; text-align: center;'>TEST PUSH UP</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #FF5722; text-align: center; font-size: 20px;'>NULL MSIH TEST</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True) 

    st.title("Mulai sekarang! (Tekan tombol dibawah)")

    left_column, middle_column, right_column = st.columns([1, 3, 1])

    with middle_column:
        st.markdown(
            "<style>div.stButton > button:first-child { width: 100%; height: 80px; font-size: 20px; }</style>", 
            unsafe_allow_html=True
        )
        if st.button("Push Up Counter", key='push_up_button'):
            use_webcam = True
        else:
            use_webcam = False

    st.markdown("<br>", unsafe_allow_html=True) 

    stframe = st.empty()

    if use_webcam:
        detector = poseDetector() 
        cap = cv2.VideoCapture(0)
        count = 0
        direction = 0
        formVal = 0
        pushup_count = 0

        start_time = time.time()
        while cap.isOpened():
            ret, img = cap.read()
            if not ret:
                break

            img, count, direction, formVal, pushup_count = process_frame(detector, img, count, direction, formVal, cap, pushup_count)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            stframe.image(img)

            elapsed_time = time.time() - start_time
            if elapsed_time >= 30:
                break

        cap.release()
        cv2.destroyAllWindows()
        st.write("Time's up!")
        st.write(f"Number of push-ups completed: {pushup_count}. Good Job!")

