import asyncio
from aiohttp import ClientSession

async def get_weather(session, city):
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': 'fc7ebccb3af53b048a7da5ad3e403215'}
        async with session.get(url=url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                print(f'Погода в {data["name"]}, {data["sys"]["country"]}')
                print(f'Температура: {int(data["main"]["temp"]-273.15)}°C')
                print(f'Минимальная температура: {int(data["main"]["temp_min"]-273.15)}°C')
                print(f'Максимальная температура: {int(data["main"]["temp_max"]-273.15)}°C')
                print(f'Давление: {data["main"]["pressure"]} Па')
                print(f'Влажность: {data["main"]["humidity"]}%')
                print(f'Ветер: {data["wind"]["speed"]} м/с')
            else:
                print('Проверить правильность введённых данных!')


async def main():
    async with ClientSession() as session:
        while True:
            choice = input('Введите город или оставьте поле пустым для отображения температуры в популярных городах: ')
            if choice:
                await get_weather(session, choice)
            else:
                cities = ['Madrid', 'Tokyo', 'Amsterdam', 'Paris', 'Berlin', 'London', 'New York', 'Dubai', 'Rim', 'Barcelona']
                tasks = [get_weather(session, city) for city in cities]
                await asyncio.gather(*tasks)
            break

asyncio.run(main())



