import streamlit as st

def summary_card_styling():
    st.markdown(
    """
    <style>
    .custom-caption.custom {
        margin-top: -10px;
        display: inline;
        color: #7A7A7A;
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
    unsafe_allow_html=True
)
    
def hide_streamlit_menu():
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

def multi_select_styling():
    st.markdown(
    """
    <style>
    /* Change the background color of the dropdown list */
    div[role="listbox"] {
        background-color: #2E4053 !important;
    }

    /* Change the text color of the options */
    div[role="option"] {
        color: #F39C12 !important;
    }

    /* Change the border color and style of the multiselect widget */
    div[role="combobox"] {
        border: 2px solid #FFDC1E !important;
        border-radius: 8px !important;
    }

    /* Change the background color of selected tags */
    span[data-baseweb="tag"] {
        background-color: #F1C40F !important;
        color: #2C3E50 !important;
    }

    /* Change the color of the delete (X) icon in tags */
    span[data-baseweb="tag"] svg {
        fill: #2C3E50 !important;
    }

    /* Change the placeholder text color */
    input[role="combobox"]::placeholder {
        color: #95A5A6 !important;
    }

    /* Change the clear all icon color */
    svg[title="Clear all"] {
        fill: #586776 !important;
    }

    /* Change the open icon color */
    svg[title="open"] {
        fill: #FFDC1E !important;
    }
    </style>
    """,
    unsafe_allow_html=True)