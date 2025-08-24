import argparse
import requests
import time
from http.cookies import SimpleCookie

def parse_cookie(cookie_string):
    """Parsea una cadena de cookie en un diccionario"""
    if not cookie_string:
        return None
    
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    return {key: morsel.value for key, morsel in cookie.items()}

def perform_request(url, data, cookie_string):
    url_with_data = f"{url}{data}"
    start_time = time.time()

    try:
        cookies_dict = parse_cookie(cookie_string) if cookie_string else None
        
        response = requests.get(
            url_with_data, 
            cookies=cookies_dict,
            timeout=20  
        )
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        return False, url_with_data, time.time() - start_time, str(e)

    return True, url_with_data, time.time() - start_time, None

def main():
    parser = argparse.ArgumentParser(description="Realiza una petición GET a múltiples URLs con diferentes datos.")
    parser.add_argument("-u", "--urls", required=True, help="Archivo de texto con las URLs a las que se les realizará la petición GET.")
    parser.add_argument("-d", "--data", required=True, help="Archivo de texto con los datos que se agregarán a las URLs.")
    parser.add_argument("-c", "--cookie", help="Cookie a incluir en la petición GET (formato: 'nombre=valor; nombre2=valor2').")
    args = parser.parse_args()

    with open(args.urls) as file:
        urls = file.read().splitlines()

    with open(args.data) as file:
        data = file.read().splitlines()

    for url in urls:
        for d in data:
            success, url_with_data, response_time, error_message = perform_request(url, d, args.cookie)

            if success and response_time <= 20:
                print(f"\033[1;32mURL {url_with_data} - {response_time:.2f} segundos\033[0m")
            else:
                print(f"\033[1;31mURL {url_with_data} - {response_time:.2f} segundos - Error: {error_message}\033[0m")

if __name__ == "__main__":
    main()
