from flask import Flask, render_template, url_for, flash, request
from forms import SearchForm
import sys
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2ec075169a60bc07986ccca6decee87'

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()

    if form.validate_on_submit():

        # grab the zip code that was entered
        searchZip = form.zip.data

        # make api request for weather
        weather_url = f'https://weather-api-361.herokuapp.com/zip?zip={searchZip}'
        response = requests.get(weather_url).json()

        #make api request for map
        map_url = f'https://lamjenni-image.herokuapp.com/streetmap,300,300'
      

        conditions = response['Conditions']
        temp = response['Temp']
        temp = int(temp)


        # make api request for image
        image_url = f'https://lamjenni-image.herokuapp.com/{conditions},150,150'
        
        return render_template('home.html', map_url=map_url, image_url = image_url, form=form, city = response['City'], temp = temp, conditions = response['Conditions'])

    else:
        print('else', file=sys.stderr)
        return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)