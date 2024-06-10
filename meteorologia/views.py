from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests


def api_lista_cidades(request):
    url_cidades = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url_cidades)
    data = response.json()
    return JsonResponse(data)

def api_tempo_hoje(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()
    return JsonResponse(data['data'][0])

def api_tempo_5_dias(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()
    return JsonResponse(data['data'][:5], safe=False)


def tempo_hoje(request, city_id):
    # URL para obter a previsão do tempo da cidade
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()

    # Verifica se a chave 'data' está presente no JSON retornado
    if 'data' not in data:
        context = {'error': 'Weather data not available'}
        return render(request, 'meteorologia/tempo_hoje.html', context)

    # Pega a previsão do tempo de hoje
    weather_today = data['data'][0]
    city = f'City ID: {city_id}'
    min_temp = weather_today["tMin"]
    max_temp = weather_today["tMax"]
    weather_type_id = weather_today["idWeatherType"]
    date = weather_today["forecastDate"]

    # URL para obter a descrição do tipo de clima
    weather_desc_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    response = requests.get(weather_desc_url)

    if response.status_code != 200:
        context = {'error': 'Failed to retrieve weather description data'}
        return render(request, 'meteorologia/tempo_hoje.html', context)

    weather_desc_data = response.json()['data']
    weather_desc = next((item for item in weather_desc_data if item["idWeatherType"] == weather_type_id), None)

    if not weather_desc:
        context = {'error': 'Weather description not available'}
        return render(request, 'meteorologia/tempo_hoje.html', context)

    weather_desc = weather_desc['descWeatherTypePT']

    if(weather_type_id >= 10):
        icon_url = f"/static/meteorologia/w_ic_d_{weather_type_id}anim.svg"
    else:
        icon_url = f"/static/meteorologia/w_ic_d_0{weather_type_id}anim.svg"

    context = {
        'city': city,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'date': date,
        'weather_desc': weather_desc,
        'icon_url': icon_url,
    }

    return render(request, 'meteorologia/tempo_hoje.html', context)


def tempo_hoje_lisboa(request):
    url_lisboa = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(url_lisboa)
    data = response.json()

    weather_today = data['data'][0]
    city = 'Lisboa'
    min_temp = weather_today['tMin']
    max_temp = weather_today['tMax']
    weather_type_id = weather_today['idWeatherType']
    date = weather_today['forecastDate']

    weather_desc_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    response = requests.get(weather_desc_url)
    weather_desc_data = response.json()['data']
    weather_desc = next(item for item in weather_desc_data if item["idWeatherType"] == weather_type_id)['descWeatherTypePT']

    if(weather_type_id >= 10):
        icon_url = f"/static/meteorologia/w_ic_d_{weather_type_id}anim.svg"
    else:
        icon_url = f"/static/meteorologia/w_ic_d_0{weather_type_id}anim.svg"

    context = {
        'city': city,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'date': date,
        'weather_desc': weather_desc,
        'icon_url': icon_url,
    }

    return render(request, 'meteorologia/tempo_hoje_lisboa.html', context)


def cidades(request):
    url_cidades = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url_cidades)
    data = response.json()

    cities = data['data']

    if 'city_id' in request.GET:
        city_id = request.GET['city_id']
        return redirect('meteorologia:tempo_hoje', city_id=city_id)

    context = {
        'cities': cities,
    }

    return render(request, 'meteorologia/cidades.html', context)


def tempo_5_dias(request, city_id):
    url_cidade = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(url_cidade)
    data = response.json()

    weather_data = data['data'][:5]

    for day in weather_data:
        weather_type_id = day["idWeatherType"]
        if weather_type_id >= 10:
            day['icon_url'] = f"/static/meteorologia/w_ic_d_{weather_type_id}anim.svg"
        else:
            day['icon_url'] = f"/static/meteorologia/w_ic_d_0{weather_type_id}anim.svg"

    context = {
        'weather_data': weather_data,
    }

    return render(request, 'meteorologia/tempo_5_dias.html', context)

