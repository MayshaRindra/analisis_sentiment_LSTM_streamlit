from pickle import bytes_types
import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import pandas as pd
import io
from io import StringIO
import modals
import json
import numpy as np
import cv2
import plotly.express as px



    
def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    st.subheader("Aplikasi sentiment analisis mengenai kebijakan pemerintah")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('./images/sentiment.jpg')

    with col3:
        st.write(' ')
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px; " /> """)
    