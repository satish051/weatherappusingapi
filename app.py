from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key (replace with your own)
API_KEY = "7f1ac843120588d2efe796546a4f2d22"

@app.route('/')
def index():
    return render_template('index.html')
                    
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    if not city:
        return render_template('index.html', error='Please enter a city name.')

    # Fetch weather data from OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return render_template('weather.html', weather_data=weather_data)
    else:
        error_message = data['message'] if 'message' in data else 'Unknown error'
        return render_template('index.html', error=f'Error: {error_message}')

if __name__ == '__main__':
    app.run(debug=True)

