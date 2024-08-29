import streamlit as st
import plotly.express as px
# import calendar
from calendar import monthrange
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import csv
import os
import numpy as np

def create_calendar(year, month, sala):

    indexes = []
    for i in range(48):
        index = f'{(datetime(year, month,1,0,0,0) + timedelta(minutes=i*30)).time().strftime("%H:%M")}'
        index += f' - {(datetime(year, month,1,0,0,0) + timedelta(minutes=(i+1)*30)).time().strftime("%H:%M")}'
        indexes.append(index)

    n_days = monthrange(year, month)[1]
    calendar = pd.DataFrame(np.zeros((48, n_days)))
    calendar.index = indexes
    calendar.columns = range(1, n_days+1)

    reservas = st.session_state['reservas'].copy()
    reservas['start_date'] = pd.to_datetime(reservas['start_date'], format='%Y-%m-%d')
    reservas = reservas[reservas['start_date'] > datetime(st.session_state['now'].year, st.session_state['now'].month, 1)]
    reservas = reservas[reservas['start_date'] <= datetime(st.session_state['now'].year, st.session_state['now'].month, n_days)]

    myscale = [[0, 'rgba(0,0,0,0)'],[1, 'rgba(255, 75, 75, 1)']]

    fig = px.imshow(
        calendar,
        color_continuous_midpoint=.5,
        color_continuous_scale=myscale
        )
    fig.update_layout(
        coloraxis_showscale=False,
        title={
            'text':     datetime(year, month, 1).strftime("%B, %Y"),
            'x':        0.5,
            'xanchor':  'center',
            'yanchor':  'top'
            },
        xaxis_title = 'Día',
        yaxis_title = 'Franja',
        width=1700,
        height=700)
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(tickmode='linear', showgrid=False)

    grupos = st.session_state['bands']

    return fig


def save_new_reg(new_record):
    file_path = 'data/events.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['email', 'band', 'start_date', 'end_date','start_time','end_time','confirmed','sanctioned','sala']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_record)


def save_new_band(new_band):
    file_path = 'data/bands.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['date','email', 'name']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_band)


def save_new_user(new_user):
    file_path = 'data/users.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['date','email', 'name', 'surnames', 'birthdate', 'address', 'city', 'gender']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_user)


def save_new_link(new_link):
    file_path = 'data/links.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['date','user_email', 'band_email']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_link)