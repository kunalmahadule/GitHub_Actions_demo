from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    temperature = None
    city = None
    error = None

    if request.method == "POST":

        city = request.form["city"]

        # first find latitude and longitude of the city
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {"name": city, "count": 1, "language": "en", "format": "json"}

               
        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()



        if "results" not in geo_data:
            error = "City not found."

        else:
            latitude = geo_data["results"][0]["latitude"]
            longitude = geo_data["results"][0]["longitude"]

            # Get current temperature
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params
            )

            weather_data = weather_response.json()

            temperature = weather_data["current"]["temperature_2m"]

    return render_template(
        "index.html",
        city=city,
        temperature=temperature,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5005)
