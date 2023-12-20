from features.person.faces.expressions import facial_expression as fe
from features.fashion.accessories import add_ons
from features.fashion.clothing import clothes, hats
from features.fashion.hairstyles import beard, hair
from features.person.complexion import skins
from features.person.faces import face
from avatar.avatar import random_avatar, custom_avatar, IMAGE_FILE
from images.image import download_avatar
import streamlit as st


# webpage configuration
st.set_page_config(page_title='Persona', page_icon=':busts_in_silhouette:', layout='centered')


def main():
    """ This is the main function that uses streamlit to create a dynamic web page. """

    # navigation tabs
    tabs = st.tabs(['Beard & Hair', 'Facial features', 'Fashion trends', 'Color', 'Background style'])
    
    st.divider()

    # "Generate random avatar" & "Download button" buttons column
    cols_btn = st.columns([6, 6])
    
    with cols_btn[1]:
        download_avatar(IMAGE_FILE)     # display download button by default

    
    if cols_btn[0].button('Generate random avatar', use_container_width=True):
        features_indices = random_avatar()
    

    with tabs[0]:
        st.caption('Add beard, hairstyle or hair cut')
        avatar_hair = st.selectbox(
            label=':haircut: Hair',
            options=hair.HAIR_STYLES, 
            index=features_indices["hair"] if features_indices else 0,
        )
        avatar_beard = st.selectbox(
            label=':bearded_person: Beard',
            options=beard.BEARD,
            index=features_indices["beard"] if features_indices else 0,
        )

    with tabs[1]:
        st.caption('Add eyes or facial expression.')
        avatar_eyes = st.selectbox(
            label=':eyes: Eyes',
            options=face.EYES,
            index=features_indices["eyes"] if features_indices else 0,
        )
        avatar_facial_expr = st.selectbox(
            label=':smiley: Facial expression',
            options=fe.FACIAL_EXPRESSIONS,
            index=features_indices["face_expression"] if features_indices else 0,
        )
        avatar_mouth = st.selectbox(
            label=':lips: Mouth',
            options=fe.FACIAL_EXPRESSIONS_MOUTH,
            index=features_indices["mouth"] if features_indices else 0,
        )

    with tabs[2]:
        st.caption("What are your favorite fashion trends?")
        tabs_cols = st.columns([6, 6])

        avatar_addons = tabs_cols[0].selectbox(
            label=':sunglasses: Accessories',
            options=add_ons.FASHION_ACCESSORIES,
            index=features_indices["accessories"] if features_indices else 0,
            )
        avatar_clothe = tabs_cols[0].selectbox(
            label=':tshirt: Clothes',
            options=clothes.CLOTHES_CATEGORIES,
            index=features_indices["clothing"] if features_indices else 0,   
        )
        avatar_clothe_pattern = tabs_cols[1].selectbox(
            label=':art: Clothe pattern',
            options=clothes.CLOTHES_GRAPHICS,
            index=features_indices["clothes_art"] if features_indices else 0,
        )
        avatar_hat = tabs_cols[1].selectbox(
            label=':face_with_cowboy_hat: Headwear',
            options=hats.HEADWEAR,
            index=features_indices["headwear"] if features_indices else 0,
        )
    
    with tabs[3]:
        st.caption('Play with colors')
        tabs_cols = st.columns([6, 6])

        avatar_skin_color = st.selectbox(
            label='Skin complexion',
            options=skins.SKIN_COLOR,
            index=features_indices["skin"] if features_indices else 0,
        )
        avatar_hair_color = tabs_cols[0].selectbox(
            label='Dye/Hair color',
            options=hair.HAIR_COLOR,
            index=features_indices["hair_color"] if features_indices else 0,
        )
        avatar_beard_color = tabs_cols[0].selectbox(
            label='Beard color',
            options=beard.BEARD_COLOR,
            index=features_indices["beard_color"] if features_indices else 0,    
        )
        avatar_clothes_color = tabs_cols[1].selectbox(
            label='Clothes color',
            options=clothes.CLOTHES_COLOR,
            index=features_indices["clothes_color"] if features_indices else 0,    
        )
        avatar_hat_color = tabs_cols[1].selectbox(
            label='Hat color',
            options=hats.HAT_COLOR,
            index=features_indices["hat_color"] if features_indices else 0,
        )
    
    with tabs[4]:
        st.caption('Add or remove background color in your avatar')
        avatar_bg = st.selectbox(
            label='Background',
            options=('CIRCLE', 'TRANSPARENT'),
            index=features_indices["background"] if features_indices else 0,
        )

    # selected avatar features
    avatar_features = {
        'accessories': avatar_addons,
        'bg': avatar_bg,
        'beard': avatar_beard,
        'beard_color': avatar_beard_color,
        'clothing': avatar_clothe,
        'clothes_color': avatar_clothes_color,
        'clothes_art': avatar_clothe_pattern,
        'eyes': avatar_eyes,
        'face_expression': avatar_facial_expr,
        'hair_and_headwear': avatar_hair if avatar_hair != 'NO_HAIR' else avatar_hat,   # display a hat if avatar_hair is "NO_HAIR"
        'hair_color': avatar_hair_color,
        'hat_color': avatar_hat_color,
        'mouth': avatar_mouth,
        'skin': avatar_skin_color,
    }
    
    return custom_avatar(avatar_features)


if __name__ == "__main__":
    main()
