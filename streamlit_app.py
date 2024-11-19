import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
#from data.snowflake_data import get_health_data  # Import the function

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
        font-size: 20px;
        color: #D44B69;
        background: #E0ACB8;
        display: inline; /* Background spans text only */
        padding: 4px 4px; /* Space around text */
        border-radius: 5px; /* Rounded corners */
        margin-top: auto; /* Ensure this element aligns to the bottom */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
def summary_card(title, caption, summary_number, difference):
    with st.container(border=True):
        st.subheader(title)
        st.markdown(f'<p class="custom-caption">{caption}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="summary_number">{summary_number}</p>', unsafe_allow_html=True)
        if 2 < 3:
            st.markdown(f'<p class="less_than">➘ -{difference}</p>', unsafe_allow_html=True)

summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", summary_number = 73, difference = 2)