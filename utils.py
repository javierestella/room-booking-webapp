import streamlit as st
import plotly.express as px
import calendar
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import csv
import os

def generate_calendar(year, month, reservas):

    cal = calendar.Calendar(0)
    month_days = cal.monthdayscalendar(year, month)

    for i_week in range(len(month_days)):
        week = month_days[i_week]

        for i_day in range(len(week)):
            day = week[i_day]
            date = f'{year}-{month:02d}-{day:02d}'
            month_days[i_week][i_day] = (day, 'black' if date not in reservas else '#ff4b4b')

    fig = go.Figure(
        data=go.Table(
            header=dict(
                values=['LUN','MAR','MIE','JUE','VIE','SAB','DOM'],
                align='center'
                ),
            cells=dict(
                values=pd.DataFrame([[d[0] if d[0]!=0 else '' for d in w] for w in month_days]).T,
                fill_color=pd.DataFrame([[d[1] for d in w] for w in month_days]).T,
                align='center',
                height=40
                )
            )
        )
    fig.update_layout(
    title={
        'text': datetime(year,month,1).strftime("%B, %Y"),
        'x': 0.5,  # Alineación horizontal (0.5 para centrado)
        'xanchor': 'center',  # Anclaje horizontal del título
        'yanchor': 'top'  # Anclaje vertical del título
    },
    xaxis_title="Eje X",
    yaxis_title="Eje Y"
    )
    return fig


def save_new_reg(new_record):
    file_path = 'data/events.csv'

    file_exists = os.path.isfile(file_path)
    fieldnames = ['email', 'band', 'start_date', 'end_date','start_time','end_time','confirmed','sanctioned']

    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(new_record)