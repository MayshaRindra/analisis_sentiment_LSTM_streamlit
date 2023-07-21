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


# data=pd.read_csv('Hasil_pelabelan.csv')
# if st.checkbox("Show Data"):
#     st.write(data.head(50))

# def uploadFile():
#     uploaded_file = st.file_uploader("Upload an file", type=['csv', 'xlsx'])
#     print("Uploaded File :", uploaded_file)
#     if uploaded_file is not None:
#         content = Image.open(uploaded_file)
#         content = np.array(content) #pil to cv
#         # content = cv2.cvtColor(content, cv2.COLOR_RGB2BGR)
#         # st.text(np.shape(content))
#         shape = np.shape(content)
#         if len(shape)<3:
#             st.error('Your file has a bit-depth less than 24. Please upload an image with a bit-depth of 24.')
#             return
        
#         emotions, topEmotion, image = modals.imageEmotion(content)

#     else:
#         emotions = None
        
#     if uploaded_file is not None:
#         # To read file as bytes:
#         file_details = {"filename":uploaded_file.name, "filetype":uploaded_file.type, "filesize": uploaded_file.size }
#         printImageInfoHead()
#         with st.expander("See JSON Object"):
#             with st.container():
#                 st.json(json.dumps(file_details))
#                 st.text("")
#                 st.subheader("Image")
#                 st.image(load_image(uploaded_file), caption=uploaded_file.name, width=250)

#     if emotions is not None and len(emotions)==0:
#         st.text("No faces found!!") 
#     if emotions is not None:
#         # Showcasing result
#         printResultHead()
#         with st.expander("Expand to see individual result"):
#             with st.container():
#                 st.write("")
#                 st.write("")
#                 contentcopy = Image.open(uploaded_file)
#                 contentcopy = np.array(contentcopy)
#                 for i in range (len(emotions)):
#                     showEmotionData(emotions[i], topEmotion, contentcopy, i+1)
        
        
#         st.write("")
#         st.write("")
#         col1, col2 = st.columns([4,2])
        
#         with col1:
#             st.image(image, width=300)
#         with col2:
#             st.metric("Top Emotion", topEmotion[0].capitalize() + " " + getEmoji[topEmotion[0]], None)
#             st.metric("Emotion Percentage", str(round(topEmotion[1]*100, 2)), None)
        
    
def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    # st.markdown("### User Input Text Analysis")
    # st.subheader("CSV Analysis")
    # st.text("Input an file and let's find sentiments in there.")
    # st.text("")
    # option = st.selectbox(
    #  'How would you like to provide an file ?',
    #  ('Upload One',))
    data=pd.read_csv('labeldata.csv')
    if st.checkbox("Show Data"):
        st.write(data.head(50))
    
    st.subheader('Text Analisis')
    tweets = st.radio('Sentiment Type', ('Negatif','Positif'))
    st.write(data.query('Label==@tweets')[['Text']].sample(1).iat[0,0])
    st.write(data.query('Label==@tweets')[['Text']].sample(1).iat[0,0])
    st.write(data.query('Label==@tweets')[['Text']].sample(1).iat[0,0])
    st.write(data.query('Label==@tweets')[['Text']].sample(1).iat[0,0])
    st.write(data.query('Label==@tweets')[['Text']].sample(1).iat[0,0])
    
    select = st.selectbox('Visualisation of tweets', ['Histogram', 'Pie Chart'],key=1)
    sentiment =data['Label'].value_counts()
    sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Text.1':sentiment.values})
    st.markdown('### Sentiment count')
    if select == 'Histogram':
        fig = px.bar(sentiment, x='Sentiment', y='Text.1', color='Text.1', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment, values='Text.1', names='Sentiment')
        st.plotly_chart(fig)
    # if option=="Upload One":
    #     uploadFile()

        
    
        