import requests

def update_score(skor, waktu, pencetak_gol, negara_A, negara_B):
    url = "http://nar.pythonanywhere.com/update-score"
    payload = {"skor": skor, "waktu": waktu, "pencetakGol": pencetak_gol, "negaraA": negara_A, "negaraB": negara_B}
    response = requests.post(url, json=payload)
    return response.json()

# Contoh penggunaan
skor_baru = "1-0"
waktu_baru = "30:00"
pencetak_gol_baru = "Player A"
negara_A_baru = "Indonesia"
negara_B_baru = "Belanda"

result = update_score(skor_baru, waktu_baru, pencetak_gol_baru, negara_A_baru, negara_B_baru)
print(result)
