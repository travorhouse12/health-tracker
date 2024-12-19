import streamlit as st

def summary_card(title, caption, current_value, previous_value, information):
    difference = current_value - previous_value
    if difference < 0:
        diff_class = "less_than"
        arrow = "➘"
    elif difference == 0:
        diff_class = "greater_than_or_equal_to"
        arrow = ""
    else:
        diff_class = "greater_than_or_equal_to"
        arrow = "➚"
        
    with st.container():
        st.subheader(title, help=information)
        st.markdown(f'<p class="custom-caption custom">{caption}</p>', unsafe_allow_html=True)
        # Combine the current value and difference into a single line using flex display
        st.markdown(
            f'''
            <div style="display: flex; align-items: flex-end;">
                <p class="summary_number custom" style="margin-bottom:0px;">{current_value}</p>
                <p class="{diff_class} custom" style="margin-left: 10px; margin-bottom: 22px;">{arrow} {difference}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
