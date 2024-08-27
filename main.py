import streamlit as st
from apps import main_app

st.set_page_config(
    page_title='App Reservas',
    page_icon='🎸',
    layout='wide'
    )

main_app()