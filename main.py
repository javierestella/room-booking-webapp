import streamlit as st
from apps import app
import utils as u
from datetime import datetime
import pandas as pd
import os

st.set_page_config(
    page_title='App Reservas',
    page_icon='🎸',
    layout='wide'#'centered'
    )

st.session_state['n_salas'] = 2
if 'now' not in st.session_state:
    st.session_state['now'] = datetime.now()

if 'reservas' not in st.session_state:
    headers = ['email', 'band', 'start_date','start_time','duration','confirmed','sanctioned','sala']
    st.session_state['reservas'] = u.read_csv('data/events.csv', headers)

if 'bands' not in st.session_state:
    headers = ['date','email', 'name']
    st.session_state['bands'] = u.read_csv('data/bands.csv', headers)

if 'users' not in st.session_state:
    headers = ['date','email', 'name', 'surnames', 'birthdate', 'address', 'city', 'gender']
    st.session_state['users'] = u.read_csv('data/users.csv', headers)

if 'calendars' not in st.session_state:
    st.session_state['calendars'] = {}
    for sala in range(st.session_state['n_salas']):
        st.session_state['calendars'][sala] = u.Calendar(st.session_state['now'].year,
                                                       st.session_state['now'].month,
                                                       sala)


app()