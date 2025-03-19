import requests
import streamlit as st

def extract_api(city):
    API_KEY = "59ece2c5f1bd2e50155f31336874c791"
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(API_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()

        if response.status_code == 200:
            general = data["weather"][0]["main"]
            icon_id = data["weather"][0]["icon"]
            humidity = data["main"]["humidity"]
            temp = round(data["main"]["temp"])
            wind = data["wind"]["speed"]
            icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            return general, icon, temp, wind, humidity
        else:
            st.error(f"Error: {data.get('message', 'City not found')}")
            return None
    except Exception as e:
        st.error("An error occurred while fetching the data.")
        return None

def main():
    st.title("🌤️ Weather App")
    city = st.text_input(label="Enter the city").strip().lower()

    if st.button("Search"):
        weather_data = extract_api(city)

        if weather_data:
            general, icon, temp, wind, humidity = weather_data
            st.write("___________________________________________________")

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"🌍 {city.upper()} :")
                st.write(f"Weather: {general}")
                st.image(icon)
            with col2:
                st.metric(label="🌡️ Temperature", value=f"{temp}°C")
                st.metric(label="💨 Wind Speed", value=f"{wind} m/s")
                st.metric(label="💧 Humidity", value=f"{humidity}%")
        else:
            st.warning("⚠️ Please enter a valid city name.")

if __name__ == '__main__':
    main()
