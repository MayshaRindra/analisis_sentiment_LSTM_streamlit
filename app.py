import streamlit as st
import sidebar
import textPage
# import audioPage
import DatasetPage
import Home


page = sidebar.show()

if page=="Home":
    Home.renderPage()
elif page=="Analisis Komentar":
    textPage.renderPage()
elif page=="Dataset":
    DatasetPage.renderPage()
