from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
        st.markdown("""
                    # Aplikasi
                    """, unsafe_allow_html = False)
        selected = option_menu(
            menu_title = None, 
            options = ["Home","Analisis Komentar", "Dataset"], #required
            icons = ["card-text", "file", "image"], #optional
            
            default_index = 0, #optional
        )
        return selected