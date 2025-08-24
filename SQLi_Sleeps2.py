import argparse
import requests
import time
import random
from http.cookies import SimpleCookie

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
    "Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0"
]

def parse_cookie(cookie_string):
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
        headers = {'User-Agent': random.choice(user_agents)}
        
        response = requests.get(
            url_with_data, 
            cookies=cookies_dict,
            headers=headers,
            timeout=20  
        )
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        return False, url_with_data, time.time() - start_time, str(e)

    return True, url_with_data, time.time() - start_time, None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--urls", required=True)
    parser.add_argument("-d", "--data", required=True)
    parser.add_argument("-c", "--cookie")
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
