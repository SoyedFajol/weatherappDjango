from django.shortcuts import render
import requests

def index(request):
    city = request.GET.get('city', 'London')
    api_key = '40d8feb7035550a36c441b73214b72ce'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

    weather_data = {}
    error_message = None

    try:
        response = requests.get(url)
        data = response.json()  # Parse JSON response

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'], 
                'wind_speed': data['wind']['speed'],  
                'description': data['weather'][0]['description'],
                
            }
        else:
            error_message = f"Error: {data.get('message', 'Failed to fetch data')}"

    except requests.exceptions.RequestException as e:
        error_message = f"API request failed: {str(e)}"

    return render(request, 'weather/index.html', {'weather_data': weather_data, 'error_message': error_message})
