import streamlit as st
import requests as req
import json
import requests
from PIL import Image
import requests
from io import BytesIO
from streamlit.legacy_caching.caching import _hash_func
from streamlit.type_util import Key
from pagination import paginator
from datetime import date
import base64
from pymongo import MongoClient
import json
import os
from datetime import datetime
import pytz
import sys

st.set_page_config(layout="wide")
MONGO_URI = "mongodb://127.0.0.1:27017/BasementOfHolding?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client.get_default_database()  

url = "http://127.0.0.1:5000/api/v1/item/"
headers = {"accept": "application/json",
    "Content-Type": "application/json"}

def list_db_items(collection):
    for document in collection['response_body']:
        st.markdown("""---""")
        cols = st.columns(3)
        cols[0].write(document['ownerId'])
        cols[1].write(document['itemName'])
        cols[2].write(document['quantity'])
        
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

features = st.container()
model_training= st.container()
dataset= st.container()


# st.write("a logo and text next to eachother")
# col21, mid, col22 = st.beta_columns([1,1,20])
# with col21:
#     st.image('pokeball.jpg', width=60)
# with col22:
#     st.write('A Name')

with header: 
    st.title('Welcome to the Catch them all!')
    # st.text('Please enter your pokemon info:')
option = st.selectbox(
     'What would you like to do?',
     ('List Cards', 'Add Card','Update Card', 'Delete Card'))
    
# with dataset:
#     st.header('Card Info:')
#     with col1:
#         d1 = st.text_input(
#             "Deck")
#     with col2:
#         d2 = st.text_input(
#             "Card Name")

#     with col3:
#         d3 = st.text_input(
#             "Quantity")

# option = st.selectbox(
#      'What would you like to do?',
#      ('List Cards', 'Add/Update Card', 'Delete Card'))

def delete_by_item_name(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/delete"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.delete(url, json = test_item, headers = headers)  
    return post_request

def add_new_item(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.post(url, json = test_item, headers = headers)  
    return post_request

def update_item_by_name(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/update"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.patch(url, json = test_item, headers = headers)  
    return post_request

def collection_from_get_request():
    url = "http://127.0.0.1:5000/api/v1/collection/"
    payload = {"Owner":"Ash","results_per_page":20}
    headers = {"accept": "application/json"}
    get_request_with_owner = requests.get(url, payload, headers = headers)
    json_response = get_request_with_owner.json()
    return json_response


if option== 'Add Card' or option=='Delete Card' or option=='Update Card':
    st.header('Card Info:')
    col1, col2, col3  = st.columns(3)
    
    with col1:
        d1 = st.text_input(
            "User")
    with col2:
        d2 = st.text_input(
            "Card Name")
    if option== 'Add Card' or option=='Update Card':
        with col3:
            d3 = st.number_input(
                "Quantity", step=1)

if st.button('Submit'):
    if option== 'List Cards':
        list_db_items(collection_from_get_request())
    elif option =="Add Card":
        test_item={'ownerId': d1,
        'itemName': d2,
        'quantity': d3}
        add_new_item(test_item)
        st.write("Card", d2, "added in ",d1,"!" )
    elif option =="Update Card":
        test_item={'ownerId': d1,
        'itemName': d2,
        'quantity': d3}
        update_item_by_name(test_item)
        st.write("Card", d2, "updated in to", str(d3), "in ",d1,"!" )
    else:
        test_item={'ownerId': d1,
        'itemName': d2}
        delete_by_item_name(test_item)
        # post_request = requests.delete(url, json = test_item, headers = headers)
        st.write("Card", d2, "deleted in",d1,"!"  )