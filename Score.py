import requests

def update_score(skor, waktu, pencetak_gol):
    url = "http://your_username.000webhostapp.com/update-score"
    payload = {"skor": skor, "waktu": waktu, "pencetakGol": pencetak_gol}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

# Contoh penggunaan
skor_baru = "1-0"
waktu_baru = "30:00"
pencetak_gol_baru = "Player A"

result = update_score(skor_baru, waktu_baru, pencetak_gol_baru)
if result:
    print(result)
