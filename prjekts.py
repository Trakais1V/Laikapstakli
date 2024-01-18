import requests

def get_weather_wttr(city):
    url = f"https://wttr.in/{city}?format=%t+%C+%w"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.text.strip()
            print(f"Weather in {city}: {weather_data}")

        else:
            print(f"Error: Unable to fetch data from {url}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Pilsetas izvele
    city = 'Riga'

    get_weather_wttr(city)

if __name__ == "__main__":
    main()
