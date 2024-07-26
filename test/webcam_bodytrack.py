#webcam_bodytrack.py

import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

# Function to load the MediaPipe Pose model
def load_pose_model():
    mp_pose = mp.solutions.pose
    return mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to process the webcam video stream
def run_webcam(pose_model):
    cap = cv2.VideoCapture(0)
    with mp_pose.Pose() as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            # Convert the image to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the image with MediaPipe Pose model
            results = pose.process(frame_rgb)

            # Draw landmarks on the frame
            if results.pose_landmarks:
                mp.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Display the frame in Streamlit
            st.image(frame, channels="BGR", use_column_width=True)

            # Check for key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# Main function to run the Streamlit app
def main():
    st.title("Webcam Body Tracker")

    # Load MediaPipe Pose model
    pose_model = load_pose_model()

    # Display webcam video stream and run body tracking
    run_webcam(pose_model)

if __name__ == '__main__':
    main()
