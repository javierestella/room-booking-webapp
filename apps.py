import streamlit as st
from streamlit_option_menu import option_menu
from utils import save_new_reg, save_new_band, save_new_user, save_new_link, create_calendar
from datetime import datetime, timedelta
from calendar import monthrange
import numpy as np
import pandas as pd
import plotly.express as px

def main_app():

    pagina = option_menu(
        menu_title=None,
        options=['Visor','Añadir','Confirmar','Eliminar'],
        icons=['calendar','calendar-plus-fill','calendar-check-fill','calendar-x-fill'],
        orientation='horizontal'
        )
    if pagina == 'Visor':
        st.title('Calendario')

        with st.expander('Sala 1'):
            left,right = st.columns(2)
            if left.button('Mes anterior en Sala 1', use_container_width=True):
                last_days = st.session_state['now'].day + 1
                st.session_state['now'] = st.session_state['now'] - timedelta(last_days)
                st.session_state['calendar'] = create_calendar(st.session_state['now'].year, 
                                                               st.session_state['now'].month, 
                                                               1)

            if right.button('Mes siguiente en Sala 1', use_container_width=True):
                n_days = monthrange(st.session_state['now'].year, st.session_state['now'].month)[1]
                last_days = n_days - st.session_state['now'].day + 1
                st.session_state['now'] = st.session_state['now'] + timedelta(last_days)
                st.session_state['calendar'] = create_calendar(st.session_state['now'].year, 
                                                               st.session_state['now'].month, 
                                                               1)

            st.plotly_chart(st.session_state['calendar'])

        with st.expander('Sala 2'):
            left,right = st.columns(2)
            if left.button('Mes anterior en Sala 2', use_container_width=True):
                last_days = st.session_state['now'].day + 1
                st.session_state['now'] = st.session_state['now'] - timedelta(last_days)
                reservas = st.session_state['reservas']
                reservas = reservas[reservas['sala'] == 2]
                st.session_state['calendar'] = create_calendar(st.session_state['now'].year, st.session_state['now'].month, 2)

            if right.button('Mes siguiente en Sala 2', use_container_width=True):
                n_days = monthrange(st.session_state['now'].year, st.session_state['now'].month)[1]
                last_days = n_days - st.session_state['now'].day + 1
                st.session_state['now'] = st.session_state['now'] + timedelta(last_days)
                reservas = st.session_state['reservas']
                reservas = reservas[reservas['sala'] == 2]
                st.session_state['calendar'] = create_calendar(st.session_state['now'].year, st.session_state['now'].month, 2)

            st.plotly_chart(st.session_state['calendar'])


    if pagina == 'Añadir':
        _, form, _ = st.columns([4,5,4])
        with form:
            grupo = st.selectbox(
                label='Grupo',
                options=st.session_state['bands']['name'].to_list()
                )
            date = st.date_input(
                label='Fecha',
                min_value=datetime.now(),
                format='DD/MM/YYYY'
                )
            start_time = st.time_input(
                label='Hora de inicio',
                # value=datetime.now() + timedelta(minutes= 30 - datetime.now().minute) if datetime.now().minute < 30 else timedelta(minutes= 60 - datetime.now().minute),
                step=30*60
                )
            duration = st.selectbox(
                label='Duración de la reserva (horas)',
                options=range(1,4)
                )
            if st.button('Añadir reserva', type='primary'):

                pass





nueva_reserva = {
    'email':        'membername@gmail.com',
    'band':         'band_name',
    'start_date':   '2024-08-14',
    'end_date':     '2024-08-14',
    'start_time':   '15:00:00',
    'end_time':     '18:00:00',
    'confirmed':    False,
    'sanctioned':   False,
    'sala':         1
    }

nueva_banda = {
    'date':     datetime.now(),
    'email':    'bandemail@gmail.com',
    'name':     'band_name'
    }

nuevo_usuario = {
    'date':     datetime.now(),
    'email':    'membername@gmail.com',
    'name':     'somename', 
    'surnames': 'somesurnames',
    'birthdate':'01/01/1992', 
    'address':  'C/street, 2',
    'city':     'somecity'
}

nuevo_link = {
    'date':         datetime.now(),
    'user_email':   'membername@gmail.com',
    'band_email':   'bandemail@gmail.com'
}

save_new_reg(nueva_reserva)
# save_new_band(nueva_banda)
# save_new_user(nuevo_usuario)
# save_new_link(nuevo_link)