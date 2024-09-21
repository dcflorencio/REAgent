import streamlit as st
import folium
from geopy.geocoders import Nominatim
import re
import pandas as pd
from streamlit_folium import st_folium
import matplotlib.pyplot as plt


# Function to extract properties from markdown content
def extract_properties_fixed(report_content):
    pattern = r"- \*\*Address\*\*: (.*?), Seattle, WA (\d+)\n- \*\*Price\*\*: \$([\d,]+)"
    matches = re.findall(pattern, report_content)
    properties = []
    for match in matches:
        address = match[0].strip() + ", Seattle, WA " + match[1]
        price = int(match[2].replace(',', ''))
        properties.append({'address': address, 'price': price})
    return pd.DataFrame(properties)


# Function to geocode addresses into latitude and longitude
def geocode_address(address):
    geolocator = Nominatim(user_agent="streamlit_app")
    location = geolocator.geocode(address, timeout=1000)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


# Function to plot properties on a folium map
def plot_properties_on_map(properties_df):
    if properties_df.empty:
        return None
    properties_df[['latitude', 'longitude']] = properties_df['address'].apply(
        lambda loc: pd.Series(geocode_address(loc)))
    properties_df = properties_df.dropna(subset=['latitude', 'longitude'])

    m = folium.Map(location=[47.6062, -122.3321], zoom_start=12)  # Seattle coordinates
    for _, row in properties_df.iterrows():
        location = (row['latitude'], row['longitude'])
        price = row['price']
        size = price / 500  # Adjust marker size based on price
        folium.CircleMarker(
            location=location,
            radius=size,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"Price: ${row['price']}"
        ).add_to(m)
    return m


# Streamlit app layout
st.title("Seattle Rental Property Visualizer")

# Upload the markdown report
uploaded_file = st.file_uploader("Upload the property markdown file", type=["md"])

if uploaded_file:
    # Read the uploaded markdown file content
    report_content = uploaded_file.read().decode("utf-8")

    # Extract properties
    properties_df = extract_properties_fixed(report_content)

    if not properties_df.empty:
        st.write("Extracted Properties:")
        st.write(properties_df)

        # Plot the properties on the map
        folium_map = plot_properties_on_map(properties_df)
        if folium_map:
            st.write("Map of Properties:")
            st_folium(folium_map, width=700, height=500)
        else:
            st.error("Failed to plot properties on the map.")

        # Visualization 1: Price Distribution
        st.write("### Price Distribution")
        fig, ax = plt.subplots()
        ax.hist(properties_df['price'], bins=10, color='skyblue')
        ax.set_xlabel("Price ($)")
        ax.set_ylabel("Number of Properties")
        st.pyplot(fig)

        # Visualization 2: Scatter Plot of Price vs Index (proxy for order)
        st.write("### Price Comparison Across Listings")
        fig2, ax2 = plt.subplots()
        ax2.scatter(properties_df.index, properties_df['price'], color='green')
        ax2.set_xlabel("Property Index")
        ax2.set_ylabel("Price ($)")
        st.pyplot(fig2)
    else:
        st.error("No properties found in the uploaded markdown file.")
