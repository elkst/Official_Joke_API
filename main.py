import requests

def get_random_programming_joke():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    try:
        response = requests.get(url)
        data = response.json()
        if data:
            joke = data[0]['setup'] + " " + data[0]['punchline']
            return joke
        else:
            return "Шутка не найдена"
    except Exception as e:
        return f"Ошибка при получении шутки: {str(e)}"

if __name__ == "__main__":
    print(get_random_programming_joke())
