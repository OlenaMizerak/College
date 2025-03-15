import requests
from flask import Flask, render_template

app = Flask(__name__)

API_URL = "https://api.jikan.moe/v4/anime/54595/episodes"

def get_anime_episodes():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Перевіряє статус відповіді
        return response.json()  # Повертає JSON-дані
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def home():
    episodes_data = get_anime_episodes()

    if "error" in episodes_data:
        return f"<p>Помилка при завантаженні даних: {episodes_data['error']}</p>"

    output = ""
    for episode in episodes_data.get("data", []):
        episode_id = episode.get("mal_id", "N/A")
        title = episode.get("title", "Без назви")
        score = episode.get("score", "Немає оцінки")
        output += f"<p>Епізод {episode_id}: {title}, оцінка {score}</p>"
    
    return output

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
