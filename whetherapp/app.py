from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Replace YOUR_API_KEY with your actual OpenWeatherMap API key
api_key = '92f32a2e16eca3b5998bd84e3a0d85f5'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = json.loads(response.text)
        print(data)
        if response.status_code == 200:
            weather = {
                'city': city,
                'temperature': round(data['main']['temp']),
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = None
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
