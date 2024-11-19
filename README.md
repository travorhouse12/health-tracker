import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from transformation.data import process_appointments_data  # Import the function

st.set_page_config(
    page_title="Daily Set Goals",
    layout="wide"
)

st.logo("https://i.ibb.co/5R9N3Bs/DAILY-SET-GOALS.png", size="large")

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