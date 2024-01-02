from datetime import datetime as dt
import streamlit as st


def christmas_festive_animation():
    """ Display snowflakes animaton during Christmas festive season. """
    
    current_year = dt.now().date()
    previous_year = dt.today().year - 1
    current_festive_date = dt(year=previous_year, month=12, day=20).date()
    date_diff = current_year - current_festive_date

    if (date_diff.days >= 0) and (date_diff.days <= 21):
        with open('static/css/styles.css') as stylesheet:
            st.markdown(f'<style>{stylesheet.read()}</style>', unsafe_allow_html=True)
        
        return st.snow()
