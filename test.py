import streamlit as st
from data.oura import get_sleep_data

sleep_df = get_sleep_data()

st.dataframe(sleep_df)