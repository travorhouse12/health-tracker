import streamlit as st

def summary_card_styling():
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