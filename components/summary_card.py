import streamlit as st

def summary_card(title, caption, summary_number, difference):
    with st.container(border=True):
        st.subheader(title)
        st.markdown(f'<p class="custom-caption custom">{caption}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="summary_number custom">{summary_number}</p>', unsafe_allow_html=True)
        if 2 < 3:
            st.markdown(f'<p class="less_than custom">➘ -{difference}</p>', unsafe_allow_html=True)