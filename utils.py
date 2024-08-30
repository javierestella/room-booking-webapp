import streamlit as st
import plotly.express as px
from calendar import monthrange
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import csv
import os
import numpy as np


class Calendar:
    def __init__(self, year, month, sala):
        index = self.get_gaps()
        self.year = year
        self.month = month
        self.sala = sala

        n_days = monthrange(year, month)[1]
        self.calendar = pd.DataFrame(np.zeros((len(index), n_days)))
        self.calendar.index = index
        self.calendar.columns = range(1, n_days + 1)
        self.import_bookings()
    

    def get_gaps(self):
        indexes = []
        n_gaps = 48
        for i in range(n_gaps):
            p = 60*24/n_gaps
            index = f'{(datetime(2000, 1,1,0,0,0) + timedelta(minutes=i*p)).time().strftime("%H:%M")}'
            index += f' - {(datetime(2000,1,1,0,0,0) + timedelta(minutes=(i+1)*p)).time().strftime("%H:%M")}'
            indexes.append(index)

        return indexes


    def import_bookings(self):
        reservas = st.session_state['reservas'].copy()
        for r in range(reservas.shape[0]):
            if reservas['sala'][r] == self.sala:
                self.add_booking(reservas.iloc[r])


    def add_booking(self, booking):
        date = pd.to_datetime(booking['start_date'], format='%d/%m/%Y')
        time = pd.to_datetime(booking['start_time'], format='%H:%M')
        date_time = datetime(date.year, date.month, date.day, time.hour, time.minute)

        for m in range(booking['duration']*2):
            a = date_time + timedelta(minutes=m*30)
            b = date_time + timedelta(minutes=(m+1)*30)
            gap = a.time().strftime('%H:%M') + ' - ' + b.time().strftime('%H:%M')

            self.calendar.loc[gap, a.day] = 1


    def show(self):
        myscale = [[0, 'rgba(0,0,0,0)'], [1, 'rgba(255, 75, 75, 1)']]
        fig = px.imshow(
            self.calendar,
            color_continuous_midpoint=.5,
            color_continuous_scale=myscale
            )
        fig.update_layout(
            coloraxis_showscale=False,
            title={
                'text':     datetime(self.year, self.month, 1).strftime("%B, %Y"),
                'x':        0.5,
                'xanchor':  'center',
                'yanchor':  'top'
                },
            xaxis_title = 'Día',
            yaxis_title = 'Franja',
            width=1700,
            height=700
            )
        fig.update_yaxes(showgrid=False)
        fig.update_xaxes(tickmode='linear', showgrid=False)
        st.plotly_chart(fig)







# def create_calendar(year, month, n_salas):



#     reservas = st.session_state['reservas'].copy()
#     reservas['start_date'] = pd.to_datetime(reservas['start_date'], format='%Y-%m-%d')
#     reservas = reservas[reservas['start_date'] > datetime(st.session_state['now'].year, st.session_state['now'].month, 1)]
#     reservas = reservas[reservas['start_date'] <= datetime(st.session_state['now'].year, st.session_state['now'].month, n_days)]
#     myscale = [[0, 'rgba(0,0,0,0)'], [1, 'rgba(255, 75, 75, 1)']]

#     fig = px.imshow(
#         calendar,
#         color_continuous_midpoint=.5,
#         color_continuous_scale=myscale
#         )
#     fig.update_layout(
#         coloraxis_showscale=False,
#         title={
#             'text':     datetime(year, month, 1).strftime("%B, %Y"),
#             'x':        0.5,
#             'xanchor':  'center',
#             'yanchor':  'top'
#             },
#         xaxis_title = 'Día',
#         yaxis_title = 'Franja',
#         width=1700,
#         height=700)
#     fig.update_yaxes(showgrid=False)
#     fig.update_xaxes(tickmode='linear', showgrid=False)

#     calendars = []
#     for sala in reservas['sala'].unique():

        
#         reservas[reservas['sala'] == sala]

#     grupos = st.session_state['bands']

#     return fig


def save_new_reg(new_record):
    file_path = 'data/events.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['email', 'band', 'start_date','start_time','duration','confirmed','sanctioned','sala']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_record)
    st.session_state['reservas'] = pd.read_csv('data/events.csv')


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