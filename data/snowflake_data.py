import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

#Function to create a Snowflake session
def create_snowflake_session():
    connection_parameters = {
        "account": st.secrets["snowflake"]["account"],
        "user": st.secrets["snowflake"]["user"],
        "password": st.secrets["snowflake"]["password"],
        "role": st.secrets["snowflake"]["role"],
        "warehouse": st.secrets["snowflake"]["warehouse"],
        "database": st.secrets["snowflake"]["database"],
        "schema": st.secrets["snowflake"]["schema"],
    }
    return Session.builder.configs(connection_parameters).create()

session = create_snowflake_session()


@st.cache_data(show_spinner=False, ttl=600)
def get_health_data():
    health_query = """
        SELECT * FROM presentation.health.stacked_health """
    return session.sql(health_query).to_pandas()