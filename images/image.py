import streamlit as st


def update_avatar_image(img):
    img_col = st.columns([.6, .5, .4])
    img_col[1].image(img, caption='Your avatar', use_column_width='auto')   # wrap the image in the center column
    
    return img