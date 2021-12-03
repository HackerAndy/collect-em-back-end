import streamlit as st
import requests as req
import json
from PIL import Image
import requests
from io import BytesIO
from streamlit.legacy_caching.caching import _hash_func
from streamlit.type_util import Key
from pagination import paginator
from datetime import date
import base64
st.set_page_config(layout="wide")
f = open('pokemon.json')
pokedata = json.load(f)
f.close()



LOGO_IMAGE = "pokeball.jpg"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}" width="150" height="150">
        <p class="logo-text">Catch Em All!</p>
    </div>
    """,
    unsafe_allow_html=True
)

header = st.container() 
dataset= st.container()
features = st.container()
model_training= st.container()
col1, col2, col3  = st.columns(3)
flight_list=st.container()

# st.write("a logo and text next to eachother")
# col21, mid, col22 = st.beta_columns([1,1,20])
# with col21:
#     st.image('pokeball.jpg', width=60)
# with col22:
#     st.write('A Name')

with header: 
    st.title('Welcome to the Catch them all!')
    st.text('Please enter your pokemon info:')
    
with dataset:
    st.text_input(
            "Add Deck")
    st.header('Pokemon Info:')
    with col1:
        d2 = st.text_input(
            "Name")
    with col2:
        d2 = st.text_input(
            "Add Type")

    with col3:
        d3 = st.text_input(
            "Add Amount")

    # with col3:
    #     d3 = st.text_input(
    #         "To",
    #         value="Anywhere")
            
    # with col4:
    #     d4 = st.text_input(
    #         "To",
    #         value="Anywhere")

if st.button('Add'):
    st.write('Searching')
# url = pokedata[24]['image']+'/low'
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")

# pokelist=[]
# for i in range(10):
#     if "image" in pokedata[20+i]:
#         image_url= pokedata[20+i]['image']
#         response = requests.get(image_url)
#         pokelist.append(Image.open(BytesIO(response.content)))
#     else:
#         pass

# st.image(pokelist)
# image_iterator = paginator("Select a sunset page", pokelist)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=100, caption=indices_on_page)
# for i in range(pokelist):
#         st.markdown("""---""")
#         cols = st.columns(3)
#         # cols[0].write(pokedata[20+i]['name'])
#         cols[0].write(st.image(img),Key=i)
        # cols[0].write(st.checkbox('I agree'),   Key=i)
# st.write(url)
# st.image(img)
# if st.button(st.image(img)):
#     st.write('Its Lit')
# img = Image.open("local-filename.jpg")
# st.button(st.image(img))
# st.image(
#     url,
#     # width=400, # Manually Adjust the width of the image as per requirement
# )