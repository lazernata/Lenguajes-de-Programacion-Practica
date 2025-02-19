import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ['OWKEY']

city = 'Seville'

def obtener_coordenadas(city):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}')
    response.raise_for_status()
    data = response.json()[0]
    return data['lon'], data['lat']

def main():
    city = 'Seville'
    lon, lat = obtener_coordenadas(city)
    weather_response = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast',
        params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    )
    weather_response.raise_for_status()
    df = pd.json_normalize(weather_response.json(), 'list')
    print(df)

if __name__ == '__main__':
    main()