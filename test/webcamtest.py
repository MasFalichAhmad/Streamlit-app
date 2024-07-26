import streamlit as st
import cv2
from PIL import Image
import numpy as np

def main():
    st.title("Webcam Live Feed")
    
    # Menampilkan pilihan untuk memulai streaming webcam
    run = st.checkbox('Run')
    
    # Inisialisasi kamera menggunakan OpenCV
    cap = cv2.VideoCapture(0)
    
    while run:
        ret, frame = cap.read()
        
        # Mengonversi frame menjadi format yang dapat ditampilkan oleh PIL
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(frame)
        
        # Menampilkan frame di Streamlit
        st.image(img_pil, caption='Webcam', use_column_width=True)
        
        # Tunggu untuk input dari user
        run = st.checkbox('Run')  # checkbox untuk menghentikan streaming
    
    # Setelah selesai, lepaskan kamera dan tutup tampilan Streamlit
    cap.release()
    st.write("Stream Stopped")

if __name__ == '__main__':
    main()
