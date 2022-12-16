import streamlit as st
import requests


api_key = "xkd5fRXbsXBanTKnYxYpIXic4nS0uxndHz1HoPBS"

url = "https://api.nasa.gov/planetary/apod?api_key=xkd5fRXbsXBanTKnYxYpIXic4nS0uxndHz1HoPBS"

# Get the request data as dictionary
request = requests.get(url)
content = request.json()

# Download the file image
image_filepath = "img.png"
content2 = requests.get(content['url'])
with open(image_filepath, 'wb') as file:
    file.write(content2.content)

st.header(content['title'])
st.image(image_filepath)
st.write(content['explanation'])
