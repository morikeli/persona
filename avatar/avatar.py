from features.person.faces.expressions import facial_expression
from features.fashion.accessories import add_ons
from features.fashion.clothing import clothes, hats
from features.fashion.hairstyles import beard, hair
from features.person.complexion import skins
from features.person.faces import face
from images.image import update_avatar_image, download_avatar
from random import sample
import py_avataaars as pa
from PIL import Image
import streamlit as st


IMAGE_FILE = 'static/img/avatar.png'


def random_avatar():
    """ This is a function that automatically generates an avatar using random avatar features. """

    features = {
        'accessories': "".join(sample(add_ons.FASHION_ACCESSORIES, k=1)),
        'background': "".join(sample(['CIRCLE', 'TRANSPARENT'], k=1)),
        'beard': "".join(sample(beard.BEARD, k=1)),
        'beard_color': "".join(sample(beard.BEARD_COLOR, k=1)),
        'clothing': "".join(sample(clothes.CLOTHES_CATEGORIES, k=1)),
        'clothes_color': "".join(sample(clothes.CLOTHES_COLOR, k=1)),
        'clothes_art': "".join(sample(clothes.CLOTHES_GRAPHICS, k=1)),
        'eyes': "".join(sample(face.EYES, k=1)),
        'face_expression': "".join(sample(facial_expression.FACIAL_EXPRESSIONS, k=1)),
        'hair_and_headwear': "".join(sample(hair.HAIR_STYLES + hats.HEADWEAR, k=1)),
        'hair_color': "".join(sample(hair.HAIR_COLOR, k=1)),
        'hat_color': "".join(sample(hats.HAT_COLOR, k=1)),
        'mouth': "".join(sample(facial_expression.FACIAL_EXPRESSIONS_MOUTH, k=1)),
        'skin': "".join(sample(skins.SKIN_COLOR, k=1)),
    }

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
        style=eval(f'pa.AvatarStyle.{features["background"]}'),
        top_type=eval(f'pa.TopType.SHORT_HAIR_SHORT_FLAT.{features["hair_and_headwear"]}'),

    )

    render_img = avatar.render_png_file(IMAGE_FILE)
    image = Image.open(IMAGE_FILE)

    return update_avatar_image(image)


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
