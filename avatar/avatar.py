from features.person.faces.expressions import facial_expression
from features.fashion.accessories import add_ons
from features.fashion.clothing import clothes, hats
from features.fashion.hairstyles import beard, hair
from features.person.complexion import skins
from features.person.faces import face
from images.image import update_avatar_image
from random import randrange
import py_avataaars as pa
from PIL import Image
import streamlit as st


IMAGE_FILE = 'static/img/avatar.png'


def random_avatar():
    """ This is a function that automatically generates an avatar using random avatar features. """

    features = {
        'accessories': randrange(0, len(add_ons.FASHION_ACCESSORIES)),
        'background': randrange(0, len(['CIRCLE', 'TRANSPARENT'])),
        'beard': randrange(0, len(beard.BEARD)),
        'beard_color': randrange(0, len(beard.BEARD_COLOR)),
        'clothing': randrange(0, len(clothes.CLOTHES_CATEGORIES)),
        'clothes_color': randrange(0, len(clothes.CLOTHES_COLOR)),
        'clothes_art': randrange(0, len(clothes.CLOTHES_GRAPHICS)),
        'eyes': randrange(0, len(face.EYES)),
        'face_expression': randrange(0, len(facial_expression.FACIAL_EXPRESSIONS)),
        'hair': randrange(0, len(hair.HAIR_STYLES)),
        'headwear': randrange(0, len(hats.HEADWEAR)),
        'hair_and_headwear': randrange(0, len(hair.HAIR_STYLES + hats.HEADWEAR)),
        'hair_color': randrange(0, len(hair.HAIR_COLOR)),
        'hat_color': randrange(0, len(hats.HAT_COLOR)),
        'mouth': randrange(0, len(facial_expression.FACIAL_EXPRESSIONS_MOUTH)),
        'skin': randrange(0, len(skins.SKIN_COLOR)),
    }

    return features


def custom_avatar(features):
    """ This is a function that generates an avatar depending on the user's input. """

    avatar = pa.PyAvataaar(
        accessories_type=eval(f'pa.AccessoriesType.{features["accessories"]}'),
        clothe_type=eval(f'pa.ClotheType.{features["clothing"]}'),
        clothe_color=eval(f'pa.Color.{features["clothes_color"]}'),
        clothe_graphic_type=eval(f'pa.ClotheGraphicType.{features["clothes_art"]}'),
        eye_type=eval(f'pa.EyesType.{features["eyes"]}'),
        eyebrow_type=eval(f'pa.EyebrowType.{features["face_expression"]}'),
        hair_color=eval(f'pa.HairColor.{features["hair_color"]}'),
        hat_color=eval(f'pa.Color.{features["hat_color"]}'),
        facial_hair_type=eval(f'pa.FacialHairType.{features["beard"]}'),
        facial_hair_color=eval(f'pa.HairColor.{features["beard_color"]}'),
        mouth_type=eval(f'pa.MouthType.{features["mouth"]}'),
        skin_color=eval(f'pa.SkinColor.{features["skin"]}'),
        style=eval(f'pa.AvatarStyle.{features["bg"]}'),
        top_type=eval(f'pa.TopType.SHORT_HAIR_SHORT_FLAT.{features["hair_and_headwear"]}'),

    )

    render_img = avatar.render_png_file(IMAGE_FILE)
    image = Image.open(IMAGE_FILE)

    return update_avatar_image(image)
