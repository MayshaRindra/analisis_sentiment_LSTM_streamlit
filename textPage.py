import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict(message):

 model=load_model('LSTM_model_1.h5')

 with open('tokenizer.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)
  x_1 = tokenizer.texts_to_sequences([message])
  x_1 = pad_sequences(x_1, maxlen=200)
  predictions = model.predict(x_1)[0][0]
  return predictions    

def renderPage():
    st.title("Sentiment Analisis😊😐😕😡")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 5px" /> """)
    # st.markdown("### User Input Text Analysis")
    st.subheader("User Input Text Analisis")
    st.text("Menganalisis data teks yang diberikan oleh pengguna dan menemukan sentimen didalamnya.")
    st.text("")
    userText = st.text_area('User Input', placeholder='Input Komentar disini!')
    st.text("")
    # type = st.selectbox(
    #  'Type of analysis',
    #  ('Positive/Negative/Neutral - TextBlob', 'Happy/Sad/Angry/Fear/Surprise - text2emotion'))
    st.text("")
    if st.button('Predict'):
      with st.spinner('Sedang menganalisa komentar …'):
        prediction=predict(userText)
        if prediction > 0.6:
            image = Image.open('./images/positive.PNG')
            st.success('Positif komentar dengan {:.2f} keakuratan'.format(prediction))
            st.balloons()
            st.image(image, caption=prediction)
        elif prediction <0.4:
            image = Image.open('./images/negative.PNG')
            st.error('Negatif komentar dengan {:.2f} keakuratan'.format(1-prediction))
            st.image(image, caption=prediction)
        else:
            st.warning('Tidak yakin! Coba untuk menambahkan beberapa kata tambahan') 
