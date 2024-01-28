# termux_update.py
import requests

def update_live_score(match_id, data):
    api_url = "https://Nrlive.pythonanywhere.com/api/update_score/{}".format(match_id)
    response = requests.post(api_url, json=data)
    print(response.json())

# Contoh data yang akan diupdate
match_id = 123
update_data = {
    "skor": {
        "tim1": 2,
        "tim2": 1
    },
    "waktu": "45:00",
    "pencetak_gol": [
        {"tim": "tim1", "pencetak": "Player A", "waktu": "30:00"},
        {"tim": "tim2", "pencetak": "Player B", "waktu": "40:00"}
    ]
}

update_live_score(match_id, update_data)
