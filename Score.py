import requests

def update_live_score(match_id, data):
    api_url = "https://Nrlive.pythonanywhere.com/api/update_score/{}".format(match_id)
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

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
