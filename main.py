import streamlit as st
from apps import main_app
from utils import Calendar
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title='App Reservas',
    page_icon='🎸',
    layout='wide'#'centered'
    )

st.session_state['n_salas'] = 2
if 'now' not in st.session_state:
    st.session_state['now'] = datetime.now()
if 'reservas' not in st.session_state:
    st.session_state['reservas'] = pd.read_csv('data/events.csv')
if 'bands' not in st.session_state:
    st.session_state['bands'] = pd.read_csv('data/bands.csv')
if 'users' not in st.session_state:
    st.session_state['users'] = pd.read_csv('data/users.csv')
if 'calendars' not in st.session_state:
    st.session_state['calendars'] = {}
    for sala in range(st.session_state['n_salas']):
        st.session_state['calendars'][sala] = Calendar(st.session_state['now'].year,
                                                       st.session_state['now'].year,
                                                       sala)


main_app()