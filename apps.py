import streamlit as st
from streamlit_option_menu import option_menu
import utils as u 
from datetime import datetime, timedelta
from calendar import monthrange
import numpy as np
import pandas as pd
import plotly.express as px


def app():

    pagina = option_menu(
        menu_title=None,
        options=['Calendar', 'Data', 'Payments'],
        icons=['calendar', 'table', 'money'],
        orientation='horizontal'
        )
    
    if pagina == 'Calendar':

        subpagina = option_menu(
            menu_title=None,
            options=['Visor','Añadir','Confirmar','Eliminar'],
            icons=['calendar','calendar-plus-fill','calendar-check-fill','calendar-x-fill'],
            orientation='horizontal'
            )

        if subpagina == 'Visor':
            st.title('Calendar')

            p, n = st.columns(2)
            with p:
                month_days = monthrange(st.session_state['now'].year, st.session_state['now'].month)[1]
                if p.button('Prev. Month', use_container_width=True):
                    st.session_state['now'] -= timedelta(month_days + 1)
                if n.button('Next. Month', use_container_width=True):
                    st.session_state['now'] += timedelta(month_days - st.session_state['now'].day + 1)

            for sala in range(1, st.session_state['n_salas'] + 1):
                with st.expander(f'Sala {sala}'):
                    calendar = u.Calendar(st.session_state['now'].year, st.session_state['now'].month, sala)
                    calendar.show()


        if subpagina == 'Añadir':
            _, form, _ = st.columns([4,5,4])
            with form:
                grupo = st.selectbox(
                    label='Grupo',
                    options=sorted(st.session_state['bands']['name'].to_list())
                    )
                date = st.date_input(
                    label='Fecha',
                    min_value=datetime.now(),
                    format='DD/MM/YYYY'
                    )
                st.code([date, type(date)])
                start_time = st.time_input(
                    label='Hora de inicio',
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
    'start_date':   f'{np.random.randint(1,30)}/08/2024',   # Habrá que ver el formato en que se obtiene este dato
    'start_time':   f'{np.random.randint(0,23)}:00',        # Lo mismo
    'duration':     np.random.randint(1,3),
    'confirmed':    False,
    'sanctioned':   False,
    'sala':         1
    }

nueva_banda = {
    'date':     datetime.now(),
    'email':    'vicriver94@gmail.com',
    'name':     'Dio Genes'
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

# u.save_new_reg(nueva_reserva)
u.save_new_band(nueva_banda)

# save_new_user(nuevo_usuario)
# save_new_link(nuevo_link)