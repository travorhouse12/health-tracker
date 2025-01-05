import streamlit as st
import pandas as pd
import numpy as np
import datetime
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from data.snowflake_data import get_health_data
from components.summary_card import summary_card
from components.charts import area_line_chart
from styling.css import summary_card_styling, hide_streamlit_menu

st.set_page_config(
    page_title="Travor's Health Tracker",
    layout="wide"
)

st.logo("https://i.ibb.co/0Gt9DcG/Group-1554-1.png", size="large")

hide_streamlit_menu()

summary_card_styling()

today = datetime.date.today()
first_day_of_month = datetime.date(2024, 10, 1)
last_day_of_month = datetime.date(2024, 10, 31)

with st.sidebar:
    st.divider()
    st.subheader("Filters")
    date_group = st.segmented_control("Group By", ("Day", "Week", "Month"), default= 'Day')
    st.text(" ")
    start_date, end_date = st.date_input("Select Date Range", (first_day_of_month, last_day_of_month))

df = get_health_data()

today = pd.to_datetime('2024-11-04').date()

df_today = df[(df['DAY'] == today) & (df['METRIC_NAME'] == 'activity.score')]

summary_number = df_today['VALUE'].squeeze().astype(int)

yesterday = pd.to_datetime('2024-11-03').date()

df_today = df[(df['DAY'] == yesterday) & (df['METRIC_NAME'] == 'activity.score')]

yesterday_summary_number = df_today['VALUE'].squeeze().astype(int)

difference = yesterday_summary_number - summary_number

cols1, cols2, cols3 = st.columns([1,1,1])

with cols1:
    summary_card(title = "Readiness Score", caption = "Today vs. Yesterday", current_value = summary_number, previous_value = yesterday_summary_number, information = "Test")

with cols2:
    summary_card(title = "Sleep Score", caption = "Today vs. Yesterday", current_value = yesterday_summary_number, previous_value = summary_number, information = "Test")

with cols3:
    summary_card(title = "Activity Score", caption = "Today vs. Yesterday", current_value = 73, previous_value = 73, information = "Test")

df_activity = df[(df["METRIC_NAME"] == 'activity.score') & (df["DAY"] >= start_date)& (df["DAY"] <= end_date)]

df_activity['activity.week'] = pd.to_datetime(df_activity["DAY"]).dt.to_period("W").dt.start_time

df_activity["activity.month"] = (
    pd.to_datetime(df_activity["DAY"]).dt.to_period("M").dt.start_time
)

if date_group == "Day":
    df_activity = (
        df_activity.groupby("DAY")
          .mean(numeric_only=True)
          .round(0)
          .reset_index()
          .rename(columns={"DAY": "date_period"})
    )
elif date_group == "Week":
    df_activity = (
        df_activity.groupby("activity.week")
          .mean(numeric_only=True)
          .round(0)
          .reset_index()
          .rename(columns={"activity.week": "date_period"})
    )
elif date_group == "Month":
    df_activity = (
        df_activity.groupby("activity.month")
          .mean(numeric_only=True)
          .round(0)
          .reset_index()
          .rename(columns={"activity.month": "date_period"})
    )

cols1, cols2 = st.columns([3,1])
with cols1:
    st.header("Comparison")
with cols2:
    st.multiselect("", ("Test1", "Test2"), placeholder="Select Metrics")
with st.container(border=True):
    area_line_chart(df_activity, x_axis="date_period", y_axis="VALUE", color="#FFDC1E")