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
    .custom-caption.custom {
        margin-top: -10px
    }
    .summary_number.custom {
        margin-top: -10px;
        font-size: 54px !important;
        padding-right: 10px;
    }
    .less_than.custom {
        background: #301D25;
        display: inline-block;
        font-size: 20px !important;
        color: #D44B69;
        padding: 1px 10px; /* Space around text */
        border-radius: 5px; /* Rounded corners */
        margin-top: -5px; /* Ensure this element aligns to the bottom */
    }
    .greater_than_or_equal_to.custom {
        background: #182E25;
        display: inline-block;
        font-size: 20px !important;
        color: #43C171;
        padding: 1px 10px; /* Space around text */
        border-radius: 5px; /* Rounded corners */
        margin-left: -35px; /* Ensure this element aligns to the bottom */
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


cols1, cols2, cols3 = st.columns([1,1, 1])

with cols1:
    summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", current_value = summary_number, previous_value = yesterday_summary_number)

with cols2:
    summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", current_value = yesterday_summary_number, previous_value = summary_number)

with cols3:
    summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", current_value = 73, previous_value = 73)