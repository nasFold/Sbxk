# live-score-app/update_scores.py
import requests

url = 'https://narpk.pythonanywhere.com/update_scores'
data = {'country': 'Country 1', 'score': 3, 'time': '60:00', 'scorer': 'Player C'}

response = requests.post(url, data=data)
print(response.text)
