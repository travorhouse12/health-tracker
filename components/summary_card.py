import streamlit as st

def summary_card(title, caption, current_value, previous_value):
    with st.container(border=True):
        st.subheader(title)
        st.markdown(f'<p class="custom-caption custom">{caption}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="summary_number custom">{current_value}</p>', unsafe_allow_html=True)
        if current_value < previous_value:
            st.markdown(f'<p class="less_than custom">➘ {current_value - previous_value}</p>', unsafe_allow_html=True)
        elif current_value == previous_value:
            st.markdown(f'<p class="greater_than_or_equal_to custom">{current_value - previous_value}</p>', unsafe_allow_html=True)
        elif current_value > previous_value:
            st.markdown(f'<p class="greater_than_or_equal_to custom">➚ {current_value - previous_value}</p>', unsafe_allow_html=True)