import streamlit as st
import requests

st.set_page_config(page_title="RestroSearch - phiUture", page_icon="favicon_32.png")

API_URL = "http://localhost:5000/search"

def search_restaurants(latitude, longitude, radius, cuisine_type, min_rating):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "radius": radius,
        "cuisine_type": cuisine_type,
        "min_rating": min_rating
    }
    response = requests.get(API_URL, params=params)
    return response.json()

st.title("Restaurant Search")

latitude = st.number_input("Enter Latitude:")
longitude = st.number_input("Enter Longitude:")
radius = st.number_input("Enter Radius (in meters):")
cuisine_type = st.text_input("Enter Cuisine Type:")
min_rating = st.number_input("Enter Minimum Rating:", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Search"):
    if latitude and longitude and radius:
        restaurants = search_restaurants(latitude, longitude, radius, cuisine_type, min_rating)
        if restaurants:
            st.write("Search Results:")
            for restaurant in restaurants:
                st.write(f"- {restaurant['name']}, Rating: {restaurant['rating']}")
        else:
            st.write("No restaurants found.")
