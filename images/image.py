import streamlit as st


def update_avatar_image(img):
    """ This is a function that displays the generated avatar. """

    img_col = st.columns([.4, .5, .4])
    img_col[1].image(img, caption='Your avatar', use_column_width='auto')   # wrap the image in the center column
    
    return img

def download_avatar(avatar_image):
    """ This function allows one to download their avatars."""

    with open(avatar_image, 'rb') as file:
        st.download_button(
            label='Download avatar',
            type="primary",
            data=file,
            file_name=avatar_image,
            use_container_width=True
        )
    