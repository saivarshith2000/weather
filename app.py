__author__ = 'Sai Varshith'
__copyright__ = 'Copyright 2018 @ Sai Varshith'

from flask import Flask,render_template,request
import weather
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['location'].lower()
        if city == '':
            return render_template('index.html', error='Please enter a city')
        else:
            while True:
                try:
                    weather_data = weather.get_by_city(city)['data'][0]
                    # print(weather_data) for console purposes
                    return render_template('index.html', weather=weather_data)
                    break;
                except json.decoder.JSONDecodeError:
                    return render_template("index.html", error="Oops! Please enter a Valid City Name ")

    return render_template('index.html')
    
@app.route('/location/')
def location():
    weather_data = weather.get_by_location()['data'][0]
    # print(weather_data) for console purposes
    return render_template('index.html',weather=weather_data)
    
if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run()

