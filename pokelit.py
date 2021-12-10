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

with header: 
    st.title('Welcome to the Catch them all!')
    # st.text('Please enter your pokemon info:')
option = st.selectbox(
     'What would you like to do?',
     ('---Choose an Option---', 'List Items', 'Add Item','Update Item', 'Delete Item'))
    
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

def collection_from_get_request(user):
    url = "http://127.0.0.1:5000/api/v1/collection/"
    payload = {"Owner":user,"results_per_page":20}
    headers = {"accept": "application/json"}
    get_request_with_owner = requests.get(url, payload, headers = headers)
    json_response = get_request_with_owner.json()
    return json_response

if option == 'List Items':
    user_name_input = st.text_input("User")

if option== 'Add Item' or option=='Delete Item' or option=='Update Item':
    st.header('Item Info:')
    col1, col2, col3  = st.columns(3)
    
    with col1:
        d1 = st.text_input(
            "User")
    with col2:
        d2 = st.text_input(
            "Item Name")
    if option== 'Add Item' or option=='Update Item':
        with col3:
            d3 = st.number_input(
                "Quantity", step=1)

if option != '---Choose an Option---' and st.button('Submit'):
    if option== 'List Items':
        list_db_items(collection_from_get_request(user_name_input))
    elif option =="Add Item":
        test_item={'ownerId': d1,
        'itemName': d2,
        'quantity': d3}
        add_new_item(test_item)
        st.write("Item: ", d2, "added for: ",d1,"!" )
    elif option =="Update Item":
        test_item={'ownerId': d1,
        'itemName': d2,
        'quantity': d3}
        update_item_by_name(test_item)
        st.write("Item", d2, "updated in to: ", str(d3), "in ",d1,"!" )
    else:
        test_item={'ownerId': d1,
        'itemName': d2}
        delete_by_item_name(test_item)
        # post_request = requests.delete(url, json = test_item, headers = headers)
        st.write("Item: ", d2, "deleted for: ",d1,"!"  )