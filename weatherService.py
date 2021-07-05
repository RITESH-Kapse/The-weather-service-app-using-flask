import requests

class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5/forecast' #?q={city name},{country code}
    appId = '7af825b7884fb9d0320b4b344bdef378'

    @classmethod
    def getForecast(cls, city, country):
        response = requests.get(cls.baseUrl, params=[
            ('appId', cls.appId),
            ('q',f'{city},{country}')
        ])
        data = response.json()
        return data['list']



if __name__ == "__main__":
    print(WeatherService.getForecast('new york','us'))