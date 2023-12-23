import streamlit as st
import streamlit_antd_components as sac
from views import bulk_meta, about
from PIL import Image

favicon = Image.open("./assets/favicon.png")

st.set_page_config(
    page_title="Bulk Meta Tags Creator",

    layout="wide",
    initial_sidebar_state='collapsed',
)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


if menu == 'Bulk Meta':
    bulk_meta.createPage()
   

