import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if filtered_data is None:
        st.error(f"No data found for {place}. Please check the city name and try again.")
    else:
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]  # Convert to Celsius
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      # Note: API returns "Clouds" not "Cloud"
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            # Handle missing weather conditions
            image_paths = []
            for condition in sky_conditions:
                if condition in images:
                    image_paths.append(images[condition])
                else:
                    # Use a default image or handle missing condition
                    st.write(f"Unknown weather condition: {condition}")
                    # Optionally use a default image
                    # image_paths.append("images/default.png")

            if image_paths:
                st.image(image_paths, width=115)