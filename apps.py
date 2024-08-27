import streamlit as st
from streamlit_option_menu import option_menu
from utils import generate_calendar, save_new_reg
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import csv
import os

PAGINAS = {
    'names': ['Reservas','Asistencia'],
    'icons': ['calendar-date','calendar-check']
    }

def main_app():

    reservas = ['2024-08-25']
    
    viewer, app = st.columns([3,7])
    with viewer:
        calendar = generate_calendar(datetime.now().year, datetime.now().month, reservas)
        st.plotly_chart(calendar)
    
    with app:
        pagina = option_menu(
            menu_title=None,
            options=['Añadir','Confirmar','Eliminar'],
            icons=['calendar-plus-fill','calendar-check-fill','calendar-x-fill'],
            orientation='horizontal'
            )
        if pagina == 'Añadir':
            _, form, buttons, _ = st.columns([5,5,1,5])
            with form:
                grupo = st.selectbox(
                    label='Grupo',
                    options=[0,1,2,3,4,5,6,7]
                    )
                date = st.date_input(
                    label='Fecha',
                    min_value=datetime.now(),
                    format='DD/MM/YYYY'
                    )
                start_time = st.time_input(
                    label='Hora de inicio',
                    value=datetime.now() - timedelta(datetime.now().minute),
                    step=30*60
                    )
                duration = st.selectbox(
                    label='Duración de la reserva (horas)',
                    options=range(1,4)
                    )
            
            with buttons:
                if st.button('Save', type='primary'):
                    
                    pass

        nueva_reserva = {
            'email':        'estellalosa@gmail.com',
            'band':         'Wolves and Weapons',
            'start_date':   '2024-08-14',
            'end_date':     '2024-08-14',
            'start_time':   '15:00:00',
            'end_time':     '18:00:00',
            'confirmed':    False,
            'sanctioned':   False
            }

        save_new_reg(nueva_reserva)