import http.client
import json
import time
import random

# Datos del host y la URL
host = "api.tellonym.me"
url = "/tells/new"
mensajes = 0

# Lista de mensajes
dic_msg = [
    "PERROS HPTAS!",
    "¿SE SALVARON? JAJAJ",
    "PAYASOS!!",
    "MARICONES",
    "NO SE VAN A SALVAR TAN FACIL",
    "CIERRAN LA MALPARIDA CUENTA DE UNA VEZ",
    "NO MARIQUEEN MÁS",
    "A NADIE LE GUSTAN LOS SAPOS",
    "HPTAS RANAS"
]

# Definir los headers
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es-ES,es;q=0.7",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA1MzY2NzIzLCJpYXQiOjE3MTg2NjY1MTZ9.yRPb5hS1hSLc9TSdgcYMNDUGRaseh4V1d5aNd84QlnA",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://tellonym.me",
    "Referer": "https://tellonym.me/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-Gpc": "1",
    "Tellonym-Client": "web:3.108.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

while True:
    # Seleccionar un mensaje aleatorio de la lista
    diccionario = random.choice(dic_msg)

    # Crear el payload con el mensaje seleccionado
    payload = json.dumps({
        "isInstagramInAppBrowser": False,
        "isSnapchatInAppBrowser": False,
        "isSenderRevealed": False,
        "limit": 13,
        "referalId": 154,
        "referralType": "dice",
        "tell": diccionario,
        "userId": 105347342,
        "username": "funa.luismadina"
    })
    
    try:
        # Configurar la conexión HTTP
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", url, body=payload, headers=headers)

        # Obtener la respuesta
        response = conn.getresponse()
        data = response.read()

        if response.status == 200:
            mensajes += 1
            print(f"[+] Mensaje enviado. Total mensajes enviados: {mensajes} - {diccionario}")
            time.sleep(3)
        elif response.status == 429:
            print(f"[!] Límite de peticiones excedido. Esperando 15 segundos...")
            time.sleep(15)
        else:
            print(f"[!] Error: Estado de respuesta: {response.status}, Mensaje: {data.decode('utf-8')}")
        
        conn.close()
    except Exception as e:
        print(f"[!] Error de conexión: {e}")
    
    time.sleep(1)  # Espera 1 segundo antes de enviar el próximo mensaje
