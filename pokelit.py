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
    cursor = collection.find({})
    for document in cursor:
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
     ('List Cards', 'Add/Update Card', 'Delete Card'))
    
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

if option== 'Add/Update Card' or option=='Delete Card':
    st.header('Card Info:')
    col1, col2, col3  = st.columns(3)
    
    with col1:
        d1 = st.text_input(
            "User")
    with col2:
        d2 = st.text_input(
            "Card Name")
    if option== 'Add/Update Card':
        with col3:
            d3 = st.number_input(
                "Quantity", step=1)

if st.button('Submit'):
    if option== 'List Cards':
        list_db_items(db.myCollectibles)
    elif option =="Add/Update Card":
        if db.myCollectibles.find_one({
            'ownerId':d1,
            'itemName':d2
            }) ==None:
                db.myCollectibles.insert_one({
                    'ownerId':d1,
                    'itemName':d2,
                    'quantity': d3
                }) 

        else:
            db.myCollectibles.update_one({
                    'ownerId':d1,
                        'itemName':d2,
                    },{
                    '$set': {
                        'quantity': d3
                    }
                    }, upsert=False)
        st.write("Added " , d3," ",d2, " to ", d1)
    else:
        test_item={'ownerId': d1,
        'itemName': }
        post_request = requests.post(url, json = test_item, headers = headers)
        # db.myCollectibles.delete_one({
        #     'ownerId':d1,
        #     'itemName':d2,
        # })
        # st.write("Deleted " ," ",d2, " from ", d1)
                
                




# with coll1:
#     if st.button('Add'):
#         st.write('Searching')
# # with coll2:
# if st.button('List Cards'):
#     list_db_items(db.myCollectibles)
# with coll3:
#     if st.button('Delete Card'):
#         st.write('Searching')