import requests

API_KEY = "2ba2e24aa37aae67604024e88c9d6631"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Check if the API returned an error or if 'list' key exists
    if "list" not in data:
        return None  # Return None if there's no 'list' key

    filtered_data = data["list"]

    if forecast_days is not None:
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Accra", forecast_days=3))