import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from data.snowflake_data import get_health_data
from components.summary_card import summary_card

st.set_page_config(
    page_title="Travor's Health Tracker",
    layout="wide"
)

st.logo("https://i.ibb.co/0Gt9DcG/Group-1554-1.png", size="large")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-10trblm {padding-top: 0px; padding-bottom: 0px;}
    .css-1d391kg {padding-top: 0px !important;}
    
    /* Custom Footer Message */
    footer:after {
        content: 'goodbye'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
        text-align: center;
        font-size: 14px;
        color: #ffffff;
        background-color: #41434A;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add custom CSS to remove margin between components
st.markdown(
    """
    <style>
    .custom-caption {
        margin-top: -16px
    }
    .summary_number {
        margin-top: -20px;
        font-size: 54px;
    }
    .less_than {
        align-self: flex-end; /* Push the element to the bottom */
        font-size: 25px;
        color: #D44B69;
        padding: 4px 4px; /* Space around text */
        border-radius: 5px; /* Rounded corners */
        margin-top: -35px; /* Ensure this element aligns to the bottom */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

df = get_health_data()

today = pd.to_datetime('2024-11-04').date()

df_today = df[(df['DAY'] == today) & (df['METRIC_NAME'] == 'activity.score')]

summary_number = df_today['VALUE'].squeeze().astype(int)

yesterday = pd.to_datetime('2024-11-03').date()

df_today = df[(df['DAY'] == yesterday) & (df['METRIC_NAME'] == 'activity.score')]

yesterday_summary_number = df_today['VALUE'].squeeze().astype(int)

difference = yesterday_summary_number - summary_number

st.dataframe(df_today)

summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", summary_number = summary_number, difference = difference)