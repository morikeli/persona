import streamlit as st


def download_avatar(avatar_image):
    """ This function allows one to download their avatars. """
    
    with open(avatar_image, 'rb') as image_file:
        st.download_button(
            label='Download avatar',
            type="primary",
            data=image_file,
            file_name=avatar_image,
            use_container_width=True
        )
    
    return image_file