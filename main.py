import http.client
import json
import time
import random

# Datos del host y la URL
host = "api.tellonym.me"
url = "/tells/new"
mensajes = 0
retries = 0

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
]

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
    user_agent = random.choice(user_agents)


    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es-ES,es;q=0.7",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://tellonym.me",
    "Referer": "https://tellonym.me/",
    'Sec-Ch-Ua': random.choice(['"Microsoft Edge";v="123"', '"Not:A-Brand";v="8"', '"Chromium";v="123"']),
    'Sec-Ch-Ua-Mobile': random.choice(['?0', '?1']),
    'Sec-Ch-Ua-Platform': random.choice(['"Windows"', '"Linux"', '"Macintosh"', '"Android"', '"iOS"']),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-Gpc": "1",
    "Tellonym-Client": "web:3.108.0",
    'User-Agent': user_agent
}
    
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
            retries += 1
            print(f"[!] Límite de peticiones excedido. Esperando 15 segundos...")
            time.sleep(15)
        else:
            print(f"[!] Error: Estado de respuesta: {response.status}, Mensaje: {data.decode('utf-8')}")
        
        conn.close()
    except Exception as e:
        print(f"[!] Error de conexión: {e}")
    

    
    time.sleep(1)  # Espera 1 segundo antes de enviar el próximo mensaje
