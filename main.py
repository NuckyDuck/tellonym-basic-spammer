import http.client
import json
import time
import random

host = "api.tellonym.me"
url = "/tells/new"
mensajes = 0
retries = 0

tokens = [
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA1MzcxMTk2LCJpYXQiOjE3MTg2NzkxNzB9.eLb8oVjhHObcCU_Srr5x7nbyDkqTjlOChBUX8Dp-P_E",
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTA1MzY2NzIzLCJpYXQiOjE3MTg2NjY1MTZ9.yRPb5hS1hSLc9TSdgcYMNDUGRaseh4V1d5aNd84QlnA",
]

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
    diccionario = random.choice(dic_msg)
    token = random.choice(tokens)
    payload = json.dumps({
        "isInstagramInAppBrowser": False,
        "isSnapchatInAppBrowser": False,
        "isSenderRevealed": False,
        "tell": diccionario,
        "userId": 105347342,
        "username": "funa.luismadina"
    })
    user_agent = random.choice(user_agents)

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "es-ES,es;q=0.7",
        "Authorization": token,
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
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", url, body=payload, headers=headers)

        response = conn.getresponse()
        content_type = response.getheader('Content-Type')
        data = response.read()

        if response.status == 200:
            mensajes += 1
            print(f"[+] Mensaje enviado. Total mensajes enviados: {mensajes} - {diccionario} - {token}")
            time.sleep(3)
        elif response.status == 429:
            retries += 1
            print(f"[!] Límite de peticiones excedido. Esperando 20 segundos...")
            time.sleep(20)
        else:
            if content_type and 'application/json' in content_type:
                try:
                    message = data.decode('utf-8')
                    print(f"[!] Error: Estado de respuesta: {response.status}, Mensaje: {message}")
                except UnicodeDecodeError as e:
                    print(f"[!] Error al decodificar la respuesta: {e}")
                    print(f"[!] Respuesta cruda: {data}")
            else:
                print(f"[!] Error: Estado de respuesta: {response.status}, Datos no son JSON: {data}")

        conn.close()
    except Exception as e:
        print(f"[!] Error de conexión: {e}")

    if retries >= 20:
        print("[!] Alcanzado el límite de 20 re-peticiones. Esperando 5 minutos antes de continuar...")
        time.sleep(300)
        retries = 0

    time.sleep(1)
