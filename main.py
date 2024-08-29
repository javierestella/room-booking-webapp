import streamlit as st
from apps import main_app
from utils import create_calendar
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title='App Reservas',
    page_icon='🎸',
    layout='wide'#'centered'#'wide'
    )

if 'now' not in st.session_state:
    st.session_state['now'] = datetime.now()
if 'reservas' not in st.session_state:
    st.session_state['reservas'] = pd.read_csv('data/events.csv')
if 'bands' not in st.session_state:
    st.session_state['bands'] = pd.read_csv('data/bands.csv')
if 'users' not in st.session_state:
    st.session_state['users'] = pd.read_csv('data/users.csv')
if 'calendar' not in st.session_state:
    st.session_state['calendar'] = create_calendar(st.session_state['now'].year, 
                                                   st.session_state['now'].month,
                                                   st.session_state['reservas'])

main_app()