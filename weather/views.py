from django.shortcuts import render
from .forms import CityForm
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

def index(request):
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = os.getenv('API_KEY')  # 環境変数からAPIキーを取得
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            print(f'Request URL: {url}')  # デバッグ用
            response = requests.get(url)
            print(f'Status Code: {response.status_code}')  # デバッグ用
            print(f'Response JSON: {response.json()}')  # デバッグ用
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}
    else:
        form = CityForm()
    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data})
